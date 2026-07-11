from collections import deque

graph = {
    '1': ['2','3'],
    '2': ['1','4'],
    '3': ['1','4'],
    '4': ['2','3'],
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
bfs(graph,'1')

### Basic in farhan hosain youtube