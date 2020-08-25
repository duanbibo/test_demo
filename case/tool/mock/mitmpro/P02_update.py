import mitmproxy.http
from mitmproxy import ctx, http


class Joker:

      #请求处理：替换请求关键词
      def request(self, flow: mitmproxy.http.HTTPFlow):
            if flow.request.host != "www.baidu.com" or not flow.request.path.startswith("/s"):
                  return

            if "wd" not in flow.request.query.keys():
                  ctx.log.warn("can not get search word from %s" % flow.request.pretty_url)
                  return
            ctx.log.info("catch search word: %s" % flow.request.query.get("wd"))
            #ctx.log.info(flow.request.content)
            flow.request.query.set_all("wd", ["360搜索"])

      #返回结果处理：修改设置文本内容
      # def response(self, flow: mitmproxy.http.HTTPFlow):
      #       if flow.request.host != "www.so.com":
      #             return
      #
      #       text = flow.response.get_text()
      #       ctx.log.info(flow.response.content)
      #       ctx.log.info("content===================================")
      #       text = text.replace("搜索", "请使用谷歌")
      #       flow.response.set_text(text)

      def response(self, flow: mitmproxy.http.HTTPFlow):
            #ctx.log.info(flow.request.path,"path")
            #ctx.log.info(flow.request.url,"url")

            for k ,v in             flow.request.query.items():
                  ctx.log.info(k)



            #ctx.log.info() #获取查询的结果是一个字典，也需要特殊处理
            ctx.log.info(flow.response.get_text())  # 获取响应文本str
            #ctx.log.info(flow.response.get_content)  #获取返回为内容json
            if not flow.request.url.startswith("y"):
                  return


            ctx.log.info("content===================================")


      #请求网址响应码处理
      def http_connect(self, flow: mitmproxy.http.HTTPFlow):
            if flow.request.host == "www.qq.com":
                  ctx.log.info("腾讯网404")
                  flow.response = http.HTTPResponse.make(404)


