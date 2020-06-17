
import xlrd
import os







def read_excel(excel_path):
      excel = xlrd.open_workbook(excel_path)
      sheet = excel.sheet_by_index(0)
      maxrows = sheet.nrows
      maxcols = sheet.ncols
      ldata = []
      for i in range(maxrows):
            if i==1:
                  continue
            value=sheet.row_values(i)
            ldata.append(value)


      print(ldata)
      return ldata
one=read_excel(os.path.dirname(__file__) + "/东方医院患者列表.xlsx")


# read only 第几列
def read_excel_col(excel_path,col):
      excel = xlrd.open_workbook(excel_path)
      sheet = excel.sheet_by_index(0)
      maxrows = sheet.nrows
      # maxcols = sheet.ncols
      ldata = []
      for i in range(maxrows):
            if i == 1:
                  continue
            valuecol = sheet.cell(i,col).value
            list1=[]
            #利用ddt做数据源时，每一个组数据必须为可迭代对象。所以用list或者dict嵌套才行
            list1.append(int(valuecol))
            ldata.append(list1)

      print(ldata)
      return ldata
#lie=read_excel_col(os.path.dirname(__file__) + "/东方医院患者列表.xlsx",1)



#读取excel全部数据
def read_excel_all(excel_path):
      excel = xlrd.open_workbook(excel_path)
      sheet = excel.sheet_by_index(0)
      maxrows = sheet.nrows
      # maxcols = sheet.ncols
      ldata = []
      for i in range(maxrows):
            if i == 1:
                  continue
            valuecol = sheet.row_values(i)
            valuecol[0]=str(valuecol[0])
            valuecol[3] = int(valuecol[3])
            ldata.append(valuecol)
      print(ldata)
      return ldata
#all=read_excel_all(os.path.dirname(__file__) + "/东方医院患者列表.xlsx")


print(all)