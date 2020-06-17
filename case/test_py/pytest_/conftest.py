# coding:utf-8
import pytest
import requests



key={'q':'长十郎'}

@pytest.fixture(scope="class")
def login():
      url="http://www.baidu.com"
      data=key
      post(url, data)

      yield       # 相当于teardown的作用，适用于每个scope后面
      print("over")

def post(url,data):
      r= requests.get(url=url, data=data)
      print(r.status_code)
      print(r.text)

      return  r.status_code



