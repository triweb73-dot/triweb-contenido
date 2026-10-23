"""TriWeb 'Nudo' mark: a trefoil knot drawn as closed outlines with true gaps at the under-crossings."""
import math

f = lambda v: f'{v:.2f}'

def pt(t, k=1.0, rot=0):
    x, y = math.sin(t) + 2*math.sin(2*t), math.cos(t) - 2*math.cos(2*t)
    a = math.radians(rot); c, s = math.cos(a), math.sin(a)
    return (k*(x*c - y*s), k*(x*s + y*c))

def _crossings(n=3000):
    ts = [2*math.pi*i/n for i in range(n)]; P = [pt(t) for t in ts]
    ev = []
    for i in range(n):
        a, b = P[i], P[(i+1) % n]
        for j in range(i+3, n):
            if i == 0 and j == n-1: continue
            c, d = P[j], P[(j+1) % n]
            den = (a[0]-b[0])*(c[1]-d[1]) - (a[1]-b[1])*(c[0]-d[0])
            if abs(den) < 1e-12: continue
            u = ((a[0]-c[0])*(c[1]-d[1]) - (a[1]-c[1])*(c[0]-d[0])) / den
            v = -((a[0]-b[0])*(a[1]-c[1]) - (a[1]-b[1])*(a[0]-c[0])) / den
            if 0 <= u <= 1 and 0 <= v <= 1:
                ev.append(ts[i] + u*2*math.pi/n); ev.append(ts[j] + v*2*math.pi/n)
    return sorted(ev)

EVENTS = _crossings()
UNDER = EVENTS[1::2]   # alternate over/under along the traversal

def runs(k, gap, n=2400):
    """Sample the curve and split it into open runs, cutting a window around each under-crossing."""
    ts = [2*math.pi*i/n for i in range(n)]
    keep = []
    for t in ts:
        cut = False
        for tu in UNDER:
            dt = (t - tu + math.pi) % (2*math.pi) - math.pi
            if abs(dt) < 0.5:
                if math.dist(pt(t, k), pt(tu, k)) < gap: cut = True
        keep.append(not cut)
    # rotate so we start in a kept stretch right after a cut
    start = next(i for i in range(n) if keep[i] and not keep[i-1])
    order = list(range(start, n)) + list(range(0, start))
    out, cur = [], []
    for i in order:
        if keep[i]: cur.append(pt(ts[i], k))
        elif cur: out.append(cur); cur = []
    if cur: out.append(cur)
    return out

def outline(poly, w):
    """Closed outline polygon of an open polyline with flat (butt) ends."""
    h = w/2; L, R = [], []
    for i, p in enumerate(poly):
        a = poly[max(i-1, 0)]; b = poly[min(i+1, len(poly)-1)]
        dx, dy = b[0]-a[0], b[1]-a[1]; m = math.hypot(dx, dy) or 1
        nx, ny = -dy/m, dx/m
        L.append((p[0]+nx*h, p[1]+ny*h)); R.append((p[0]-nx*h, p[1]-ny*h))
    keep = lambda seq: seq[::3] + ([seq[-1]] if (len(seq)-1) % 3 else [])  # decimate, always keep both ends
    pts = keep(L) + keep(R[::-1])
    return 'M' + ' L'.join(f'{f(x)} {f(y)}' for x, y in pts) + ' Z'

# optical centring: the bbox of mark_path() at the defaults is x ±74.7, y -81.0 … 58.5
BBOX = (-74.66, -81.0, 74.66, 58.5)
CY = (BBOX[1] + BBOX[3]) / 2

def mark_path(k=24, w=18, gap=None):
    gap = gap if gap is not None else w*1.12
    return ' '.join(outline(r, w) for r in runs(k, gap))

def mark_svg(color, k=24, w=18, gap=None):
    return f'<path d="{mark_path(k, w, gap)}" fill="{color}"/>'

def seed_path(k=24, w=18, gap=4, bins=360):
    """The central region of the knot, inset by `gap` from the strands: TriWeb's green 'Tri' triangle."""
    S = [pt(2*math.pi*i/6000, k) for i in range(6000)]
    rad = [1e9]*bins
    for x, y in S:
        b = int((math.degrees(math.atan2(y, x)) % 360)/360*bins) % bins
        rad[b] = min(rad[b], math.hypot(x, y))
    pts = []
    for b in range(0, bins, 2):
        r = min(rad[(b+j) % bins] for j in range(-2, 3)) - w/2 - gap
        a = math.radians((b+.5)*360/bins)
        pts.append((r*math.cos(a), r*math.sin(a)))
    return 'M' + ' L'.join(f'{f(x)} {f(y)}' for x, y in pts) + ' Z'
