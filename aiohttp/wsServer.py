
import asyncio
import aiohttp
from aiohttp import web
import json
import aiohttp_jinja2


bindHost = "0.0.0.0"
bindPort = 1080


# グローバルで定義した接続中のwebsocketのリスト
ws_clients = list()


async def server_worker(waittime: int = 1, taskname: str = ""):
    """
    定期的にイベントを現在接続されているwebsocketに対してメッセージを送信するタスク
    :return:
    """
    print("begin server_worker")
    counter = 0
    while True:
        counter = counter + 1
        # 非同期にsleepする
        await asyncio.sleep(waittime)
        print("task[{0}/{1}]: send len={2} clients".format(taskname, str(counter), str(len(ws_clients))))
        for ws in ws_clients:
            # 非同期にwebsocketに対してメッセージを送信する
            await ws.send_str("task[{0}] count = {1}]".format(taskname, str(counter)))


# 通常のgetに対するレスポンス
async def web_hello(request: web.Request):
    args = dict()
    args["name"] = request.url.query.get("name", "somebody")
    return web.json_response(text=json.dumps(args))

# websocket
async def web_connect(request: web.Request):
    # wsの初期化
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    ws_clients.append(ws)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.send_str("disconnect")
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    ws_clients.remove(ws)
    print('websocket connection closed')

    return ws

# HTTPd用のルーティング設定
routes = [
    web.get   ("/", web_hello),
    web.get("/connect", web_connect),

]

app = web.Application()
aiohttp_jinja2.setup(app)
app.add_routes(routes)

if __name__ == "__main__":
    # グローバルなループイベントの作成
    loop = asyncio.get_event_loop()

    # NEWebの実体化
    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, port=bindPort)

    # ループイベントにWebタスクを追加する
    cors = []

    cors.append(site.start())

    res = loop.run_until_complete(asyncio.gather(*cors))


    # ループの開始
    print(">> NEE Start [{0};{1}]".format(bindHost, bindPort))

    asyncio.ensure_future(server_worker(1, "1sec_task"))
    asyncio.ensure_future(server_worker(3, "3sec_task"))

    loop.run_forever()

