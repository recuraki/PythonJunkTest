import asyncio
from aiohttp import web
import json
import aiohttp_jinja2
import datetime
from Logs import Log
import jinja2
import lib
from checkConfig import checkConfig, checkConfigTests
from SimpleTextLineTestDecorator import SimpleTextLineTestDecorator
from checkConfigResult import checkConfigResult, checkConfigResultData
from datetime import datetime

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

bindHost = "0.0.0.0"
bindPort = 8081


async def web_top(request: web.Request):
    return aiohttp_jinja2.render_template("templ/top.html", request, {})


async def web_hello(request: web.Request):
    """
    テスト用のダミー
    :param request:
    :return:
    """
    args = dict()
    args["application"] = "DashBoard"
    args["name"] = request.url.query.get("name", "somebody")
    return web.json_response(text=json.dumps(args))

async def web_log(request: web.Request):
    args = dict()
    args["logs"] = logs.get_logs()
    return aiohttp_jinja2.render_template("templ/status.templ", request, args)


async def web_reset(request: web.Request):
    # TODO 現状単なるstubです。実装されていません。
    args = dict()
    args["logs"] = logs.get_logs()
    return aiohttp_jinja2.render_template("templ/status.templ", request, args)


async def web_list_scenarios(request: web.Request):
    # id: シナリオ名を一覧する
    args = dict()
    args["data"] = testall.list_scenario()
    return web.json_response(text=json.dumps(args))


async def web_detail_scenarios(request: web.Request):
    # idで指定されたシナリオを表示する
    id = request.match_info["id"]
    if not id:
        return web.Response(text="Resource not found", status=404)
    args: dict = testall.test_by_id(id)
    return web.json_response(text=json.dumps(args, indent=2))

async def web_run_by_id(request: web.Request):
    """
    idで指定されたテストを実行する。
    テストに含まれるnode単位ごとにcheckConfigのタスクを作り、asyncで終了を待ちます。(asyncio.wait)
    結果はresultに出力されます。
    :param request:
    :return:
    """
    id = request.match_info["id"]
    if not id:
        return web.Response(text="plz input id", status=404)

    timeStart:datetime = datetime.now()

    tests = testall.test_by_id(id)
    cors_test = []
    for node in tests:
        cors_test.append(checkConfig(debug=True, timeout=2.5).test(node))
    res_cors, pending = await asyncio.wait(cors_test)
    res_cors = list(map(lambda x: x.result(), res_cors))

    timeEnd:datetime = datetime.now()

    resultall.push(id, res_cors, timeStart, timeEnd)

    sd = SimpleTextLineTestDecorator()
    html = sd.render(res_cors)
    return web.Response(text=html, content_type="text/html")

async def web_results(request: web.Request):
    id = request.match_info["id"]
    rev = request.match_info["rev"]
    if not id or not rev:
        return web.Response(text="Resource not found", status=404)

    res = resultall.getLastResultById(id)

    sd = SimpleTextLineTestDecorator()
    html = sd.render(res)
    return web.Response(text=html, content_type="text/html")

async def web_results_by_id(request: web.Request):
    id = request.match_info["id"]
    if not id:
        return web.Response(text="Resource not found", status=404)

    res = resultall.getLastResultById(id)
    if not res:
        return web.Response(text="Resource not found", status=404)

    sd = SimpleTextLineTestDecorator()
    html = sd.render(res)
    return web.Response(text=html, content_type="text/html")


routes = [
    web.get   ("/", web_top),
    web.get("/logs", web_log),
    web.get("/reset", web_reset),
    web.get("/scenarios", web_list_scenarios),
    web.get("/scenarios/{id}", web_detail_scenarios),
    web.get("/run/id/{id}", web_run_by_id),
    web.get("/results/{id}", web_results_by_id),
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

logs = Log()
logs.write_log("init")


testall = checkConfigTests()
def initScenario():
    # TODO scenarioは可変にする
    scenarioPath = "./scenario"
    scenarios = lib.listScenarioname(scenarioPath)
    for no, name, p in scenarios:
        test = lib.loadYamlFromDir(p)
        testall.push(str(no), name, lib.loadYamlFromDir(p))


resultall = checkConfigResult()


if __name__ == "__main__":
    initScenario()
    # グローバルなループイベントの作成
    loop = asyncio.get_event_loop()

    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, port=bindPort)

    # ループイベントにWebタスクを追加する
    cors = []
    cors.append(site.start())
    res = loop.run_until_complete(asyncio.gather(*cors))

    # ループの開始
    print(">> Server Process Start [{0};{1}]".format(bindHost, bindPort))


    loop.run_forever()




