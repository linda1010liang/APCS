#b682.同學早安
h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
sm1=60*h1+m1
sm2=60*h2+m2
s=sm2-sm1
h=s//60
m=s%60
if h<0:
    print(h+24,m)
else:
    print(h,m)
