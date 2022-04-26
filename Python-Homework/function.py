#1. 函数计算
# a. 求三个数之和。
def sum_m(x, y, z):
    return x+y+z

# b. 求三个数平均值。
def avg(x, y, z):
    return (x+y+z)/3

pi = 3.14
# 2. 创建一个有返回值的函数。
def fun(mode="sum", *args):
    result = 0
    if(mode=="sum"):
        for i in range(len(args)):
            result += args[i]
    elif(mode=="avg"):
        for i in range(len(args)):
            result += args[i]
        result = result / len(args)
    elif(mode=="circle"):
        global pi
        result = pi * args[0]
    return result

# 3. 创建一个共用全局变量的函数。
A = 7
def glob():
    global A
    print(A)

# 4. 创建一个位置参数的函数。
print( sum_m(1, 2, 3))

# 5. 创建一个关键字参数的函数。
print( avg(x=1, y=2, z=3))

# 6. 创建一个默认参数的函数。
def avg_2(x, y, z = 3):
    return (x+y+z)/3

# 7. 创建一个不定长参数的函数。
# a. 包裹位置传递。
def test_1(*args):
    print(args)

# b. 包裹关键字传递。
def test_2(**args):
    print(args)

glob()
print( avg_2(1, 2))
test_1(1, 2, 3)
test_2(a=1, b=2, c=3)

print(fun( 1, 2, 3,))
print(fun("sum", 1, 2, 3,))
print(fun("avg", 1, 2, 3 ))
print(fun("circle", 1))
