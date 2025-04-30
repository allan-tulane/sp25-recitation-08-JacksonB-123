from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    dist = {}
    for v in graph:
        dist[v] = (float('inf'), float('inf'))
    dist[source] = (0, 0)
    pq = []
    heappush(pq, (0, 0, source))

    while pq:
        total_weight, num_edges, node = heappop(pq)

        if (total_weight, num_edges) > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_weight = total_weight + weight
            new_num_edges = num_edges + 1

            if new_weight < dist[neighbor][0] or (
                new_weight == dist[neighbor][0] and new_num_edges < dist[neighbor][1]):
                dist[neighbor] = (new_weight, new_num_edges)
                heappush(pq, (new_weight, new_num_edges, neighbor))

    return dist
  
    
  
  
    pass
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    visited = set()
    queue = deque([source])
    visited.add(source)
    queue.append(source)
    parents = {}
    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parents[neighbor] = current_node
    return parents
    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    current_node = destination
    while current_node in parents:
        path.append(parents[current_node])
        current_node = parents[current_node]
    path.reverse()
    return ''.join(path)
    pass

