class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state  # The current state
        self.parent = parent  # The parent node
        self.action = action  # The action taken to reach this node

class StackFrontier:
    def __init__(self):
        self.stack = []
    
    def add(self, node):
        self.stack.append(node)
    
    def remove(self):
        if self.is_empty():
            raise Exception("Frontier is empty!")
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def contains_state(self, state):
        return any(node.state == state for node in self.stack)

class SearchAlgorithm:
    def __init__(self, start_state, goal_state, neighbors_func):
        self.start_state = start_state
        self.goal_state = goal_state
        self.neighbors_func = neighbors_func  # Function to get neighbors of a state
    
    def depth_first_search(self):
        start_node = Node(self.start_state)
        frontier = StackFrontier()
        frontier.add(start_node)
        explored = set()
        
        while not frontier.is_empty():
            node = frontier.remove()
            
            # Goal check
            if node.state == self.goal_state:
                return self.reconstruct_path(node)
            
            explored.add(node.state)
            
            # Expand node
            for action, state in self.neighbors_func(node.state):
                if state not in explored and not frontier.contains_state(state):
                    child_node = Node(state, node, action)
                    frontier.add(child_node)
        
        return None  # No solution found
    
    def reconstruct_path(self, node):
        path = []
        while node.parent is not None:
            path.append((node.action, node.state))
            node = node.parent
        path.reverse()
        return path

# Example usage 
graph = {
    'A': [('B', 'B'), ('C', 'C')],
    'B': [('D', 'D'), ('E', 'E')],
    'C': [('F', 'F')],
    'D': [],
    'E': [('G', 'G')],
    'F': [],
    'G': []
}

def neighbors(state):
    return graph.get(state, [])

search = SearchAlgorithm(start_state='A', goal_state='G', neighbors_func=neighbors)
solution = search.depth_first_search()

print("DFS Solution Path:", solution)
