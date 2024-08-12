from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, x, y):
        self.graph[x].append(y)
        
    def dfsearch(self, start):
        visited = set()
        stack = []
        
        stack.append(start)
        
        while stack:
            n = stack.pop()
            if n not in visited:
                print(n, end = " ")
                visited.add(n)
            
            # Add unvisited neighbors to the stack
            for v in reversed(self.graph[n]):
                if v not in visited:
                    stack.append(v)
                    
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
    
    print("DFS starting from vertex 1:")
    g.dfsearch(1)
    
main()