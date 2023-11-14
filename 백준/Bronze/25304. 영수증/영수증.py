a=int(input())
b=int(input())
sum=0
for i in range(b):
    x,y=map(int,input().split())
    sum+=x*y
if sum == a:
    print('Yes')
else:
    print('No')