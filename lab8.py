n = int(input("Enter number of vertices: ")) 
adj = [[0]*n for _ in range(n)] 
e = int(input("Enter number of edges: ")) 
print("Enter edges (u v):") 
for _ in range(e): 
    u, v = map(int, input().split()) 
adj[u][v] = adj[v][u] = 1 
print("Adjacency Matrix:") 
for row in adj: 
    print(row) 