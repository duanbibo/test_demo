

'''

这个脚本统计请求次数，每次请求后输出的log信息，都+1，在执行脚本的控制台输出
'''
import mitmproxy.http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)





