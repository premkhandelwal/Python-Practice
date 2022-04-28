""" 
    5
  /   \
  3     7
  / \   \
  2 4 - 8    
"""

import queue


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []

}

visited = []
q = []
def bfs(node):
    visited.append(node)
    q.append(node)
    while(len(q)):
        n  = q.pop(0)
        print(n)
        for i in graph[n]:
            if(i not in visited):
                visited.append(i)
                q.append(i)


bfs('5')