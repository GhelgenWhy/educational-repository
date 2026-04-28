pip install requests
python -m venv venv
.venv\Scripts\activate
pip install requests

```
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)
```

python .\req_text.py
pip install pip-audit
pip freeze > requirements.txt
pip install -r requirements.txt
pip-audit
