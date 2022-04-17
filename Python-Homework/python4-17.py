# 1.计算字符串 "cd" 在 字符串 "abcd"中出现的位置。
str1='abcd'
print(str1.find('cd'))
#答案 2

# 2.字符串 "a,b,c,d" ，请用逗号分割字符串。
str2="a,b,c,d"
print(str2.split(',',4))
#答案 ['a', 'b', 'c', 'd']

# 3. "this is a book",请将字符串里的book替换成apple。
str3="this is a book"
print(str3.replace('book','apple'))
#答案 this is a apple

# 4. "this is a book", 请用程序判断该字符串是否以this开头。
str4="this is a book"
print(str4.startswith('this'))
# 答案 True

# 5.创建一个空列表，命名为names，往里面添加 Lihua、Rain、Jack、Xiuxiu、Peiqi和Black元素。
names=[]
names.extend(['Lihua','Rain','Jack','Xiuxiu','Peiqi','Black'])
print(names)
# ['Lihua', 'Rain', 'Jack', 'Xiuxiu', 'Peiqi', 'Black']

# a.往(1)中的names列表里Black前面插入一个Blue。
names.insert(5,'Blue')
print(names)
#答案 ['Lihua', 'Rain', 'Jack', 'Xiuxiu', 'Peiqi', 'Blue', 'Black']

# b.返回names列表中Peiqi的索引值（下标）。
print(names.index('Peiqi'))
# 答案 4
# c.取出names列表中索引2-10的元素，步长为2。
print(names[2:10:2])
#答案 ['Jack', 'Peiqi', 'Black']
# d.循环names列表，打印每个元素的索引值和元素。
for i in names :
    print(i)
    print(names.index(i))
    #答案

# Lihua 0 Rain 1 Jack 2 Xiuxiu 3 Peiqi 4 Blue 5 Black 6
# 10．tuple1=('123','abc','你好')
tuple1=('123','abc','你好')
# a. len()计算元组元素个数
print(len(tuple1))
#答案 3
# b. max()返回元组中元素最大值
print(max(tuple1))
#答案 你好
# c. min()返回元组中元素最小值
print(min(tuple1))
#答案 123
# d. tuple()将列表转换为元组
list1=list(tuple1)
print(list1)
#答案 ['123', 'abc', '你好']
# 11. dict = {'k1':'v1','k2':'v2','k3':[11,22,33]}
dict = {'k1':'v1','k2':'v2','k3':[11,22,33]}
# a.请循环出所有的key
for key in dict.keys() :
    print(key)
#答案 k1 k2 k3
# b. 请循环出所有的value
for value in dict.values() :
    print(value)
#答案 v1 v2 [11, 22, 33]

# c.请循环出所有的元素
for i in dict.items():
    print(i)
   # 答案 ('k1', 'v1') ('k2', 'v2') ('k3', [11, 22, 33])
# d.请分别循环出所有的元素
for key,value in dict.items():
    print(f'{key} {value}')
    #答案 k1 v1  k2 v2  k3 [11, 22, 33]
# e.请在字典中任意添加一个键值对,’k4’:’v4’输出后添加到字典
dict['k4']='v4'
print(dict)
#答案 {'k1': 'v1', 'k2': 'v2', 'k3': [11, 22, 33], 'k4': 'v4'}
# 12.  a = {'Nacy', 'Lily', 'Rita'}
# b ={'Nacy', 'Zara', 'John'}
a = {'Nacy', 'Lily', 'Rita'}
b ={'Nacy', 'Zara', 'John'}
#print(a|b)

#  答案{'Nacy', 'Rita', 'Lily', 'John', 'Zara'}
#print(a&b)

#  答案{'Nacy'}
#print(a-b)

# 答案{'Rita', 'Lily'}
#print(a^b)

# 答案{'Lily', 'Rita', 'John', 'Zara'}
# 13.
g1 = {'wcj','good','lucky','sunny'}
g2 = {'cloudy','love','wcj','miss'}
# a.使用update函数将两个集合合并为一个集合
g1.update(g2)
print(g1)
#答案 {'lucky', 'cloudy', 'miss', 'wcj', 'love', 'good', 'sunny'}
# b.清空g1集合
g1.clear()
print(g1)
# 答案 set()
# c.给g2集合添加一个元素
g2.add('jialiang')
print(g2)
# 答案{'miss', 'wcj', 'love', 'jialiang', 'cloudy'}