#b186. 97七區資訊學科1(改編)
while 1:
    try:
        a,b,c=map(int,input().split())
        a1=a//10
        c1=c//2
        if a1<c1:
            b+=a1
            print("{} 個餅乾，{} 盒巧克力，{} 個蛋糕。".format(a,b,c))
        else:
            b+=c1
            print("{} 個餅乾，{} 盒巧克力，{} 個蛋糕。".format(a,b,c))
    except:
        break
