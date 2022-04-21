def bb(cost,ol,cl,g):
    found=False
    a=0
    e={}
    co=0
    while ol!=[] and found==False:
        if len(ol)==1:
            a=ol[0][0]
            co=ol[0][1]
        else:
            t=9999;
            for i in range(len(ol)):
               if ol[i][1]<t:
                  t=ol[i][1]
                  a=ol[i][0]
            co=t
        if a in g:
            print("goal nodes and cost",a,t)
            found=True
        else:
            print(a)
            cl.append([a,co])
            e[a]=co
            ol.remove([a,co])
            for i in range(len(cost)):
                if i not in e.keys() and cost[a][i]!=0 :
                    ol.append([i,co+cost[a][i]])
n=int(input("enter the number of vertices"))
cost=[]
for i in range(n):
    temp=list(map(int,input().split()))
    cost.append(temp)
g=list(map(int,input("enter the goal nodes").split()))
ol=[[0,0]]
cl=[]
bb(cost,ol,cl,g)
