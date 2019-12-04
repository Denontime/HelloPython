# File: avgs.py
# A simple program to average some scores
# by: Mar Ping

def main():
    print()
    print("This program computes the average of some scores.")

    a = eval(input("How many scores need average? "))
    score = 0
    
    for i in range(a):
        score1 = eval(input("Enter score need average: "))
        score = score + score1

    average = score / a
    
    print("The average of this scores is: ",average)
    main()

main()
