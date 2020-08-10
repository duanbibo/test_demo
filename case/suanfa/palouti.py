#encoidng=utf-8


'''
题目： 有台阶100个，第一种每步走1个台阶，第二种每步走2个台阶，第三种每步走3个台阶，请问一共有多少种走法
'''
''''''

l=[]
for one  in range(1,101):
      for two in range(1,101):
            for three in range(1,101):
                  if (one+two*2+three*3)==100:
                       l.append([one,two,three])

'''
三个for循环可以继续优化，第一个for循环的区间是0-100，
第二个for循环根据总数100个台阶，每步2台阶，肯定小于51
第三个for循环根据总数100个台阶，每步3台阶，肯定小于34
'''
print(l)
print(len(l))


