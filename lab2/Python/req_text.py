"""
www
"""

import requests

x = requests.get(
    "https://w3schools.com/python/demopage.htm",
    headers={"User-Agent": "Mozilla/5.0"},
    allow_redirects=False,
    stream=True,
    verify=False,
    proxies={"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"},
    timeout=5,
    params={"key1": "value1", "key2": "value2"},
)

print(x.text)
