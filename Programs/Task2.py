import time
import random
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

def generate_random_numbers(size):
    """Generate unique random numbers for each set."""
    return random.sample(range(1, size + 1), size)

def build_tree(numbers):
    """Build a tree from a list of numbers."""
    return {num: {'left': None, 'right': None} for num in numbers}

def bfs(tree, goal):
    """Perform Breadth First Search."""
    start_time = time.time()  # Record the start time
    queue = deque([list(tree.keys())[0]])  # Start from the root node
    while queue:
        node = queue.popleft()  # Get the node at the front of the queue
        if node == goal:  # If the goal is found
            return time.time() - start_time  # Return the time taken
        left_child = tree[node]['left']
        right_child = tree[node]['right']
        if left_child:
            queue.append(left_child)  # Add left child to the queue
        if right_child:
            queue.append(right_child)  # Add right child to the queue
    return time.time() - start_time  # Return time taken even if goal not found

def dfs(tree, goal):
    """Perform Depth First Search."""
    start_time = time.time()  # Record the start time
    stack = [list(tree.keys())[0]]  # Start from the root node
    while stack:
        node = stack.pop()  # Get the node at the top of the stack
        if node == goal:  # If the goal is found
            return time.time() - start_time  # Return the time taken
        left_child = tree[node]['left']
        right_child = tree[node]['right']
        if right_child:
            stack.append(right_child)  # Add right child to the stack
        if left_child:
            stack.append(left_child)  # Add left child to the stack
    return time.time() - start_time  # Return time taken even if goal not found

def main():
    sizes = [1000, 40000, 80000, 200000, 1000000]
    results = {'Total Size': sizes, 'BFS Time': [], 'DFS Time': []}

    for size in sizes:
        numbers = generate_random_numbers(size)
        tree = build_tree(numbers)
        goal = numbers[-220]
        bfs_time = bfs(tree, goal)
        dfs_time = dfs(tree, goal)
        results['BFS Time'].append(bfs_time)
        results['DFS Time'].append(dfs_time)

    df = pd.DataFrame(results)

    # Print the DataFrame
    print("Results:")
    print(df)

    # Plotting the bar chart
    ax = df.plot(x='Total Size', kind='bar')
    ax.set_ylabel('Time (seconds)', fontsize=12)
    ax.set_xlabel('Total Size', fontsize=12)
    ax.set_title('Time taken by BFS and DFS for different sizes', fontsize=14)
    ax.set_xticklabels(df['Total Size'], rotation=45, ha='right')
    plt.show()

if __name__ == "__main__":
    main()
