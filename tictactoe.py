def valid_2(n):
    if n in l:
        return 0;
    else:
        return 1
def poswin():
    
k=int(input())
ms=[8,1,6,3,5,7,4,9,2]
move=[1,2,3,4,5,6,7,8,9]
np=[]
found=["win","draw","loose"]
t=False
i=1
nc=1
np=1
while t!=True:
    if i%3==0 :
        print("palyers Move")
        s=0
        while(s==0):
            n=int(input("enter the move"))
            if n in move:
                s=1
                ms[n-1]="x"
                np.append(ms[n-1])
        printf("players move is ",n);
    else:
        if i==2 :
            if 5 in l:
                l.append(5)
                
            else:
                l.append(1)
        if i==4:
            x=poswin()
            if x!=0:
                ms[x]="c"
                move.remove(x)
            else:
                ms[
    
