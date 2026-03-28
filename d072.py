#d072. 格瑞哥里的煩惱 (Case 版)
n=int(input())
for i in range(n):
    n=int(input())
    if n%400==0 or n%4==0 and n%100!=0:
        print("Case {}: a leap year".format(i+1))
    else:
        print("Case {}: a normal year".format(i+1))
