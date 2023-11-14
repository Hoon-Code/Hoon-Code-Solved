num=int(input())
for i in range(1,num+1):
    a,b=map(int,input().split())
    print("Case #%s: %s + %s = %s" %(i, a, b, a+b))