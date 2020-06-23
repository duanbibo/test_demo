import unittest
from ddt import *
from .outconfig import  dataout
import xlrd



@ddt
class TestCount(unittest.TestCase):


    excel_path=os.path.dirname(__file__)+"case.xlsx"
    def read_excel(self,excel_path=excel_path):
          excel=xlrd.open_workbook(excel_path)
          sheet=excel.sheet_by_index(0)
          maxrows=sheet.nrows
          ldata=[]
          for i in range(maxrows):
                ldata.append(sheet.row_values(i))
          print(ldata)


    @data(*dataout)
    @unpack
    def test_bijiao(self,a,b):
      global c
      c=a-b
      assert (a>b)


    def test_dier(self,w):
          print(c)

          assert c >w





