import asyncio
import functools


'''
这个比较复杂：涉及到传参函数传参。

'''

def callback(future, n):
      print('{}: future done: {}'.format(n, future.result()))


async def register_callbacks(all_done):
      ''' 这里用到冻结参数，'''
      print('注册callback到future对象')
      all_done.add_done_callback(functools.partial(callback, n=1))
      all_done.add_done_callback(functools.partial(callback, n=2))


async def main(all_done):

      await register_callbacks(all_done)

      print('设置future的结果')
      all_done.set_result('the result')


if __name__ == '__main__':

      '''' 
      核心是这块，通过在main函数执行块中注册一个变量形参future对象，直接传给异步的函数当其中一个参数。
      
      1. 进入main异步函数内，先执行需要调用异步的函数，这个future对象当做形参继续调用一个异步函数，
      2.在异步函数内，获取这个future对象，调用future对象的回调方法，通过冻结参数。传入方法名和实参
      3.进入回调函数内执行具体的内容。
      '''
      loop = asyncio.get_event_loop()
      try:
            all_done = asyncio.Future()
            loop.run_until_complete(main(all_done))
      finally:
            loop.close()