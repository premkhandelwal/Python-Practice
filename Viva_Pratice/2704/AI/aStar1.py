
def aStar(start, goal):
    openSet = set(start)
    closedSet = set()
    g = {}
    parents = {}
    g[start] = 0
    parents[start] = start
    while(len(openSet)):
        n = None
        for v in openSet:
            if(n == None or ((g[v] + h(v)) < (g[n] + h(n)))):
                n = v

        if(n == goal or graphNodes[n] == None):
            pass
        else:
            for (m, cost) in getNeighbours(n):
                f = g[n] + cost
                parents[m] = n
                if(m not in openSet and m not in closedSet):
                    openSet.add(m)
                    g[m] = f         
                else:
                    if(g[m] > f):
                        g[m] = f 
                        if(m in closedSet):
                            closedSet.remove(m)
                            openSet.add(m)

        if(n == None):
            print("Path does not exist")
            return None
        if(n == goal):
            path = []
            while(parents[n] != n):
                path.append(n)
                n = parents[n]

            path.append(start) 
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        openSet.remove(n)
        closedSet.add(n)
    print('Path does not exist!')
    return None  


def getNeighbours(v):
    if v in graphNodes:
        return graphNodes[v]
    else:
        return None
#for simplicity we ll consider heuristic distances given
#and this function returns heuristic distance for all nodes
def h(n):
    H_dist = {
            'A': 11,
            'B': 6,
            'C': 99,
            'D': 1,
            'E': 7,
            'G': 0,       
        }
 
    return H_dist[n]
 
#Describe your graph here  
graphNodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
     
}
aStar('A', 'G')          
