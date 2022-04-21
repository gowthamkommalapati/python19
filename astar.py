def astar_algorihm(start_node,end_node):
    open_set=set(start-node)
    closed_set=set()
    g={}
    parents={}
    g[start_node]=0
    parents[start_node]=start_node
    while len(open_set)>0:
        n=none
    for v in open_set:
        if n==none or g[v]+heuristic(v)<g[n]+heuristic(n):
            n=v
        if n==end_node or graph_nodes[n]==none:
            pass
        else:
            for(m,weight)in get_neighbours(n):
                if m not in open_set and m not in data_set:
                    open_set.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
                    if n==none:
                        print("path does not exist!")
                        return none
                    if n==end_node:
                        path=[]
                        while parents[n]!=n:
                            path.append(n)
                            n=parents[n]
                        path.append(start_node)
                        path.reverse()
                        print('path found:{}'.forward(path))
                        return path
                    open_set.remove(n)
                    closed_set.add(n)
                    print("path does not exist!")
                    return none
def get_neighbours(v):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return none
def heuristic(n):
    h_dist={'s':5,
            'a':5,
            'b':3,
            'c':4,
            'd':6,
            'e':5,
            'f':6,
            'g1':0,
            'g2':0,
            'g3':0
            }
    return h_dist[n]
graph_nodes={
    's':[('a',5),('b',9),('d',6)]
    'a':[('b',3),('g1',9)]
    'b':[('a',2),('c',1)]
    'c':[('s',6),('g2',5),('f',7)]
    'd':[('c',2),('e',2),('s',1)]
    'e':[('g3',7)]
    'f':[('d',2),('g3',8)]
    }
astar_algorithm('s','g2')

                
