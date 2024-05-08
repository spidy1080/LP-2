import heapq

class Node:
    def __init__(self, name, distance=float('inf')):
        self.name = name
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

def dijkstra(graph, source):
    nodes = {}
    for node in graph:
        nodes[node] = Node(node)

    nodes[source].distance = 0
    queue = [nodes[source]]

    while queue:
        current_node = heapq.heappop(queue)

        if current_node.distance == float('inf'):
            break

        for neighbor, distance in graph[current_node.name].items():
            new_distance = current_node.distance + distance

            if new_distance < nodes[neighbor].distance:
                nodes[neighbor].distance = new_distance
                heapq.heappush(queue, nodes[neighbor])

    return nodes

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 3, 'D': 2},
    'C': {'A': 2, 'B': 3, 'D': 1},
    'D': {'B': 2, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

source = 'A'

nodes = dijkstra(graph, source)
print("Shortest path from node A to each node : ")
for node in nodes.values():
    print(f"{node.name}: {node.distance}")
