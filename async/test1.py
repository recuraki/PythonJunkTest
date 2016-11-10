#!/usr/bin/python3.5

#If your ubuntu don't have python35 pkg, 
# sudo add-apt-repository ppa:fkrull/deadsnakes
# sudo apt-get update
# sudo apt-get install python3.5

import asyncio
import time

async def s(s):
    #await asyncio.sleep(s)
    await time.sleep(s)

async def wait():
    return await asyncio.wait([s(3), s(2)])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait())
