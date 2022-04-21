import random
n=0
c=1
k=0
game=0
def dash():
    print("%c %c %c" %(bo[1],bo[2],bo[3]))
    print("%c %c %c" %(bo[4],bo[5],bo[6]))
    print("%c %c %c" %(bo[7],bo[8],bo[9]))
    

def check(l):
    global o
    k=0
    for i in l:
        k=k+1
        
        for j in l[k:]:
            d=15-(i+j)
            if(d>0 and d<=9):
                if d in r:
                    o=d
                    return True
                    
                
                
            
    return False
            
    
        
def pos(k):
    global p
    for i in range(1,10):
        if(m[i]==k):
            p=i

def checkwin():
    k=0
    for i in ma:
        k=k+1
        for j in (ma[k:]):
            d=15-(i+j)
            if d in ma:
                if d!=i and d!=j:
                    return True
    return False
    
       

        
            
      
    

def ran():
    global n
    n= random.randint(1,9)
    
    if n in r:
        pass
    else:
        ran()
    
        
    
        
    

m={1:8,2:1,3:6,4:3,5:5,6:7,7:4,8:9,9:2}
r=[8,1,6,3,5,7,4,9,2]
bo=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
l=[]
ma=[]
ch=1
p=0
print("first who you 1 com 0 ")
z=int(input("enter"))
while(game==0):
    if(z==0):
        z=1
        c=c+1
        
        dash()
        print("com chance")
            
    
        if(check(l)):
            l.append(o)
            game=1
            dash()
            print("com winned")
            
            
            pos(o)
            bo[p]='x'
        elif(check(ma)):
            l.append(o)
            r.remove(o)
            
            pos(o)
            bo[p]='x'
        else:
            if 5 in r:
                bo[5]='x'
                r.remove(5)
                l.append(5)
            else:
                print("using random")
                ran()
                pos(n)
                bo[p]='x'
                r.remove(n)
                l.append(n)
                
            
        
    
    dash()
    
    if(c==10):
        print("game draw")
        dash()
        break
    
        
    

    if(game==0 and z==1):
        z=0
        choice=int(input("enter man choice"))
        c=c+1
        
        ma.append(m[choice])
        tem=m[choice]
        r.remove(tem)
        bo[choice]='o'
        if(checkwin()):
            print("game winned by man")
            dash()
            game=1
            
        
    if(c==10):
        print("game draw")
        dash()
        game=1
        break
        
    
            
            
        
