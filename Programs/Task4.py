def alpha_beta(node, alpha, beta, maximizing_player):
    # If the node is a terminal node (i.e., an integer representing a score), return the score
    if isinstance(node, int):
        return node

    if maximizing_player:
        value = float('-inf')  # Initialize the value for the maximizing player as negative infinity
        # Loop through the children of the node
        for child in node.values():
            value = max(value, alpha_beta(child, alpha, beta, False))  # Recursively call alpha_beta for child nodes
            alpha = max(alpha, value)  # Update alpha to the maximum value found so far
            if alpha >= beta:
                break  # Prune the search if alpha is greater than or equal to beta
        return value
    else:
        value = float('inf')  # Initialize the value for the minimizing player as positive infinity
        # Loop through the children of the node
        for child in node.values():
            value = min(value, alpha_beta(child, alpha, beta, True))  # Recursively call alpha_beta for child nodes
            beta = min(beta, value)  # Update beta to the minimum value found so far
            if beta <= alpha:
                break  # Prune the search if beta is less than or equal to alpha
        return value

# Example usage
if __name__ == "__main__":
    tree = {
        'root': {'a': {'d': 8, 'e': 9}, 'b': {'f': 10, 'g': 11}, 'c': {'h': 12}}
    }

    print(alpha_beta(tree, float('-inf'), float('inf'), True))
