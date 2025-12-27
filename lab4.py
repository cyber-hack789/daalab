#4.Write program to implement the DFS and BFS algorithm for a graph.

g={'A':['B','C'],
   'B':['C'],
   'C':['A','D'],
   'D':[]}
def bfs(s):
 v=[]
 q=[s]
 while q:
  x=q.pop(0)
  if x not in v:
     v+=[x]
     q+=g[x]
 return v
def dfs(s):
 v=[]
 st=[s]
 while st:
  x=st.pop()
  if x not in v:
    v+=[x]
    st+=g[x]
 return v
print(bfs('C'),dfs('C'))
