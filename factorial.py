'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2019-12-02 15:35:12
@LastEditors: Mar Ping
@LastEditTime: 2019-12-03 23:15:39
'''
# File: factorial.py
# Program compute the factorial(阶乘) of a number
# by: Mar Ping


def main():
    
    print()
    print("This program compute the factorial(阶乘) of a number")

    n = int(input("Please enter a whole number : "))

    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    print("The factorial of ",n,"is",fact)
    main()

main()
