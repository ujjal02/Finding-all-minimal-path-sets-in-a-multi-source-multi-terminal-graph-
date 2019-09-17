from demo import print_exp
l=[]
visited_node=[]
l1=[]
r=[]
p=[]

def add_node(n):
    l.append(n)
    visited_node.append(n)
    
def path(G_directed,T,S,R):
    for x in S:
        next_node(G_directed,T,S,x,R)
        l.clear()
        visited_node.clear()
    
    print_exp(p)
    return r
        
def next_node(G_directed,T,S,n,R):
    if n in T:
        r1=1.0
        add_node(n)
        p.append(l)
        print(p)
        for i in l:
            r1=r1*R[i]
        r.append(1-r1)
        print(l)
        l.pop()
        visited_node.pop()
        return
    else:
        add_node(n)
        for x in G_directed[n][1]:
            if x not in visited_node:
                next_node(G_directed,T,S,x,R)
        l.pop()
        visited_node.pop()