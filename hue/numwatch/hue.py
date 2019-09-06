import json
import urllib.request
from pprint import pprint
from xy import rgb2xy
import argparse

class hue():
    url = ""

    def __init__(self, hostname, key, light = 1):
        self.url = "http://{0}/api/{1}/".format(hostname, key)
        self.light = light

    def setrgb(self, red, green, blue, bri=128):
        r, g, b = int(red), int(green), int(blue)
        bri = int(bri)

        data = {"on": True, "bri": 0, "xy": [0,0] }
        headers = {'Content-Type': 'application/json',}
        requrl = self.url + "lights/{0}/state".format(self.light)
        print(requrl)


        x, y = rgb2xy(r, g, b)

        data["bri"] = bri
        data["xy"] = [x, y]

        req = urllib.request.Request(requrl, json.dumps(data).encode(), headers, method='PUT')
        with urllib.request.urlopen(req) as res:
            body = res.read()
            resHue = json.loads(body)
            resHue = resHue[0]
            pprint(resHue)
            if "error" in resHue:
                raise ValueError
            if "success" in resHue:
                pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='hue test')
    parser.add_argument('-k', '--key', help='hue key')
    parser.add_argument('-s', '--hostname', help='bridge server hostname')
    parser.add_argument('-l', '--lights', help='lights number', default="1")
    parser.add_argument('-r', '--red', help='red')
    parser.add_argument('-g', '--green', help='green')
    parser.add_argument('-b', '--blue', help='blue')
    parser.add_argument('--bri', help='bright', default=128)
    args = parser.parse_args()

    h = hue(hostname = args.hostname, key = args.key, light=args.lights)
    h.setrgb(args.red, args.green, args.blue, bri=args.bri)
