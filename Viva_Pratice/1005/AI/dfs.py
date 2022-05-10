graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '4': ['8'],
    '8':[],
    '2':[]
}

visited = []

def dfs(n):
    if(n not in visited):
        print(n)
        visited.append(n)
        for i in graph[n]:
            dfs(i)

dfs('5')            