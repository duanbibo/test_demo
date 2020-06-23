
import HTMLTestRunner
import unittest

case_path = "C:/Users/87842/PycharmProjects/test_demo/case/test_un"
discover = unittest.defaultTestLoader.discover(case_path,pattern="test_*.py",top_level_dir=None)

#执行用例生成报告
runner = unittest.TextTestRunner()
reportpath = "C:/Users/87842/PycharmProjects/test_demo/case/test_un/report/result.html"



rp=open(reportpath,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=rp, title=u'测试报告', description=u'用例执行情况：')
runner.run(discover)
rp.close()

