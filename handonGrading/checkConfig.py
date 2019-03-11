import netdev
from SimpleTextLineTest import SimpleTextLineTest
from SimpleTextLineTestDecorator import SimpleTextLineTestDecorator
import asyncio
import yaml

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

class CheckConfig:
    """
    当該ホストへのtelnetを行い、指定した文字列を打って、戻り値を評価するライブラリ
    """
    debug = False
    promptName = ""
    net_connect = None
    stlt = None
    result = None
    rawReturn = None

    def __init__(self, debug = False):
        self.debug = debug
        pass

    def dp(self, d):
        if self.debug == True:
            print(d)

    async def connect(self, host, port, username, password, device_type="cisco_ios", enablePass = "cisco"):
        loginInfo = {
            "host": host,
            "username": username,
            "password": password,
            "device_type": device_type,
        }
        if device_type in ["cisco_ios"]:
            loginInfo["secret"] = password
        print(loginInfo)
        self.net_connect = netdev.create(**loginInfo)
        await self.net_connect.connect()

    async def do_singletest(self, cmd, p = [], n = []):
        """
        :param cmd: これを実施する
        :param p: 含まれるべき文字列
        :param n: 含まれてはならない文字列
        :return: 結果true or false
        """
        # 指定文字列の実行
        logger.debug("send: {0}".format(cmd))
        await asyncio.sleep(0.3)
        res = await self.net_connect.send_command(cmd)
        logger.debug("result")
        logger.debug(res)
        # 応答を評価する
        self.stlt = SimpleTextLineTest(res, p, n, debug=True)
        is_pass = self.stlt.is_pass()
        # 結果の詳細を格納
        self.result = self.stlt.result
        self.rawReturn = res
        stlt = None
        # 結果をターミナルに書く
        resultstr = self.result2str()
        for l in resultstr:
            logger.debug("!" + l)
        return is_pass

    def result2str(self):
        """
        ターミナルに出力するようの
        :param result:
        :return:
        """
        res = []
        for fp, type, pat, negline, pos in self.result:
            l = ""
            l = l + "[OK]:" if fp else "[ERROR]:"
            if type == "p":
                l = l + "INCLUDE [{0}]".format(pat)
            elif type == "n":
                l = l + "NOT-INCLUDE [{0}]".format(pat)
            res.append(l)
        return res

    def disconnect(self):
        pass

    async def test(self, diTests):
        res = []
        ipaddr = diTests.get("ipaddr", "127.0.0.1")
        port = diTests.get("port", "23")
        hostname = diTests.get("hostname", "localhost")
        username = diTests.get("username", "test")
        password = diTests.get("password", "test123")
        device_type = diTests.get("device_type", "cisco_ios")

        logger.info("connecting to: " + hostname)
        await self.connect(ipaddr, port, username, password, device_type=device_type)
        final_pass = True
        for t in diTests.get("tests", []):
            name = t.get("name", "NONAME")
            logger.debug("!!!!!!! BEGIN Test: {0}".format(name))
            cmd = t.get("cmd", [])
            p = t.get("include", [])
            n = t.get("notinclude", [])
            is_pass = await self.do_singletest(cmd, p, n)
            final_pass = final_pass and is_pass
            logger.debug("!!!!!!! END")
            logger.debug("")
            r = {}
            r["name"] = name
            r["is_pass"] = is_pass
            r["res"] = self.result
            r["cmd"] = cmd
            r["html"] = self.decorateHTML()
            res.append(r)
        r = {}
        r["hostname"] = hostname
        r["pass"] = final_pass
        ret = {}
        ret["header"] = r
        ret["test"] = res
        logger.info("finish on: " + hostname)
        return (ret)



    def writeResult(self, result):
            """
            最終結果のコンソールへの表示
            :param result:
            :return:
            """
            logger.debug("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            finalResult = True
            for name, is_pass in result:
                s = "PASS" if is_pass else "FAIL"
                finalResult = finalResult and is_pass
                logger.debug("! [{0}]: {1}".format(s, name))
            logger.debug("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            logger.debug("! FINAL RESULT [{0}]".format("PASS" if finalResult else "FAIL"))

    def writeResult2stdout(self, result):
        """
        最終結果のターミナルへの表示
        :param result:
        :return:
        """
        print("")
        finalResult = True
        for name, is_pass in result:
            finalResult = finalResult and is_pass
        print("##### {0} [{1}]".format(self.promptName, "OK" if finalResult else "FAIL"))
        for name, is_pass in result:
            s = "PASS" if is_pass else "FAIL"
            finalResult = finalResult and is_pass
            print("  [{0}]: {1}".format(s, name))

    def decorateHTML(self):
        return self.stlt.decorateHTML()



testStr="""
- "hostname": "CiscoRouter"
  "ipaddr": "192.168.153.20"
  "tests":
   - "name": "SW1 is vty server"
     "cmd": "show ip os nei"
     "include": 
       - "192.168.0.1"
       - "FULL"
     "notinclude": 
       - "192.168.0.2"
       - "2WAY"
- "hostname": "JUNOSRouter"
  "device_type": "juniper_junos"
  "ipaddr": "192.168.153.10"
  "tests":
   - "name": "ospf"
     "cmd": "show ospf neighbor"
     "include": 
       - "192.168.0.2"
       - "Full"
     "notinclude": 
       - "192.168.0.1"
       - "2WAY"
   - "name": "lldp"
     "cmd": "show lldp local-information | match ^ge"
     "include": 
       - "ge-0/0/1.0"
     "notinclude": 
       - "ge-0/0/0.0"
   - "name": "disable evil route"
     "cmd": "show route 6.6.6.6 | match 6.6.6.6"
     "notinclude":
       - "8.8.8.8"
       - "6.6.6.6"
       - "7.7.7.7"
       - "9.9.9.9"
"""


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    cors = []

    d = yaml.load(testStr)
    nodes = []
    is_pass = True

    for node in d:
        cors.append(CheckConfig(debug=True).test(node))
    futures = asyncio.gather(*cors)
    loop.run_until_complete(futures)
    nodes = futures.result()

    sd = SimpleTextLineTestDecorator()
    with open("test.html", mode='w') as f:
        f.write(sd.render(nodes))
