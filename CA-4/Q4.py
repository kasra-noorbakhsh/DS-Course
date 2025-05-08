N = int(input())
X = 0

class Node:
    
    def __init__(self, v, label):
        self.node = v
        self.edgeLabel = label
        
adj = [[] for _ in range(N + 1)]

freq = [0] * N

def dfs(u, p):
    global N
    global X

    sz = 1

    for a in adj[u]:

        if a.node != p:

            val = dfs(a.node, u)

            freq[X] = (val * (N - val), a.edgeLabel)
            X += 1
            sz += val

    return sz

def addEdge(u, v, label):
    adj[u].append(Node(v, label))
    adj[v].append(Node(u, label))

def sol():

    global N
    

    dfs(1, 1)
    total = 0
    for i in range(X):
        total += freq[i][0] * freq[i][1]
        
    return total


try:
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        addEdge(u, v, w)
    
    print(sol())
except: 
    print("An error occurred while processing the input.")