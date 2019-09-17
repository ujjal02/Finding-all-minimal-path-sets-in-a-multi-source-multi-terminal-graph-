from directed import directed_graph
from undirected import undirected_graph

print("1.Undirected")
print("2.Directed")
s=int(input())

if(s==1):
    undirected_graph()
elif(s==2):
    directed_graph()
else:
    print("Worng")