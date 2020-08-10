from multiprocessing import  Process,Pipe

'''
使用管道 进行多进程通信：类似于电话线，一个人在这头，一人在那头
'''

def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child2'])
    print("from parent:",conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # 名字自定义
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints [42, None, 'hello from child']
    print(parent_conn.recv())  # prints [42, None, 'hello from child2']
    parent_conn.send("[42, None, 'hello']") # prints "[42, None, 'hello']"
    p.join()