b=[]
for i in range(9):
    x=int(input())
    b.append(x)
print(max(b),b.index(max(b))+1)