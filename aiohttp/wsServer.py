import asyncio
import aiohttp
from aiohttp import web
import json

bindPort = 1082

# グローバルで定義した接続中のwebsocketのリスト
ws_clients = list()


async def server_worker(waittime: int = 1, taskname: str = ""):
    """
    定期的にイベントを現在接続されているwebsocketに対してメッセージを送信するタスク
    :return:
    """
    print("server_worker start[{0}]".format(taskname))
    counter = 0
    while True:
        # waittimeごとにカウンタをインクリメント
        counter = counter + 1
        # 非同期にsleepする
        await asyncio.sleep(waittime)
        print("task[{0}/{1}]: send len={2} clients".format(taskname, str(counter), str(len(ws_clients))))
        # 全ての接続中のWebSocketに対して
        for ws in ws_clients:
            # 現在、自分の持っているカウンタ値をweb socketのpeer全員に通知
            await ws.send_str("task[{0}] count = {1}]".format(taskname, str(counter)))


# 通常のgetに対するレスポンス(デバッグ用)
async def web_hello(request: web.Request):
    args = dict()
    args["name"] = request.url.query.get("name", "somebody")
    return web.json_response(text=json.dumps(args))


async def web_connect(request: web.Request):
    """
    WebSocket接続の際のハンドラ
    :param request:
    :return:
    """
    # wsの初期化/準備
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    # socketの接続が完了したので、WebSocketのリストに入れる
    ws_clients.append(ws)

    # この場合のasync forはメッセージ入力が来るのを待つ
    # 今回の場合、Errorが発生するかCloseするまでloop
    async for msg in ws:
        # 通常のメッセージである場合
        if msg.type == aiohttp.WSMsgType.TEXT:
            # closeと入力された場合は切断を行う
            if msg.data == 'close':
                await ws.send_str("disconnect")
                await ws.close()
            else:
                # そうでないなら、クライアントに対して文字を反射する
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    # 例外による切断 あるいは closeを検知したのだからクライアントリストから抜く
    ws_clients.remove(ws)
    print('websocket connection closed')
    return ws

# HTTPd用のルーティング設定
routes = [
    web.get("/", web_hello),
    web.get("/connect", web_connect),
]

if __name__ == "__main__":
    # グローバルにループイベントを作成
    loop = asyncio.get_event_loop()

    # aiohttp.web.Applicationの実体化
    app = web.Application()
    app.add_routes(routes)
    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())

    site = web.TCPSite(runner, port=bindPort)

    # ループイベントにWebタスクを追加する
    cors = list()
    cors.append(site.start())
    cors.append(asyncio.ensure_future(server_worker(1, "1sec_task")))
    cors.append(asyncio.ensure_future(server_worker(3, "3sec_task")))
    res = loop.run_until_complete(asyncio.gather(*cors))

    # Unreach in this code!
    loop.run_forever()

