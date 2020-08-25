import argparse

'''
使用这个库来解析命令行参数
'''

#创建参数解析对象
parse=argparse.ArgumentParser(description="传入一个数字")

#传入的位置参数
parse.add_argument('integers',help="传入一个数字")


#解析参数，返回一个字典
args=parse.parse_args()


#获取传入的参数,通过args的字典来获取参数对应的值
print(args.integers)