# BFS for trees
def bfs_tree(root):
    # If the tree is empty, return an empty list
    if not root:
        return []
    # Initialize queue to store nodes to be visited and result list
    queue, result = [root], []
    # Loop until the queue is empty
    while queue:
        # Get the first node in the queue
        node = queue.pop(0)
        # Add the value of the node to the result list
        result.append(node[0])
        # If the node has children, add them to the queue
        if node[1]:
            queue.extend(node[1:])
    return result

# DFS for trees
def dfs_tree(root):
    # If the tree is empty, return an empty list
    if not root:
        return []
    # Initialize stack to store nodes to be visited and result list
    stack, result = [root], []
    # Loop until the stack is empty
    while stack:
        # Get the last node in the stack
        node = stack.pop()
        # Add the value of the node to the result list
        result.append(node[0])
        # If the node has children, add them to the stack
        if node[2]:
            stack.extend(node[2:])
    return result

# BFS for graphs
def bfs_graph(graph, start):
    # Initialize visited set to keep track of visited vertices,
    # queue to store vertices to be visited, and result list
    visited, queue, result = set(), [start], []
    # Loop until the queue is empty
    while queue:
        # Get the first vertex in the queue
        vertex = queue.pop(0)
        # If the vertex has not been visited
        if vertex not in visited:
            # Add the vertex to the result list
            result.append(vertex)
            # Mark the vertex as visited
            visited.add(vertex)
            # Add unvisited neighbors of the vertex to the queue
            queue.extend(graph[vertex] - visited)
    return result

# DFS for graphs
def dfs_graph(graph, start, visited=None):
    # If visited set is not provided, create an empty set
    if visited is None:
        visited = set()
    # Mark the current vertex as visited
    visited.add(start)
    # Initialize result list with the current vertex
    result = [start]
    # Explore unvisited neighbors of the current vertex
    for neighbor in graph[start] - visited:
        # Recursively call DFS on unvisited neighbors
        result.extend(dfs_graph(graph, neighbor, visited))
    return result

# Example tree
tree = (1, (2, (4, None, None), (5, None, None)), (3, None, None))

print("BFS for tree:", bfs_tree(tree))
print("DFS for tree:", dfs_tree(tree))

# Example graph
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B'},
    'F': {'C'}
}

print("BFS for graph:", bfs_graph(graph, 'A'))
print("DFS for graph:", dfs_graph(graph, 'A'))
