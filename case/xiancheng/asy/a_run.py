import asyncio

async def x():
      print("hello")
      await  asyncio.sleep(3)
      print("执行")
loop=asyncio.get_event_loop()
asyncio.run(x())