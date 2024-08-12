from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, x, y):
        self.graph[x].append(y)
        
    def dfs_limited(self, start, depth_limit):
        visited = set()
        
        def dfs_recursive(node, depth):
            if depth > depth_limit:
                return False
            
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        if dfs_recursive(neighbor, depth + 1):
                            return True
            
            return False
        
        return dfs_recursive(start, 0)

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
    
    
    print("Depth Limited DFS starting from vertex 1, searching with depth 2:")
    g.dfs_limited(1, 2)

main()