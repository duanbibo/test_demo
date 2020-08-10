from gevent import monkey; monkey.patch_all()
import gevent


def f(n):
    for i in range(n):
        print( gevent.getcurrent(), i)

g1 = gevent.spawn(f, 5)  #创建一个协程
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()


#可以看到，3个greenlet是依次运行而不是交替运行。
#要让greenlet交替运行，可以通过gevent.sleep()交出控制权：