# File: chaos.py
# A simple program illustrating chaotic behavio.
# by: Mar Ping

def main():
    print()
    print("My frist python progam! It show us what is chaos.")
    x = eval(input("Enter 2 number between 0 and 1: "))
    y = x
    z = x
    a = eval(input("How many numbers should I print? "))
    print("________________________________________________")
    for i in range (a):
        x = 3.9 * x *(1 - x)
        y = 3.9 * (y - y * y)
        z = 3.9 * z - 3.9 * z * z
        print(x,"         ",y,"         ",z)
    main()

main()
