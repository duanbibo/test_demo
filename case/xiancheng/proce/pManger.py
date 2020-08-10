from multiprocessing import Process,Manager
import os


'''
通过Queue和Piepe只实现了数据的传递，没有实现数据的共享

'''


def f(dict1,list1):
    dict1[os.getpid()] = os.getpid()  # 往字典里放当前PID
    list1.append(os.getpid())  # 往列表里放当前PID
    print(list1)

if __name__ == "__main__":

    with Manager() as manager:
        d = manager.dict()  # 生成一个字典，可在多个进程间共享和传递
        l = manager.list(range(5)) #生成一个列表，可在多个进程间共享和传递
        p_list = []  # 存进程列表
        for i in range(10):
            p = Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)
        for res in p_list:  # 等待结果
            res.join()
        print('\n%s' %d)