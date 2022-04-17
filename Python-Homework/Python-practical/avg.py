# File: avg.py
# A simple program to average two scores
# by: Mar Ping

def main():
    print()
    print("This program computes the average of two scores.")

    score1,score2 = eval(input("Enter two soresseparated by a comma: "))
    average = (score1 + score2) / 2

    print("The average of the scores is: ",average)
    main()

main()
