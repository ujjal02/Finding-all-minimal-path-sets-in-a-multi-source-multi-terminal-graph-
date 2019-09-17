G=[[], [2, 3, 7], [1, 3, 4, 13], [1, 2, 6], [2, 5, 13], [4, 6, 14], [3, 5, 7, 14], [1, 6, 8], [7, 9], [8, 12, 15], [], [], [9, 16], [2, 4], [5, 15], [14, 16], [12, 15], [], []]
T=[9]
S=[2]
l=[]
s=[]

def add_node(n):
    l.append(n)
    s.append(n)
    
def path():
    for x in S:
        next_node(x)
        l.clear()
        s.clear()
        
def next_node(n):
    if n in T:
        add_node(n)
        print(l)
        l.pop()
        s.pop()
        return
    else:
        add_node(n)
        for x in G[n]:
            if(x not in s):
                next_node(x)
        l.pop()
        s.pop()

path()