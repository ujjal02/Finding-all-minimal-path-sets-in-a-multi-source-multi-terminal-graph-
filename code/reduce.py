to_delete_in=[]
to_delete_out=[] 
    
def incoming(G,x):
    '''
    returns the set of nodes connected to x with incoming edges
    '''
    return G[x][0]

def outgoing(G,x):
    '''
    returns the set of nodes connected to x with outgoing edges
    '''
    return G[x][1]

def delete_incoming(G,n):
    '''delete the node n from the graph having 0 incoming edge
    '''
    for x in outgoing(G,n):
        if n in G[x][0]:
            G[x][0].remove(n)
    for _ in range(0,len(G[n][1])):
        G[n][1].pop()

def delete_outgoing(G,n):
    '''delete the node n from the graph having 0 outgoing edge
    '''
    for x in incoming(G,n):
        if n in G[x][1]:
            G[x][1].remove(n)
    for _ in range(0,len(G[n][0])):
        G[n][0].pop()
    
def reduction(G,t,s,V):
    
    for x in range(0,V):
        if(len(incoming(G,x))==0 and x not in s):
            to_delete_in.append(x)
        elif(len(outgoing(G,x))==0 and x not in t):
            to_delete_out.append(x)
    
    while True:
        if(len(to_delete_in)==0):
            break
        x=to_delete_in.pop()
        for y in outgoing(x):
            if(len(incoming(G,y))==1):
                to_delete_in.append(y)
        delete_incoming(G,x)
        
                    
    while True:
        if(len(to_delete_out)==0):
            break
        x=to_delete_out.pop()
        for y in incoming(G,x):
            if(len(outgoing(G,y))==1):
                to_delete_out.append(y)        
        delete_outgoing(G,x)
        
    return G