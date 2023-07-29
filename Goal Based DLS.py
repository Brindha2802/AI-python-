
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited, goal, depth, max_depth, path):
        visited.add(v)
        path.append(v)
        if v == goal:  
            return True
        if depth == max_depth:  
            return False
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.DFSUtil(neighbour, visited, goal, depth+1, max_depth, path):
                    return True
        path.pop()  
        return False
    def DFS(self,v, goal, max_depth):
        visited=set()
        path = []
        found = self.DFSUtil(v,visited, goal, 0, max_depth, path)
        if found:
            print("Goal reached!")
            print("Path: ", end="")

            for node in path:
                print(node, end=" ")

        else:
            print(False)


if __name__=="__main__":
    g=Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(1,4)
    g.addEdge(1,5)
    g.addEdge(3,4)
    g.addEdge(4,6)
   
    goal = 5
    max_depth = 3

    print("DFS traversal:")
    g.DFS(0, goal, max_depth)
