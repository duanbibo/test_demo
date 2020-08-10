import asyncio

async def a():
      print("协程执行中")
      await asyncio.sleep(2)
      print("sleep后")
      return  "协程执行完毕"

def hello_world(loop):
    print('Hello World')
    loop.stop()


loop = asyncio.get_event_loop()

task=loop.run_until_complete(a())

print(task)
# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
