'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2019-12-04 00:01:57
@LastEditors: Mar Ping
@LastEditTime: 2019-12-04 08:39:08
'''
# File: pizza.py
# Program calculation the price(价格) per square inch(每平方英寸) of pizza
# by: Mar Ping

import math

def main():

    print("This program calculation the price(价格) per square inch(每平方英寸) of pizza.",end="\n")

    r = float(input("Please enter the pizza's radius: "))
    unit = float(input("Please entre the price of this pizza: "))

    area = math.pi * r * r
    price = unit / area
    
    print("This pizza's price of per square inch is : ",price,end="\n")
    
    main()

main()
