#d069. 格瑞哥里的煩惱 (t 行版)
t=int(input())
for i in range(t):
    y=int(input())
    if y%400==0 or y%4==0 and y%100!=0:
        print("a leap year")
    else:
        print("a normal year")
