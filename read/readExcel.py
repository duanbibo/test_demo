import  xlrd
import os

def read_exl(exl_name=None):

      # 获取当前脚本所在文件夹路径将    当前文件夹     ..
      curPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
      # 获取exl文件路径
      exl_Path = os.path.join(curPath, "resource/" + exl_name)


      #利用xlrd库的open_workbook方法打开exl文件，返回一个book集合
      data=xlrd.open_workbook(exl_Path)
      print(type(data))

      #可以利用sheet页的名称和下标进行获取 sheet页
      sheet=data.sheets()[0]
      print(type(sheet))

      #最大行数
      row_length=sheet.nrows
      #最大列数
      col_length=sheet.ncols



      #打印这一行的全部内容
      sheet.row(0)
      #打印这一列的全部数据
      sheet.col(0)
      # 打印第2行第5个 单元格
      a = sheet.cell(1, 4)
      #打印一行内容，第一个值为行数，第二个值为开始位置，第三个值为结束位置
      v=sheet.row_values(0,2,6)
      print(v,"-----------")




      #获取单元格时，从0.0开始的。
      return  row_length,a,

print(read_exl(exl_name="case.xlsx"))

