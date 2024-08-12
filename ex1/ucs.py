import heapq
from collections import defaultdict

class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, x, y, cost):
        self.graph[x].append((y, cost))
    
    def uniform_cost_search(self, start, goal):
        priority_queue = [(0, start)]
        visited = set()
        
        while priority_queue:
            (cost, node) = heapq.heappop(priority_queue)
            
            if node not in visited:
                visited.add(node)
                
                print(f"Visiting node {node} with cost {cost}")
                
                if node == goal:
                    return cost
                
                for (neighbor, edge_cost) in self.graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (cost + edge_cost, neighbor))
        
        return float('inf')  # If goal is not reached

def main():
    g = WeightedGraph()
    
    g.addEdge(1, 2, 4)
    g.addEdge(1, 3, 2)
    g.addEdge(2, 3, 1)
    g.addEdge(2, 4, 5)
    g.addEdge(3, 4, 8)
    g.addEdge(3, 5, 10)
    g.addEdge(4, 5, 2)
    g.addEdge(4, 6, 6)
    g.addEdge(5, 6, 3)
    
    start = 1
    goal = 6
    print(f"Uniform Cost Search from node {start} to node {goal}:")
    cost = g.uniform_cost_search(start, goal)
    print(f"Minimum cost from {start} to {goal}: {cost}")

main()