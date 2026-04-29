"""
app
"""

import os

import sentry_sdk


def init_sentry():
    """initialize sentry"""
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        environment=os.getenv("SENTRY_ENVIRONMENT", "development"),
        traces_sample_rate=1.0,
    )
    print(os.getenv("SENTRY_DSN"))


def check_logins(input_string):
    """
    check logins
    """
    logins_list = [login for login in input_string.replace(",", " ").split() if login]

    if not logins_list:
        raise ValueError("logs list is empty")

    return len(logins_list)


def main():
    """main function"""
    init_sentry()
    try:
        print("enter logins:")
        user_input = input()

        count = check_logins(user_input)
        print(f"logins count: {count}")

    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f"\nerror: {e}")
        raise


if __name__ == "__main__":
    main()
