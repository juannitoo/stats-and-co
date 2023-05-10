# from .imports import *

import requests

req = requests.get("https://hubw3qloapa4enr2apkjuc5pkq0yioju.lambda-url.eu-west-3.on.aws/")
res = req.json()

print(res)
