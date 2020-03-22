a=int(input())
c=1
while(a!=0):
    l=list(map(int,input().split()))
    n=l[0]
    b=l[1]
    h=0
    aa=list(map(int,input().split()))
    aa.sort()
    for i in range(len(aa)):
        if(aa[i]<=b):
            h=h+1
            b=b-aa[i]
        else:
            break
   
    a-=1
    print("Case #"+str(c)+":",h )
    c+=1
