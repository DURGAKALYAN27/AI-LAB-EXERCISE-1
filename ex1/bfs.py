from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, x, y):
        self.graph[x].append(y)
        
    def bfsearch(self, start):
        visited = set()
        queue = []
        
        visited.add(start)
        queue.append(start)
        
        while queue:
            n = queue.pop(0)
            print(n, end=" ")
            
            for v in self.graph[n]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)
                    
def main():
    g = Graph()
    
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 7)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(3, 7)
    g.addEdge(4, 6)
    g.addEdge(5, 6)
    g.addEdge(7, 6)
    
    g.bfsearch(1)
    
main()