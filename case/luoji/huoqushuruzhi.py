import time


'''
 需求：1.让用户输入金额    
                   输入金额，需要做限制 类型和值,
                   通过 while true实现不正确输入时，循环执行提示输入正确金额和接收输入的金额
                   
       2.选择购买的商品加入购物车
              利用字典进行展示商品的 名称和价格 {'goods1':price1,'goods2':price2}
              字典接收 需要购买的    {'goods1':count2,'goods1':count2}
              
       3.选择完毕后用户输入N结算 Q退出
               在结算和退出进行输入值时，为了更友好进行大小写不区分。
               结算时,组合成一个新的字典  {'goods1':prices,'goods2':prices}
                prices 的值为 同一个键的字典1的值*字典2的值
                
                将字典内所有的values值进行求和，即为本次结算所有商品的价格。
             
       4.结算时，超过金额提示‘余额不足’
           结算时，总金额与首次输入金额做比较。
           结算时提示余额不足，进行利用需求1的函数，进行复用继续充值。
            充值完毕后，金额累加计算，如果还不足。继续进行死循环判断。
            结算完毕后，进行充值总金额与支付总金额差额计算，求剩余金额。
            
 注：所有用户的输入的，都要套个死循环来验证输入的争取性。      
       
'''
def gouwu():
      dictgoods = {'1.机器猫': 20, '2.变形金刚': 10, '3.葫芦娃': 130}
      buy={}
      paymoney={}
      while True:
         jine=input("请输入存钱金额:")
         if jine.isdigit() and 0< int(jine):
            print("存钱成功，存入%s元" % jine)
            break
         else:
             print("存入金额必须大于零，请重新输入")

      print("以下为本商店出售的商品")
      for key,value in dictgoods.items():
            print('{key}:{value}'.format(key=key,value=value))
      time.sleep(1)
      while True:
        chose = input("请选择想要购买的商品添加购物车:")
        if chose==str(1):
            print("选择完毕后，确认是否进行结算")
            print("N:结算          Q:退出")
            price=dictgoods.get('1.机器猫')
            break
        elif chose==str(2):
            print("选择完毕后，确认是否进行结算")
            print("N:结算          Q:退出")
            price=dictgoods.get('2.变形金刚')
            break
        elif chose==str(3):
            print("选择完毕后，确认是否进行结算")
            print("N:结算          Q:退出")
            price=dictgoods.get('3.葫芦娃')
            break
        else:
            print("请选择正确的商品")

      while True:
        enter = input()
        if str(enter)=="N"or str(enter)=="n":
            print("本次付款金额%s元"  %price)
            if  int(jine)< int(price):
                  print("卡内余额不足，请充值")
                  while True:
                        jine2 = input("请输入存钱金额")
                        if jine.isdigit() and 0 < int(jine):
                              print("充钱成功，存入%s元" % jine2)
                              break
                        else:
                              print("存入金额必须大于零，请重新输入")
                  heji=int(jine)+int(jine2)
                  if heji >int (price):
                        yue=int(heji)-int(price)
                        print("支付成功，卡内余额%d" %yue)
                        print("欢迎下次光临")
            else:
                  yue=int(jine)-int(price)
                  print("支付成功，卡内余额%d"%yue)
                  print("欢迎下次光临")
            break
        elif str(enter)=="Q"or str(enter)=="q":
            print("程序已退出")
            break
        else:
           print("输入有误，请重新输入")



a=gouwu()
a




