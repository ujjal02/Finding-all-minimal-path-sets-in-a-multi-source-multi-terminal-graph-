def convert(G_reduced,S,T,V):
    
    G_directed=[]
    for i in range(0,V):
        G_directed.append([])
        G_directed[i].append([])
        G_directed[i].append([])
        
        if i in S:
            for y in G_reduced[i]:
                G_directed[i][1].append(y)  
        elif i in T:
            for y in G_reduced[i]:
                G_directed[i][0].append(y)
        else:
            for y in G_reduced[i]:
                if y in T:
                    G_directed[i][1].append(y)
                elif y in S:
                    G_directed[i][0].append(y)
                else:
                    G_directed[i][0].append(y)
                    G_directed[i][1].append(y)
                    
    return G_directed