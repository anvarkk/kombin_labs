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
for edge_id, a, b in edges:
    graph[a].append((b, edge_id))
    graph[b].append((a, edge_id))

visited = set()
used_edges = set()
components = []

for start_node in graph:
    if start_node in visited:
        continue
        
    stack = [start_node]
    visited.add(start_node)
    component = [start_node]
    
    while stack:
        current = stack[-1]
        has_next_edge = False
        
        for neighbor, edge_id in graph[current]:
            if edge_id not in used_edges:
                used_edges.add(edge_id)
                has_next_edge = True
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    component.append(neighbor)
                    
                break
                
        if not has_next_edge:
            stack.pop()
            
    components.append(component)

for c in components:
    print(c)
```
### Вывод
<img width="1064" height="423" alt="image" src="https://github.com/user-attachments/assets/874f1c13-eb97-4e1c-a06e-2c54c74b3068" />
