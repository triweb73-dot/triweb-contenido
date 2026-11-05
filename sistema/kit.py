"""Shared TriWeb brand kit (final identity: Nudo, negro / crema / verde trébol) for rendering Instagram pieces."""
import sys, pathlib
sys.path.insert(0, '/home/claude/triweb/logo')
sys.path.insert(0, '/home/claude/triweb/logo2')
from nudo import mark_path, seed_path, BBOX, CY

NEGRO, CREMA, VERDE, VERDE_TXT = '#0B0B0C', '#F2ECDD', '#22C55E', '#166534'
GRIS, GRIS_D, RAISED_D = '#6F6A60', '#A8A29A', '#18181A'
MARK = mark_path()
SEED = seed_path()
MW, MH = BBOX[2] - BBOX[0], BBOX[3] - BBOX[1]

BASE_CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#777}}
#frame{{position:relative;overflow:hidden;font-family:'Inter',sans-serif;}}
.d{{font-family:'Inter Display','Inter',sans-serif;font-weight:800;letter-spacing:-0.035em;line-height:.98}}
.negro{{background:{NEGRO};color:{CREMA}}}
.crema{{background:{CREMA};color:{NEGRO}}}
.verdebg{{background:{VERDE};color:{NEGRO}}}
.hl{{background:{VERDE};color:{NEGRO};padding:0 .14em;border-radius:.16em;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.vt{{color:{VERDE_TXT}}} .vd{{color:{VERDE}}}
.pill{{display:inline-block;border-radius:999px;padding:14px 30px;font-weight:700;font-size:28px;letter-spacing:.01em}}
.gris{{color:{GRIS}}} .gris-d{{color:{GRIS_D}}}
.handle{{position:absolute;font-size:26px;font-weight:600;letter-spacing:.01em}}
.num{{position:absolute;font-size:26px;font-weight:600}}
"""

def mark_svg(color, size=None, extra='', seed=VERDE):
    """El Nudo NUEVO (logo enviado por Luciano el 2026-11-02) con su semilla verde, caja cuadrada centrada."""
    import nudo_nuevo as N
    x0, y0, x1, y1 = N.BBOX; s = max(x1 - x0, y1 - y0) * 1.04; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    st = f'width="{size}" height="{size}"' if size else 'width="100%" height="100%"'
    return (f'<svg viewBox="{cx-s/2:.1f} {cy-s/2:.1f} {s:.1f} {s:.1f}" {st} {extra}>'
            f'<path d="{N.KNOT}" fill="{color}" fill-rule="evenodd"/>'
            + (f'<path d="{N.SEED}" fill="{seed}" fill-rule="evenodd"/>' if seed else '') + '</svg>')

def page(inner, w=1080, h=1350, cls='', extra_css=''):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{extra_css}</style></head>
<body><div id="frame" class="{cls}" style="width:{w}px;height:{h}px">{inner}</div></body></html>"""

def render(pairs, scale=1):
    """pairs: list of (html_path, png_path)."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(device_scale_factor=scale, viewport={'width': 1200, 'height': 2000})
        for src, out in pairs:
            pg.goto(pathlib.Path(src).resolve().as_uri()); pg.wait_for_timeout(250)
            pg.query_selector('#frame').screenshot(path=str(out))
        b.close()
