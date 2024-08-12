from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, x, y):
        self.graph[x].append(y)
        
    def dfs_limited(self, start, depth_limit, goal):
        visited = set()
        
        def dfs_recursive(node, depth):
            if depth > depth_limit:
                return False
            
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                
                if node == goal:
                    return True
                
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        if dfs_recursive(neighbor, depth + 1):
                            return True
            
            return False
        
        return dfs_recursive(start, 0)
        
    def iterative_deepening_dfs(self, start, goal):
        depth = 0
        while True:
            print(f"\nDepth {depth}:")
            if self.dfs_limited(start, depth, goal):
                print(f"\nGoal {goal} found at depth {depth}")
                return depth
            depth += 1

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
    
    print("Iterative Deepening DFS starting from vertex 1, searching for goal 6:")
    g.iterative_deepening_dfs(1, 6)

main()