import sys;
def dfs(u,v):
    cl=[]
    if u==4:
        sys.exit()
    while u!=4:
      x=u
      y=v
      if x<5:
           if [5,y] not in ol and  [5,y] not in cl:
               ol.append([5,y])
               print(5,y)
               dfs(5,y);
      if x>0:
           if [0,y] not in ol and  [0,y] not in cl :
               ol.append([0,y])
               print(0,y)
               dfs(0,y);
      if y<3:
           if [x,3] not in ol and [x,3] not in cl :
               ol.append([x,3])
               print(x,3)
               dfs(x,3);
      if y>0:
           if [3,0] not in ol and [3,0] not in cl :
               ol.append([3,0])
               print(3,0)
               dfs(3,0);
      if x+y<=5 and y>0:
           if [x+y,0] not in ol and [x+y,0] not in cl :
               ol.append([x+y,0])
               print(x+y,0)
               dfs(x+y,0)
      if x+y<=3 and x>0:
           if [0,x+y] not in ol and [0,x+y] not in cl :
               ol.append([0,x+y])
               print(0,x+y)
               dfs(0,x+y)
      if x+y>=5 and y>0 :
          if [5,y-(5-x)] not in ol and [5,y-(5-x)]  not in cl :
               ol.append([5,y-(5-x)])
               print(5,y-(5-x))
               dfs(5,y-(5-x))
      if x+y>=3 and x>0:
           if [x-(3-y),3] not in ol and [x-(3-y),3] not in cl:
               ol.append([x-(3-y),3])
               print(x-(3-y),3)
               dfs(x-(3-y),3)
      cl.append([x,y])

x=int(0)
y=int(0)
ol=[[0,0]]
dfs(0,0)
