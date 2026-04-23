/***************************************************************************
 *                                  _   _ ____  _
 *  Project                     ___| | | |  _ \| |
 *                             / __| | | | |_) | |
 *                            | (__| |_| |  _ <| |___
 *                             \___|\___/|_| \_\_____|
 *
 * Copyright (C) Daniel Stenberg, <daniel@haxx.se>, et al.
 *
 * This software is licensed as described in the file COPYING, which
 * you should have received as part of this distribution. The terms
 * are also available at https://curl.se/docs/copyright.html.
 *
 * You may opt to use, copy, modify, merge, publish, distribute and/or sell
 * copies of the Software, and permit persons to whom the Software is
 * furnished to do so, under the terms of the COPYING file.
 *
 * This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
 * KIND, either express or implied.
 *
 * SPDX-License-Identifier: curl
 *
 ***************************************************************************/
#include "curl_setup.h" // підключаємо файл конфігурації "curl_setup.h"

#ifdef __AMIGA__ // якщо це AmigaOS

#include "amigaos.h"       // підключаємо файл "amigaos.h"
#include "curl_addrinfo.h" // підключаємо файл "curl_addrinfo.h"
#include "hostip.h"        // підключаємо файл "hostip.h"

#ifdef HAVE_PROTO_BSDSOCKET_H         // якщо встановлено макрос HAVE_PROTO_BSDSOCKET_H
#ifdef __amigaos4__                   // якщо це AmigaOS 4.x
#include <bsdsocket/socketbasetags.h> // підключаємо файл "socketbasetags.h"
#elif !defined(USE_AMISSL)            // якщо не використовується AmiSSL
#include <amitcp/socketbasetags.h>    // підключаємо файл "socketbasetags.h"
#endif
#ifdef __libnix__  // якщо встановлено макрос __libnix__
#include <stabs.h> // підключаємо файл "stabs.h"
#endif
#endif

#ifdef HAVE_PROTO_BSDSOCKET_H // якщо встановлено макрос HAVE_PROTO_BSDSOCKET_H

#ifdef __amigaos4__ // якщо це AmigaOS 4.x
/*
 * AmigaOS 4.x specific code
 */

/*
 * hostip4.c - Curl_ipv4_resolve_r() replacement code
 *
 * Logic that needs to be considered are the following build cases:
 * - newlib networking
 * - clib2 networking
 * - direct bsdsocket.library networking (usually AmiSSL builds)
 * Each with the threaded resolver enabled or not.
 *
 * With the threaded resolver enabled, try to use gethostbyname_r() where
 * available, otherwise (re)open bsdsocket.library and fallback to
 * gethostbyname().
 */

#include <proto/bsdsocket.h> // підключаємо файл "bsdsocket.h"

static struct SocketIFace *__CurlISocket = NULL;
static uint32 SocketFeatures = 0;

#define HAVE_BSDSOCKET_GETHOSTBYNAME_R 0x01 // константа зі значенням 0x01
#define HAVE_BSDSOCKET_GETADDRINFO 0x02     // константа зі значенням 0x02

CURLcode Curl_amiga_init(void) // функція ініціалізаціЇ
{
  struct SocketIFace *ISocket; // структура "SocketIFace"
  struct Library *base = OpenLibrary(
      "bsdsocket.library", 4); // відкриваємо бібліотеку "bsdsocket.library"

  if (base)
  { // якщо бібліотека "bsdsocket.library" існує
    ISocket = (struct SocketIFace *)GetInterface(
        base, "main", 1, NULL); // отримуємо інтерфейс "SocketIFace"
    if (ISocket)
    {                    // якщо інтерфейс "SocketIFace" існує
      ULONG enabled = 0; // змінна "enabled"

      SocketBaseTags(SBTM_SETVAL(SBTC_CAN_SHARE_LIBRARY_BASES), TRUE,
                     SBTM_GETREF(SBTC_HAVE_GETHOSTADDR_R_API), (ULONG)&enabled,
                     TAG_DONE);

      if (enabled)
      { // якщо "enabled" існує
        SocketFeatures |=
            HAVE_BSDSOCKET_GETHOSTBYNAME_R; // встановлюємо прапорець
                                            // "HAVE_BSDSOCKET_GETHOSTBYNAME_R"
      }

      __CurlISocket = ISocket; // зберігаємо інтерфейс "SocketIFace"

      atexit(Curl_amiga_cleanup); // викликаємо функцію "Curl_amiga_cleanup"

      return CURLE_OK; // повертаємо CURLE_OK
    }
    CloseLibrary(base); // закриваємо бібліотеку "bsdsocket.library"
  }

  return CURLE_FAILED_INIT; // повертаємо CURLE_FAILED_INIT
}

