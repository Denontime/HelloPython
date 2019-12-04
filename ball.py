'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2019-12-02 14:02:35
@LastEditors: Mar Ping
@LastEditTime: 2019-12-03 23:52:42
'''
# File: ball.py
# A program to calculate the volume(体积) and area(面积) of the ball
# by: Mar Ping

import math

def main():

    print()
    print("This program calculate the volume(体积) and area(面积) of the ball")
    
    r = float(input("Please enter the radius(半径) of the ball : "))
    
    vol = 4 / 3 * math.pi * r * r * r
    area = 4 * math.pi * r * r

    print("The volume of the ball is : ",vol)
    print("The area of the ball is : ", area)
    
    main()
    
main()