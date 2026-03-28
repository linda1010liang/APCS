#b572. 忘了東西的傑克
a=int(input())
for i in range(a):
    t=list(map(int,input().split()))
    m1=t[0]*60+t[1]
    m2=t[2]*60+t[3]
    m=t[4]
    if m1+m>m2:
        print("No")
    else:
        print("Yes")
