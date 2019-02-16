import asyncio
import aiohttp
from aiohttp import web
import json
import aiohttp_jinja2
from typing import List
from pprint import pprint
import datetime
from Logs import Log
import jinja2
import aioconsole


from Maze import Maze
from Maze import Solver

bindHost = "0.0.0.0"
bindPort = 8081

ws_clients = list()

breakType = (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.ERROR)

async def web_hello(request: web.Request):
    args = dict()
    args["application"] = "DashBoard"
    args["name"] = request.url.query.get("name", "somebody")
    return web.json_response(text=json.dumps(args))

async def sendMsg(wsd, dat: dict, res: dict, debug = False):
    """

    :param wsd: websocket clientのオブジェクト
    :param dat: clientから送られてきたデータ
    :param res: 返信すべきデータ
    :return:
    """
    # 成功応答の作成
    res["result"] = "ok"
    res["reason"] = ""
    res["nodeName"] = ""
    res["msgId"] = ""
    # 反射
    if "nodeName" in dat:
        res["nodeName"] = dat["nodeName"]
    if "msgId" in dat:
        res["msgId"] = dat["msgId"]
    if debug:
        pprint(res)
    await wsd.send_str(json.dumps(res, indent=4))


async def ws_init(ws, dat: dict) -> None:
    r = {}
    r["method"] = "responseoInit"
    r["map"] = m.map
    r["posStart"] = m.posStart
    r["posGoal"] = m.posGoal
    r["searchCells"] = s.searchCells
    r["discardCells"] = s.discardCells
    logs.write_log("[came] init")
    await sendMsg(ws, dat, r)

async def ws_next(ws, dat: dict) -> None:
    r = {}
    r["method"] = "responseoNext"
    logs.write_log("[came] next")
    await sendMsg(ws, dat, r)

finish = False
async def solveUpdate() -> None:
    global finish
    if finish:
        return
    # s.solve()
    r = {}
    r["method"] = "update"
    r["searchCells"], finish = next(n)
    logs.write_log("[send] update")
    for wsc in ws_clients:
        await sendMsg(wsc, {}, r)


async def web_connect(request: web.Request):
    # wsの初期化
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    print('websocket connection came')
    ws_clients.append(ws)

    async for msg in ws:
        print("recv:{0}".format(msg.data.replace('\n','')))
        if msg.type in breakType:
            print('ws connection closed with exception %s' % ws.exception())

        try:
            dat = json.loads(msg.data)
        except json.decoder.JSONDecodeError:
            print("cannot decode by json {0}".format(msg.data))
            continue

        if "method" not in dat:
            print("[error] no method element")
            continue

        if dat["method"] == "init":
            await ws_init(ws, dat)

        if dat["method"] == "ping":
            await ws.send_str('{"method": "pong"}')

        if dat["method"] == "next":
            await ws_next(ws, dat)

    ws_clients.remove(ws)
    print('websocket connection closed')

    return ws

async def web_log(request: web.Request):
    args = dict()
    args["logs"] = logs.get_logs()
    return aiohttp_jinja2.render_template("templ/status.templ", request, args)

routes = [
    web.get   ("/", web_hello),
    web.get("/logs", web_log),
    web.get("/connect", web_connect),
    web.static("/static", "./static"),
]


# Jinja2 Filter: ログの整形用
def j2_filter_date(date: datetime):
    return date.strftime('%H:%M:%S.%f')

j2_filters = dict()
j2_filters["strftime"] = j2_filter_date

app = web.Application()
app["static_root_url"] = "/static"
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("./"), filters=j2_filters)
app.add_routes(routes)

class Cli(object):
    def __init__(self, loop):
        self.loop = loop

    async def read(self):
        while True:
            s = sys.stdin.readline().strip()
            if s == "exit":
                return
            yield s

    async def task(self):
        print("task")
        stdin, stdout = await aioconsole.get_standard_streams()
        async for s in stdin:
            s = s.decode()
            s = s.strip()
            print("async for [{0}]".format(s))
            if s == "":
                await solveUpdate()


logs = Log()
logs.write_log("init")

m = Maze()
s = Solver(m)
n = s.solve()

if __name__ == "__main__":
    # グローバルなループイベントの作成
    loop = asyncio.get_event_loop()

    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, port=bindPort)

    c = Cli(loop)

    # ループイベントにWebタスクを追加する
    cors = []
    cors.append(site.start())
    res = loop.run_until_complete(asyncio.gather(*cors))

    # ループの開始
    print(">> Server Process Start [{0};{1}]".format(bindHost, bindPort))

    asyncio.ensure_future(c.task())

    loop.run_forever()




