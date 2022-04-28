"""  
0 -  1  - 4
|   |  /
2 - 3 
   
"""

class Node:

    def __init__(self, f=0, h=0, name=0, g=999999):
        self.f = f
        self.h = h
        self.g = g
        self.name = name

    def setNeighbours(self, neighbours={}):
        self.neighbours = neighbours


def aStar(start, goal):
    closedSet = set([])
    openSet = set([start])
    cameFrom = {}
    start.g = 0
    start.f = start.h

    while(len(openSet)):
        current = findNodewithLowestScore(openSet)
        if(current == goal):
            return constructPath(cameFrom, current)

        openSet.remove(current)
        closedSet.add(current)

        for neighbour in current.neighbours:
            if(neighbour in closedSet):
                continue
            else:
                openSet.add(current)
            tentativeGScore = current.g + graph[current.name][neighbour.name]
            if(tentativeGScore >= neighbour.g):
                continue
            cameFrom[neighbour] = current
            neighbour.g = tentativeGScore
            neighbour.f = neighbour.g + neighbour.h
    return -1


def findNodewithLowestScore(openSet):
    fscore = 999999
    node = None
    for each in openSet:
        if(each.f < fscore):
            fscore = each.f
            node = each
    return node


def constructPath(cameFrom, current):
    totalPath = []
    while(current in cameFrom.keys()):
        curr = cameFrom[current]
        totalPath.append(current)

    return totalPath            

heuristics = [7, 6, 2, 1, 0]
