import math


def dist(p1, p2):
    """Расстояние между двумя точками."""
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def closest_pair(points):
    if len(points) < 2:
        return float('inf')

    points_sorted = sorted(points, key=lambda p: p[0])  # по X

    def _rec(px, py):
        n = len(px)

        # --- базовые случаи ---
        if n == 2:
            return dist(px[0], px[1])
        if n == 3:
            return min(
                dist(px[0], px[1]),
                dist(px[1], px[2]),
                dist(px[0], px[2]),
            )

        # --- делим ---
        mid = n // 2
        mid_x = px[mid][0]

        left_x = px[:mid]
        right_x = px[mid:]

        # Делим по Y, сохраняя порядок — O(n)
        left_set = set(left_x)
        left_y = [p for p in py if p in left_set]
        right_y = [p for p in py if p not in left_set]

        d_left = _rec(left_x, left_y)
        d_right = _rec(right_x, right_y)
        d = min(d_left, d_right)

        # --- полоса вокруг разделителя ---
        strip = [p for p in py if abs(p[0] - mid_x) < d]

        # Внутри полосы у каждой точки не больше 7 соседей
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < d:
                d = min(d, dist(strip[i], strip[j]))
                j += 1

        return d

    py = sorted(points_sorted, key=lambda p: p[1])
    return _rec(points_sorted, py)


if __name__ == "__main__":
    pts = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(f"Минимальное расстояние: {closest_pair(pts):.4f}")
