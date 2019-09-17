import numpy as np
import networkx as nx
import reduce_undirected
import convert_undirected
import finpath2

def undirected_graph():
    R=[]
    G=[]
    V=int(input("Enter no of vertices:"))
    S=list(map(int,input("Enter source vertices:").split()))
    T=list(map(int,input("Enter terminal vertices:").split()))
    s=[0]
    t=[V-1]

    for i in range(0,V):
        print("nodes connected to ",i,":")
        l=list(map(int,input().split()))
        G.append(l)

    original_adjacency_matrix=np.full((V,V),0)

    for i in range(0,V):
        for j in range(0,V):
            if(j in G[i]):
                original_adjacency_matrix[i][j]=1
                
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
                
    print("Original Adjacency Matrix:")
    print(original_adjacency_matrix)
    print("Original Graph")
    original_graph=nx.Graph(original_adjacency_matrix)
    nx.draw(original_graph)

    G_reduced=reduce_undirected.reduction(G,V,t,s)

    reduced_adjacency_matrix=np.full((V,V),0)

    for i in range(0,V):
        for j in range(0,V):
            if(j in G_reduced[i]):
                reduced_adjacency_matrix[i][j]=1

    print("Reduced Adjacency Matrix:")
    print(reduced_adjacency_matrix)
    #print("Reduced Graph")
    #reduced_graph=nx.Graph(original_adjacency_matrix)
    #nx.draw(reduced_graph)

    G_directed=convert_undirected.convert(G_reduced,S,T,V)
    r=finpath2.path(G_directed,T,S,R)
    reliability=1.0
    for i in r:
        reliability*=i
    print("Reliability of the minial path set:",(1-reliability))