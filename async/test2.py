"""
終わらないイベントループ内の、あるコルーチン内で、
他の複数のコルーチンをcallして、その結果を表示するサンプル。
基本的には、
res, pending = await asyncio.wait([cors...])
でcallできる。
この際、resはsetで帰ってくるため、resultを得るには
    for i in res:
        print(name + ": " + i.result())
などで、Task(Finished).result()をcallする。

加えて、asyncio.waitの戻り値resは順不同であるため、
戻り値を識別できるコードは入れるべきである。(あるいは、順が必要なら、ソート用にキーを返すべきである)

これに対して、  asyncio.ensure_future(

wake[b]
wake[a]
loop
done[b]
wait_and_call: call coroutine
loop
wake[cor_a]
wake[cor_b]
done[a]
loop
done[cor_b]
loop
loop
done[cor_a]
loop
wait_and_call: awaited coroutine
wait_and_call: coroutine:cor_b
wait_and_call: coroutine:cor_a
loop

"""
import asyncio
import time
from pprint import pprint

async def s(s, name=""):
    print("wake[" + name + "]")
    await asyncio.sleep(s)
    print("done[" + name + "]")
    return "sle:" + name

async def wait_and_call(s, name=""):
    await asyncio.sleep(s)
    print(name + ": call coroutine")
    res, pending = await asyncio.wait([coroutine(2, "cor_a"), coroutine(1, "cor_b"), ])
    print(name + ": awaited coroutine")
    for i in res:
        print(name + ": " + i.result())
    return name


async def coroutine(s, name=""):
    print("wake[" + name + "]")
    await asyncio.sleep(s)
    print("done[" + name + "]")
    return "coroutine:" + name


async def zuttoloop(s, name=""):
    while True:
        print(name)
        await asyncio.sleep(s)


if __name__ == "__main__":
    cors = []
    cors.append(s(1, "a"))
    cors.append(s(0.25, "b"))
    cors.append(wait_and_call(0.5, "wait_and_call"))
    cors.append(zuttoloop(0.5, "loop"))
    loop = asyncio.get_event_loop()
    futures =asyncio.gather(*cors)
    res = loop.run_until_complete(futures)
    print(res)