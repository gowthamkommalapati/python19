def bfs(u,v):
    cl=[]
    while u!=4:
      x=u
      y=v
      if x<5:
           if [5,y] not in ol and  [5,y] not in cl:
               ol.append([5,y])
      if x>0:
           if [0,y] not in ol and  [0,y] not in cl :
               ol.append([0,y])
      if y<3:
           if [x,3] not in ol and [x,3] not in cl :
               ol.append([x,3])
      if y>0:
           if [3,0] not in ol and [3,0] not in cl :
               ol.append([3,0])
      if x+y<=5 and y>0:
           if [x+y,0] not in ol and [x+y,0] not in cl :
               ol.append([x+y,0])
      if x+y<=3 and x>0:
           if [0,x+y] not in ol and [0,x+y] not in cl :
               ol.append([0,x+y])
      if x+y>=5 and y>0 :
          if [5,y-(5-x)] not in ol and [5,y-(5-x)]  not in cl :
               ol.append([5,y-(5-x)])
      if x+y>=3 and x>0:
           if [x-(3-y),3] not in ol and [x-(3-y),3] not in cl:
               ol.append([x-(3-y),3])
      cl.append([x,y])
      del ol[0]
      u=ol[0][0]
      v=ol[0][1]
      print((u,v))
x=int(0)
y=int(0)
ol=[[0,0]]
bfs(0,0)

