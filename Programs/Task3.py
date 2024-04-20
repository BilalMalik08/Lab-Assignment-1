def manhattan_distance(point1, point2):
    # Calculate the Manhattan distance between two points
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(maze, start, goal):
    # Get the number of rows and columns in the maze
    rows, cols = len(maze), len(maze[0])

    # Initialize scores and parent pointers for all nodes
    g_score = {(x, y): float('inf') for x in range(rows) for y in range(cols)}
    g_score[start] = 0
    f_score = {(x, y): float('inf') for x in range(rows) for y in range(cols)}
    f_score[start] = manhattan_distance(start, goal)
    parent = {(x, y): None for x in range(rows) for y in range(cols)}

    # Priority queue for open list
    open_list = [(f_score[start], start)]

    # Closed list to store explored nodes
    closed_list = set()

    while open_list:
        # Get the node with the lowest f_score
        current_f_score, current_node = min(open_list)

        # If goal is reached, reconstruct path
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]  # Reverse for start to goal order

        open_list.remove((current_f_score, current_node))
        closed_list.add(current_node)

        # Explore neighbors
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = current_node[0] + dx, current_node[1] + dy
            # Check if the neighbor is within the maze boundaries and is not a wall
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] != 'W':
                neighbor = (x, y)
                tentative_g_score = g_score[current_node] + 1  # Assuming uniform movement cost

                # If neighbor not yet explored or has better path through current node
                if neighbor not in closed_list and tentative_g_score < g_score.get(neighbor, float('inf')):
                    parent[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + manhattan_distance(neighbor, goal)
                    open_list.append((f_score[neighbor], neighbor))

    return None  # No path found

# Example maze (replace with your actual maze layout)
maze = [
    [' ', ' ', 'W', ' ', 'X', 'Y'],  
    ['R', 'S', 'T', 'U', ' ', 'V'],
    ['M', 'N', ' ', 'O', 'P', 'Q'],
    ['H', 'I', 'J', ' ', 'K', 'L'],
    ['F', ' ', 'G', ' ', ' ', ' '],
    ['A', ' ', 'B', 'C', 'D', 'E'],
]

start = (5, 0)  # Replace with your actual start position (A)
goal = (0, 5)   # Replace with your actual goal position (Y)

path = a_star_search(maze, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found")
