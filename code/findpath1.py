from demo import print_exp
l=[]
r=[]
p=[]
l1=[]

def add_node(n):
    l.append(n)
    
def path(G,S,T,R):
    for x in S:
        next_node(G,S,T,x,R)
        l.clear()
        
    print_exp(p)
    
    return r
        
def next_node(G,S,T,n,R):
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
        return
    else:
        add_node(n)
        for x in G[n][1]:
            next_node(G,S,T,x,R)
        l.pop()