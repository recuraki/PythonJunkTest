import json
import urllib.request
from pprint import pprint
import private_sample as sample
import time

url = "http://{0}/api/{1}/".format(sample.hostname, sample.key)

data = {
    "on": True,
    "bri": 0,
    "xy": [0.48, 0.41]
}


headers = {
    'Content-Type': 'application/json',
}

requrl = url + "lights/1/state"
print(requrl)
bri = 0
x = 0
y = 0
while True:
    data["bri"] = bri
    data["xy"] = [x,y]

    x = x + 0.1
    y = y + 0.1
    bri = bri + 10
    if bri > 200:
        bri = 0
    if x  > 0.8:
        x = 0
    if y > 0.7:
        y = 0

    time.sleep(0.1)
    pprint(data)

    req = urllib.request.Request(requrl, json.dumps(data).encode(), headers, method='PUT')
    with urllib.request.urlopen(req) as res:
        body = res.read()
        resHue = json.loads(body)
        resHue = resHue[0]
        pprint(resHue)
        if "error" in resHue:
            raise ValueError
        if "success" in resHue:
            print("done")
