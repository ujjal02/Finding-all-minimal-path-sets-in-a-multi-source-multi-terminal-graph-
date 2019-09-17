import numpy as np
import networkx as nx
import reduce
import findpath1

def directed_graph():
    R=[]
    G=[]
    V=int(input("Enter no of vertices:"))
    S=list(map(int,input("Enter source vertices:").split()))
    T=list(map(int,input("Enter terminal vertices:").split()))
    s=[0]
    t=[V-1]
    
    for i in range(0,V):
        print("Incoming nodes to ",i)
        l1=list(map(int,input().split()))
        print("Outgoing nodes from ",i)
        l2=list(map(int,input().split()))
        G.append([])
        if(-1 in l1):
            G[i].append([])
        else:
            G[i].append(l1)
        
        if(-1 in l2):
            G[i].append([])
        else:
            G[i].append(l2)

    print("1.Uniform Reliablility")
    print("2.Non-uniform Reliability")
    c=int(input("Enter:"))
    if(c==1):
        r=float(input("Enter reliability:"))
        for i in range(0,V):
            R.append(r)
    elif(c==2):
        for i in range(0,V):
            print("Enter reliability of node ",i,end='')
            R.append(float(input()))
    
    original_adjacency_matrix=np.full((V,V),0)

    for i in range(0,V):
        for j in range(0,V):
            if(j in G[i][0]):
                original_adjacency_matrix[i][j]=-1
            elif(j in G[i][1]):
                original_adjacency_matrix[i][j]=1
                
    print("Original Adjacency Matrix:")
    print(original_adjacency_matrix)
    #print("Original Graph")
    #original_graph=nx.Graph(original_adjacency_matrix)
    #nx.draw(original_graph)
    print("Original Graph:",G)
    G_reduced=reduce.reduction(G,t,s,V)
    
    print("Reduced Graph:",G_reduced)
    
    reduced_adjacency_matrix=np.full((V,V),0)
    
    for i in range(0,V):
        for j in range(0,V):
            if(j in G_reduced[i][0]):
                reduced_adjacency_matrix[i][j]=-1
            elif(j in G_reduced[i][1]):
                reduced_adjacency_matrix[i][j]=1

    print("Reduced Adjacency matrix:")
    print(reduced_adjacency_matrix)

    r=findpath1.path(G_reduced,S,T,R)
    reliability=1.0
    for i in r:
        reliability*=i
    print("Reliability of the minial path set:",(1-reliability))