void Curl_amiga_cleanup(void) // функція очищення
{
  if (__CurlISocket)
  {                                                     // якщо інтерфейс "SocketIFace" існує
    struct Library *base = __CurlISocket->Data.LibBase; // отримуємо бібліотеку
    DropInterface((struct Interface *)__CurlISocket);   // видаляємо інтерфейс
    CloseLibrary(base);                                 // закриваємо бібліотеку
    __CurlISocket = NULL;                               // встановлюємо NULL
  }
}

#ifdef CURLRES_AMIGA // якщо встановлено макрос CURLRES_AMIGA
/*
 * Because we need to handle the different cases in hostip4.c at runtime,
 * not at compile-time, based on what was detected in Curl_amiga_init(),
 * we replace it completely with our own as to not complicate the baseline
 * code. Assumes malloc/calloc/free are thread-safe because Curl_he2ai()
 * allocates memory also.
 */

struct Curl_addrinfo *Curl_ipv4_resolve_r(const char *hostname,
                                          int port) // функція визначення
{
  struct Curl_addrinfo *ai = NULL;             // структура "Curl_addrinfo"
  struct hostent *h;                           // структура "hostent"
  struct SocketIFace *ISocket = __CurlISocket; // інтерфейс "SocketIFace"

  if (SocketFeatures &
      HAVE_BSDSOCKET_GETHOSTBYNAME_R)
  {                      // якщо "SocketFeatures" містить
                         // константу
                         // "HAVE_BSDSOCKET_GETHOSTBYNAME_R"
    LONG h_errnop = 0;   // змінна "h_errnop"
    struct hostent *buf; // структура "hostent"

    buf = curlx_calloc(1, CURL_HOSTENT_SIZE); // виділяємо пам'ять
    if (buf)
    { // якщо буфер існує
      h = gethostbyname_r((STRPTR)hostname, buf,
                          (char *)buf + sizeof(struct hostent),
                          CURL_HOSTENT_SIZE - sizeof(struct hostent),
                          &h_errnop); // викликаємо функцію "gethostbyname_r"
      if (h)
      {                           // якщо "h" існує
        ai = Curl_he2ai(h, port); // визначаємо IP
      }
      curlx_free(buf); // звільняємо пам'ять
    }
  }
  else
  {
#ifdef CURLRES_THREADED // якщо встановлено макрос CURLRES_THREADED
    /* gethostbyname() is not thread-safe, so we need to reopen bsdsocket
     * on the thread's context
     */
    struct Library *base =
        OpenLibrary("bsdsocket.library", 4); // отримуємо бібліотеку
    if (base)
    { // якщо бібліотека існує
      ISocket = (struct SocketIFace *)GetInterface(base, "main", 1,
                                                   NULL); // отримуємо інтерфейс
      if (ISocket)
      { // якщо інтерфейс існує
        h = gethostbyname(
            (STRPTR)hostname); // викликаємо функцію "gethostbyname"
        if (h)
        {                           // якщо "h" існує
          ai = Curl_he2ai(h, port); // визначаємо IP
        }
        DropInterface((struct Interface *)ISocket); // видаляємо інтерфейс
      }
      CloseLibrary(base); // закриваємо бібліотеку
    }
#else
    /* not using threaded resolver - safe to use this as-is */
    h = gethostbyname(hostname); // викликаємо функцію "gethostbyname"
    if (h)
    {                           // якщо "h" існує
      ai = Curl_he2ai(h, port); // визначаємо IP
    }
#endif
  }

  return ai; // повертаємо "Curl_addrinfo"
}
#endif /* CURLRES_AMIGA */

