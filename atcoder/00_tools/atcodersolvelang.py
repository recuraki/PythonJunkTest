from pprint import pprint
import requests
import json
import time
import pathlib
import sys
import logging
import argparse
logging.basicConfig(level=logging.DEBUG)

timeCache = 300 # キャッシュする時間(sec)
username="recuraki"

fUseCache = True

time.sleep(1) # 連打した時にAPI側に変な負荷がかからないようにお気持ち

jsondat = None
def getJsonFromAPI():
    global jsondat
    req = requests.get(url)
    jsondat = json.loads(req.text)

######################

import argparse
parser = argparse.ArgumentParser(description='Atcoder Solved Problems')
parser.add_argument('-u', '--user', default=None, dest="username")
parser.add_argument('-n', '--no-cache', action="store_true", dest="nocache")

args = parser.parse_args()
if args.username != None:
    username = args.username
if args.nocache is True:
    fUseCache = False

######################
url="https://kenkoooo.com/atcoder/atcoder-api/results?user={0}".format(username)
pathCache="./cache.{0}.json".format(username)
######################

if fUseCache is True:
    logging.debug("USE CACHE: ON[filename:{0}]".format(pathCache))
    plCache = pathlib.Path(pathCache)
    if plCache.exists():
        logging.debug(" CACHE FILE EXIST")
        lastUpdate = int(plCache.stat().st_mtime)
        curTime = int(time.time())
        logging.debug(" cachetime={0}, filetime={1}, nowtime={2}".format(timeCache, lastUpdate, curTime))
        if curTime - lastUpdate >= timeCache:
            logging.debug(" cache expired...")
            getJsonFromAPI()
            print(jsondat)
            with open(pathCache, "w") as fw:
                logging.debug(" CACHE WROTE...")
                json.dump(jsondat, fw)
        else:
            logging.debug(" USE CACHE!")
            with open(pathCache, "r") as fr:
                jsondat = json.load(fr)
    else:
        logging.debug(" CACHE FILE NOEXIST")
        getJsonFromAPI()
        print(jsondat)
        with open(pathCache, "w") as fw:
            logging.debug(" CACHE WROTE...")
            json.dump(jsondat, fw)
else:
    logging.debug("USE CACHE: OFF")
    getJsonFromAPI()

# ACしたものだけ抜き出す
acdat = filter(lambda x: x["result"] == "AC", jsondat)
acdat = list(acdat)
acNum = len(acdat) # AC数

# それぞれのACについて，probID - languageで辞書に突っ込む
import collections
acProb = collections.defaultdict(list)
for item in acdat:
    problem_id = item["problem_id"]
    language = item["language"]
    language = language.split("(")[0]
    language = language.replace(" ", "")
    if language not in acProb[problem_id]:
        acProb[problem_id].append(language)

#表示する
probNames = acProb.keys()
probNames = list(probNames)
probNames.sort()
for k in probNames:
    langs = acProb[k]
    langs.sort()
    print("{0} {1}".format(k, " ".join(langs)))


