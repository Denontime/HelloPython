# File: futval.py
# A program to compute the value of an investment( 计算投资终值 本金+利息)
# by: Mar Ping
# principal(本金)     apr(利率)

def main():
    print()
    print("This program computes the value of an investment.")

    pri = eval(input("Enter your principal: "))
    apr = eval(input("Enter your apr: "))
    years = eval(input("How long do you investment?  "))

    for i in range(years):
        pri = pri * (1 + apr)

    print("The value of an investment is: ",pri)
    main()

main()
