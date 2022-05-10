

class Node:
    def __init__(self, h=0, g=999999, f=0, name=0):
        self.h = h
        self.g = g
        self.f = f
        self.name = name

    def setNeighbours(self, neighbours={}):
        self.neighbours = neighbours

def astar(start, goal):
    openSet = set([start])
    closedSet = set([])
    cameFrom = {}
    parents = {}
    start.g = 0
    start.f = start.h
    while(len(openSet) != 0):
        current = findNodeWithLowestFScore(openSet)
        if(current == goal):
            return construct_path(cameFrom, current)
        openSet.remove(current)
        closedSet.add(current)
        for neigh in current.neighbours:
            if(neigh in closedSet):
                continue
            if(neigh not in openSet):
                openSet.add(neigh)

            gScore = current.g + graph[current.name][neigh.name]
            if(gScore >= neigh.g):
                continue
            cameFrom[neigh] = current
            neigh.g = gScore
            neigh.f = neigh.g + neigh.h        
    return -1

def construct_path(cameFrom, current):

	totalPath = []
	while current in cameFrom.keys():
		current = cameFrom[current]
		totalPath.append(current)

	return totalPath

def findNodeWithLowestFScore(openSet):
    minF = 999999
    node = None
    for nod in openSet:
        if(nod.f < minF):
            node = nod
            minF = nod.f
    return node        
graph = [
    # s, a, b, c, d
    [-1, 1, 4, -1, -1],
    [1, -1, 2, 5, 12],
    [4, 2,  -1, 2,-1 ],
    [-1, 5, 2, -1, 3],
    [-1, 12, -1, 3, -1]
]

heu = [7,6,2,1,0]

s = Node(h=heu[0], name=0)
a = Node(h=heu[1], name=1)
b = Node(h=heu[2], name=2)
c = Node(h=heu[3], name=3)
d = Node(h=heu[4], name=4)

s.setNeighbours([a,b])
a.setNeighbours([s,b, c, d])
b.setNeighbours([s,a, c])
c.setNeighbours([a, b,d])
d.setNeighbours([a, c])


start = s
goal = d
path  = astar(s,d)
print(path)
for nod in path[::-1]:
    print(nod.name)
print(goal.name)    
print(goal.g)