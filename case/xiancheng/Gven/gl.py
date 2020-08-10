from greenlet import greenlet
def _test1():
    print (12)
    gr2.switch()
    print (34)

def _test2():
    print (56)
    gr1.switch()
    print (78)

gr1 = greenlet(_test1)
gr2 = greenlet(_test2)
gr2.switch()