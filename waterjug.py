x=int(0)
y=int(0);
a=[]
while x!=4:
    n=int(input("enter the production rule"))
    a.append(n)
    if n==1:
        x=5;
    elif n==2:
        x=0;
    elif n==3:
        y=3;
    elif n==4:
        y=0;
    elif n==5:
        x=x+y;
    elif n==6:
        y=y+x;
    elif n==7:
        y=y-(5-x);
        x=5;               
    elif n==8:
        x=x-(3-y);
        y=3;
print("goal state reached")
print(a)
