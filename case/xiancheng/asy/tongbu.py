import  asyncio



loop=asyncio.get_event_loop()
loop.create_task()  #传入一个协程
asyncio.create_task()#传入一个协程
asyncio.ensure_future()  #传入一个 future，await 或者协程
asyncio.shield()  #传入一个协程future，await 或者协程，内部一个包装器调用ensure不会被取消

loop.run_in_executor(None) # 将协程放入执行器中执行
asyncio.run()#入口
