from collections import deque

graph = {
    '1': ['2','3'],
    '2': ['1','4'],
    '3': ['1','4'],
    '4': ['2','3'],
}

grap = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G', 'H'],
    'D': ['A', 'H', 'I'],
    'E': ['B', 'J'],
    'F': ['B', 'J', 'K'],
    'G': ['C', 'L'],
    'H': ['C', 'D', 'L', 'M'],
    'I': ['D', 'M'],
    'J': ['E', 'F', 'N'],
    'K': ['F', 'N'],
    'L': ['G', 'H', 'O'],
    'M': ['H', 'I', 'O'],
    'N': ['J', 'K', 'P'],
    'O': ['L', 'M', 'P'],
    'P': ['N', 'O']
}

def bfs(graph,root):
    visited = set()
    queue = deque([root]) # 1

    visited.add(root) # {1}

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
bfs(grap,'A')

