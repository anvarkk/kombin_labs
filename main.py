import math


def d(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def closest(pts):
    if len(pts) < 2:
        return float('inf')

    px = sorted(pts)
    py = sorted(pts, key=lambda p: p[1])

    def go(px, py):
        n = len(px)
        if n == 2:
            return d(px[0], px[1])
        if n == 3:
            a, b, c = px
            return min(d(a, b), d(b, c), d(a, c))

        m = n // 2
        mx = px[m][0]

        lx, rx = px[:m], px[m:]

        lset = set(lx)
        ly = [p for p in py if p in lset]
        ry = [p for p in py if p not in lset]

        dl = go(lx, ly)
        dr = go(rx, ry)
        best = dl if dl < dr else dr

        strip = [p for p in py if abs(p[0] - mx) < best]

        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and strip[j][1] - strip[i][1] < best:
                dd = d(strip[i], strip[j])
                if dd < best:
                    best = dd
                j += 1

        return best

    return go(px, py)


pts = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest(pts))
