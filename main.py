import glob
import os
import json
import requests
# from urllib.parse import urlencode
# from urllib.request import Request, urlopen


def doProcess(js):
    v = ""  # "v1"
    h = ""  # "https://petstore.swagger.io/v1"
    if "info" in js:
        if "version" in js['info']:
            v = js['info']['version']

    if "host" in js:
        h = js['host']

    if not v and not h:
        print("Version and Host not detected!!")
        return

    secret = "03d03045c78944cf5fa65e8e9a2bd8eb"
    url = "http://10.2.29.43:3000/api/import/swagger/"
    # auth = "Authorization: " + secret
    # ct = "Content-Type: application/json"
    out = json.dumps(js)

    data = {
        "swagger": out,
        "insert_into_api": False,
        "version_name": v,
        "upstream_url": h
    }
    header = {
        'Content-Type': 'application/json',
        'Authorization': secret
    }
    # print(data)
    r = requests.post(url, json=data, headers=header)
    print(r.json())


os.chdir(".")
for file in glob.glob("*.json"):
    f = open(file)
    j = json.load(f)
    doProcess(j)
