# kombin_labs
Лабораторная работа №1 
```Python
import math

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def brute_force(points):
    n = len(points)
    if n < 2:
        return float('inf'), None
    best_d = float('inf')
    best_pair = None
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            if d < best_d:
                best_d = d
                best_pair = (points[i], points[j])
    return best_d, best_pair

def closest_pair(points):
    if len(points) < 2:
        return float('inf'), None

    points_sorted = sorted(points, key=lambda p: p[0])

    def _rec(px, py):
        n = len(px)
        if n <= 3:
            return brute_force(px)

        mid = n // 2
        mid_x = px[mid][0]
        left_x, right_x = px[:mid], px[mid:]

        left_set = set(left_x)
        left_y = [p for p in py if p in left_set]
        right_y = [p for p in py if p not in left_set]

        d_left, pair_left = _rec(left_x, left_y)
        d_right, pair_right = _rec(right_x, right_y)

        if d_left < d_right:
            d, best_pair = d_left, pair_left
        else:
            d, best_pair = d_right, pair_right

        strip = [p for p in py if abs(p[0] - mid_x) < d]

        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < d:
                d_new = dist(strip[i], strip[j])
                if d_new < d:
                    d = d_new
                    best_pair = (strip[i], strip[j])
                j += 1
        return d, best_pair

    py = sorted(points_sorted, key=lambda p: p[1])
    return _rec(points_sorted, py)


if __name__ == "__main__":
    data = [
        (0, 16), (31, 10), (25, 11), (44, 21), (33, 25),
        (3, 10), (4, 28), (6, 66), (3, 12), (6, 6),
        (8, 11), (7, 22), (21, 14), (71, 0), (61, 12)
    ]

    min_d, pair = closest_pair(data)
    print(f"Минимальное расстояние: {min_d}")
    print(f"Точки: {pair}")
```
### Вывод
<img width="1072" height="421" alt="image" src="https://github.com/user-attachments/assets/38d13778-cc31-49a0-ae01-ab78e18baf4c" />

