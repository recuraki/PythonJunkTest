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
    args = dict()
    args["application"] = "DashBoard"
    args["name"] = request.url.query.get("name", "somebody")
    return web.json_response(text=json.dumps(args))

async def web_log(request: web.Request):
    args = dict()
    args["logs"] = logs.get_logs()
    return aiohttp_jinja2.render_template("templ/status.templ", request, args)


async def web_reset(request: web.Request):
    args = dict()
    args["logs"] = logs.get_logs()
    return aiohttp_jinja2.render_template("templ/status.templ", request, args)


async def web_list_scenarios(request: web.Request):
    args = dict()
    args["application"] = "DashBoard"
    args["name"] = request.url.query.get("name", "sce")
    return web.json_response(text=json.dumps(args))


async def web_detail_scenarios(request: web.Request):
    id = request.match_info["id"]
    if not id:
        return web.Response(text="Resource not found", status=404)

    args = dict()
    args["application"] = "DashBoard"
    args["name"] = request.url.query.get("name", str(id))
    return web.json_response(text=json.dumps(args))


routes = [
    web.get   ("/", web_top),
    web.get("/logs", web_log),
    web.get("/reset", web_reset),
    web.get("/scenarios", web_list_scenarios),
    web.get("/scenarios/{id}", web_detail_scenarios),
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

if __name__ == "__main__":
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




