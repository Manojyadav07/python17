a1,b1=map(int,input().split())
for i in range(a1+1,b1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=" ")
