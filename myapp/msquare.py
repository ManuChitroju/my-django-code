def square(num):
    L=[[0 for x in range(num)] for y in range(num)]
    x=0
    y=int(num/2)
    L[x][y]=1
    n=2
    for i in range(1,num*num):
        if ((x==0) & (y==num-1)):
            x+=1
            L[x][y]=n
        else:
            if x==0:
                x=num-1
            else:
                x-=1
            if y==num-1:
                y=0
            else:
                y+=1
            if  L[x][y]==0:
                L[x][y]=n
            else:
                x+=2
                y-=1
                L[x][y]=n;
        n+=1
    return(L)
