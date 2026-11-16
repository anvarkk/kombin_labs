ЛАБОРАТОРНАЯ РАБОТА 3
'''Python
from collections import defaultdict

# Исходный граф в виде списка рёбер: (номер_ребра, вершина_u, вершина_v)
edges = [
    (1, 1, 2), (2, 2, 3), (3, 3, 4),
    (4, 1, 4), (5, 1, 3), (6, 2, 4),
    (7, 5, 6), (8, 5, 7)
]

# Список смежности: для каждой вершины храним (сосед, номер_ребра).
# Граф неориентированный — каждое ребро добавляем в обе стороны.
graph = defaultdict(list)
for edge_id, u, v in edges:
    graph[u].append((v, edge_id))
    graph[v].append((u, edge_id))

visited = set()      # список помеченных вершин (S'i из лекции)
used_edges = set()   # список помеченных рёбер (R'i из лекции)
components = []      # найденные компоненты связности

# Внешний цикл: каждый запуск из непосещённой вершины = новая компонента
for start in graph:
    if start in visited:
        continue

    stack = [start]      # стэк активных вершин
    visited.add(start)
    component = [start]

    while stack:
        current = stack[-1]   # текущая вершина — вершина стека (не убираем)
        found = False

        # Просмотр рёбер: ищем первое непомеченное ребро
        for neighbor, edge_id in graph[current]:
            if edge_id not in used_edges:
                used_edges.add(edge_id)   # помечаем ребро
                found = True
                if neighbor not in visited:
                    # Шаг вперёд: помечаем вершину и углубляемся
                    visited.add(neighbor)
                    stack.append(neighbor)
                    component.append(neighbor)
                break   # берём только ОДНО ребро за раз — это и делает обход "в глубину"

        if not found:
            # Шаг назад: непомеченных рёбер нет — возвращаемся
            stack.pop()

    components.append(component)   # стек пуст — компонента собрана

for c in components:
    print(c)
'''
