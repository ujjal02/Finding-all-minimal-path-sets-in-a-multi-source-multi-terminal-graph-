def reduction(G,V,T,S):
    to_delete=[]
    for i in range(0,V):
        if(len(G[i])==1 and i not in T and i not in S):
            to_delete.append(i)

    print(to_delete)

    while True:
        if(len(to_delete)==0):
            break
        x=to_delete.pop()
        for y in G[x]:
            if(len(G[y])==2):
                to_delete.append(y)
        delete_node(G,x) 
        
        
    return G
    
def delete_node(G,n):
    for i in G[n]:
        if n in G[i]:
            G[i].remove(n)
            
    G[n].pop()