#ifdef USE_AMISSL   // якщо встановлено макрос USE_AMISSL
#include <signal.h> // підключаємо бібліотеку "signal.h"
int Curl_amiga_select(int nfds, fd_set *readfds, fd_set *writefds,
                      fd_set *errorfds,
                      struct timeval *timeout) // функція "Curl_amiga_select"
{
  int r = WaitSelect(nfds, readfds, writefds, errorfds, timeout,
                     0); // викликаємо функцію "WaitSelect"
  /* Ensure Ctrl-C signal is actioned */
  if ((r == -1) &&
      (SOCKERRNO ==
       SOCKEINTR)) // якщо "r" дорівнює -1 і "SOCKERRNO" дорівнює "SOCKEINTR"
    raise(SIGINT); // надсилаємо сигнал
  return r;        // повертаємо "r"
}
#endif /* USE_AMISSL */

#elif !defined(USE_AMISSL) /* __amigaos4__ */
/*
 * Amiga OS3 specific code
 */

struct Library *SocketBase = NULL; // змінна "SocketBase"

#ifdef __libnix__                              // якщо встановлено макрос __libnix__
void __request(const char *msg); // функція "request"
#define CURL_AMIGA_REQUEST(msg) __request(msg) // викликаємо функцію "request"
#else                                          // якщо не встановлено макрос __libnix__
#define CURL_AMIGA_REQUEST(msg) \
  Printf((const unsigned char *)(msg "\n\a"), 0) // виводимо повідомлення
#endif                                           // якщо не встановлено макрос __libnix__

void Curl_amiga_cleanup(void) // функція очищення
{
  if (SocketBase)
  {                           // якщо "SocketBase" існує
    CloseLibrary(SocketBase); // закриваємо бібліотеку
    SocketBase = NULL;        // встановлюємо NULL
  }
}

CURLcode Curl_amiga_init(void) // функція ініціалізаціЇ
{
  if (!SocketBase) // якщо "SocketBase" не існує
    SocketBase = OpenLibrary((const unsigned char *)"bsdsocket.library",
                             4); // відкриваємо бібліотеку

  if (!SocketBase)
  {                                                 // якщо "SocketBase" не існує
    CURL_AMIGA_REQUEST("No TCP/IP Stack running!"); // виводимо повідомлення
    return CURLE_FAILED_INIT;                       // повертаємо "CURLE_FAILED_INIT"
  }

  if (SocketBaseTags(SBTM_SETVAL(SBTC_ERRNOPTR(sizeof(errno))), (ULONG)&errno,
                     SBTM_SETVAL(SBTC_LOGTAGPTR), (ULONG) "curl",
                     TAG_DONE))
  {                                             // якщо "SocketBaseTags" повертає "TRUE"
    CURL_AMIGA_REQUEST("SocketBaseTags ERROR"); // виводимо повідомлення
    return CURLE_FAILED_INIT;                   // повертаємо "CURLE_FAILED_INIT"
  }

#ifndef __libnix__ // якщо не встановлено макрос __libnix__
  atexit(Curl_amiga_cleanup); // викликаємо функцію "Curl_amiga_cleanup"
#endif

  return CURLE_OK; // повертаємо "CURLE_OK"
}

#ifdef __libnix__ // якщо встановлено макрос __libnix__
ADD2EXIT(Curl_amiga_cleanup, -50); // викликаємо функцію "Curl_amiga_cleanup"
#endif

#endif /* !USE_AMISSL */

#endif /* HAVE_PROTO_BSDSOCKET_H */

#endif /* __AMIGA__ */