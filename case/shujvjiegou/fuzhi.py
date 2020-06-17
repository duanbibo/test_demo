
list1=[2,3,45]

print(max(list1))

tuple1 = ('001', '张三',18,'man', '138383838438')
id, name, age,sex ,tel= tuple1
print(id)  #001
print(name) #张三
print(age)   #18
print(sex)   #man
print(tel)    #138383838438
id,*info=tuple1
print(info)