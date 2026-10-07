# kombin_labs
Лабораторная работа №2
```Python
from collections import defaultdict

edges = [
    (1, 1, 2), (2, 2, 3), (3, 3, 4),
    (4, 1, 4), (5, 1, 3), (6, 2, 4),
    (7, 5, 6), (8, 5, 7)
]

graph = defaultdict(list)
for edge_id, u, v in edges:
    graph[u].append((v, edge_id))
    graph[v].append((u, edge_id))

visited = set()
used_edges = set()
components = []

for start in graph:
    if start in visited:
        continue
    stack = [start]
    visited.add(start)
    component = [start]
    while stack:
        current = stack[-1]
        found = False
        for neighbor, edge_id in graph[current]:
            if edge_id not in used_edges:
                used_edges.add(edge_id)
                found = True
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    component.append(neighbor)
                break
        if not found:
            stack.pop()
    components.append(component)

for c in components:
    print(c)
```
### Вывод
<img width="1064" height="423" alt="image" src="https://github.com/user-attachments/assets/874f1c13-eb97-4e1c-a06e-2c54c74b3068" />
