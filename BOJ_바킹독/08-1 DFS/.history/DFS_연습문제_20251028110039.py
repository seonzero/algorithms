def dfs():
    pass

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'G'],
    'D': ['B', 'F'],
    'E': ['B', 'F'], 
    'F': ['D', 'E', 'G'],
    'G': ['C', 'F']
}

start_vertex = 'A'
visited = set()
result = []

dfs()

print(' '.join(result))