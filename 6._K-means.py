import math
import sys

m=int(input("no.of data points: "))
n=int(input("no.of dimensions per a data point: "))

#to read data points and centroid

l=[]
for i in range(m):
    k=input("enter a data point with "+str(n)+" dimensions: ").split()
    k=[int(i) for i in k]
    if(len(k)==n):
        l=l+[k]
    else :
        print("Data point with incorrect dimensions...!")
        sys.exit()
print('\n\nThe given data points are',l)

c=int(input("enter no.of clusters: "))
g=[]
for i in range(c):
    g=g+[l[i]]
print("\nInitialized centeriod matrix:")
print(g)

#calcute first distance and group matrix

dist = [[0] * c for i in range(m)]
print('\nintial distance matrix',dist)

for i in range(m):
    for j in range(c):
        t=0
        for k in range(n):
            t=t+(l[i][k]-g[j][k])*(l[i][k]-g[j][k])
        t=math.sqrt(t)
        dist[i][j]=t
print("\nDistance matrix after 1st iteration: ")
print(dist)

g = [[0] * n for i in range(c)]
grp = [[0] * c for i in range(m)]
grp1 = [[0] * c for i in range(m)]
t=[0 for i in range(c)]
for i in range(m):
    for j in range(c):
        if(dist[i][j]==min(dist[i])):
            grp[i][j]= j+1
            for k in range(n):            
                g[j][k]+=l[i][k]
            t[j]+=1
        else:
            grp[i][j]=0
            
for j in range(c):
    for k in range(n):
        g[j][k]/=t[j]  
print("\nCluster Membership  matrix after 1st iteration: ")
print(grp)
print("\nupdated centeriod matrix after 1st iteration:")
print(g)

#for next iterations

while(grp1!=grp) :
    for i in range(m):
        for j in range(c):
            t=0
            for k in range(n):
                t=t+(l[i][k]-g[j][k])*(l[i][k]-g[j][k])
            t=math.sqrt(t)
            dist[i][j]=t
    print("\nDistance matrix in next iteration: ")
    print(dist)

    g = [[0] * n for i in range(c)]
    grp1=grp
    grp = [[0] * c for i in range(m)]
    t=[0 for i in range(c)]
    for i in range(m):
        for j in range(c):
            if(dist[i][j]==min(dist[i])):
                grp[i][j]= j+1
                for k in range(n):            
                    g[j][k]+=l[i][k]
                t[j]+=1
            else:
                grp[i][j]=0
                
    for j in range(c):
        for k in range(n):
            g[j][k]/=t[j]  
    print("\nCluster Membership after next iteration: ")
    print(grp)
    print("\n\n\nUpdated centroid matrix after next iteration:")
    print(g)
