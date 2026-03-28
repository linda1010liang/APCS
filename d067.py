#d067. 格瑞哥里的煩惱 (1 行版)
y=int(input())
if y%400==0 or y%4==0 and y%100!=0:
    print("a leap year")
else:
    print("a normal year")
