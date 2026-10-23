"""Build the final TriWeb logo package (SVG outlines + PNG + vector PDF) from the Nudo mark."""
import sys, pathlib, re
sys.path.insert(0, '/home/claude/triweb/logo'); sys.path.insert(0, '/home/claude/triweb/brand'); sys.path.insert(0, '/home/claude/triweb')
from nudo import mark_path, seed_path, BBOX, CY
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen
from outline import text_path

OUT = pathlib.Path('/home/claude/triweb/logo/TriWeb-logo'); OUT.mkdir(exist_ok=True)
NEGRO, CREMA, VERDE = '#0B0B0C', '#F2ECDD', '#22C55E'
MARK = mark_path()
SEED = seed_path()
WITH_SEED = '--sin-semilla' not in sys.argv

MW, MH = BBOX[2] - BBOX[0], BBOX[3] - BBOX[1]

_F = TTFont('/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf'); _GS = _F.getGlyphSet(); _UPM = _F['head'].unitsPerEm
def _ibounds():
    g = _F.getBestCmap()[0x131]; bp = BoundsPen(_GS); _GS[g].draw(bp); return bp.bounds  # xmin, ymin, xmax, ymax
def seed_mark(cx, top, width, color=None):
    """Seed triangle scaled to `width`, flat side at y=`top`, centred on cx."""
    sc = width / 37.5
    return f'<path d="{SEED}" fill="{color or VERDE}" transform="translate({cx:.2f} {top + 11.61*sc:.2f}) scale({sc:.4f})"/>'

def wordmark(fg, x, base, size):
    tr = -size*0.015
    if not WITH_SEED:
        a, xe = text_path('Tri', 'InterDisplay-Bold.otf', size, x, base, tr)
        b, xe = text_path('Web', 'InterDisplay-Regular.otf', size, xe, base, tr)
        return f'<path d="{a} {b}" fill="{fg}"/>', xe
    a1, xi = text_path('Tr', 'InterDisplay-Bold.otf', size, x, base, tr)
    a2, xe = text_path('\u0131', 'InterDisplay-Bold.otf', size, xi, base, tr)
    b, xe = text_path('Web', 'InterDisplay-Regular.otf', size, xe, base, tr)
    x0, y0, x1, y1 = _ibounds(); sc = size/_UPM
    stem_c = xi + (x0 + x1)/2*sc; stem_w = (x1 - x0)*sc
    dw = stem_w*1.6; dh = dw*33.26/37.5
    xh = y1*sc                                   # top of the dotless i
    bottom = base - xh - size*0.085              # optical gap above the stem
    dot = seed_mark(stem_c, bottom - dh, dw)
    return f'<path d="{a1} {a2} {b}" fill="{fg}"/>' + dot, xe

def svg(w, h, body, bg=None):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{b}{body}</svg>'

def seedp(col=None): return f'<path d="{SEED}" fill="{col or VERDE}"/>' if WITH_SEED else ''

def symbol(fg, bg=None, pad=24, seed_col=None):
    w, h = MW + 2*pad, MH + 2*pad
    body = f'<g transform="translate({w/2} {h/2 - CY})"><path d="{MARK}" fill="{fg}"/>{seedp(seed_col)}</g>'
    return svg(w, h, body, bg)

def horizontal(fg, mark_col=None, bg=None, pad=24):
    size = 104; cap = size*0.727              # Inter Display cap height ≈ 0.727 em
    gap = 44
    mx = pad + MW/2; my = pad + MH/2
    base = my + cap/2
    wm, xe = wordmark(fg, pad + MW + gap, base, size)
    w, h = xe + pad, MH + 2*pad
    body = f'<g transform="translate({mx} {my - CY})"><path d="{MARK}" fill="{mark_col or fg}"/>{seedp()}</g>' + wm
    return svg(w, h, body, bg)

def vertical(fg, mark_col=None, bg=None, pad=40):
    size = 92; cap = size*0.727
    wtmp, xe = wordmark(fg, 0, 0, size); tw = xe
    w = max(MW, tw) + 2*pad; gap = 46
    h = pad + MH + gap + cap + pad
    mx, my = w/2, pad + MH/2
    wm, _ = wordmark(fg, (w - tw)/2, pad + MH + gap + cap, size)
    body = f'<g transform="translate({mx} {my - CY})"><path d="{MARK}" fill="{mark_col or fg}"/>{seedp()}</g>' + wm
    return svg(w, h, body, bg)

def avatar(fg, bg, size=1080, frac=0.52):
    s = size*frac/max(MW, MH)
    body = f'<g transform="translate({size/2} {size/2}) scale({s:.4f}) translate(0 {-CY})"><path d="{MARK}" fill="{fg}"/>{seedp()}</g>'
    return svg(size, size, body, bg)

files = {
    'triweb-simbolo-negro.svg': symbol(NEGRO),
    'triweb-simbolo-crema.svg': symbol(CREMA),
    'triweb-simbolo-verde.svg': symbol(VERDE, seed_col=NEGRO),
    'triweb-simbolo-sobre-verde.svg': symbol(NEGRO, seed_col=CREMA),
    'triweb-logo-horizontal-negro.svg': horizontal(NEGRO),
    'triweb-logo-horizontal-crema.svg': horizontal(CREMA),
    'triweb-logo-vertical-negro.svg': vertical(NEGRO),
    'triweb-logo-vertical-crema.svg': vertical(CREMA),
    'triweb-avatar.svg': avatar(CREMA, NEGRO),
}
for n, s in files.items(): (OUT / n).write_text(s)

# PNG + vector PDF via headless Chromium
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for n in files:
        src = (OUT / n)
        w, h = map(float, re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', files[n]).groups())
        scale = 1 if n == 'triweb-avatar.svg' else 3
        pg.set_viewport_size({'width': int(w), 'height': int(h)})
        html = f'<html><body style="margin:0;background:transparent">{files[n]}</body></html>'
        pg.set_content(html)
        pg.locator('svg').screenshot(path=str(OUT / n.replace('.svg', '.png')), omit_background=True, scale='device') if scale == 1 else None
        if scale != 1:
            p2 = b.new_page(device_scale_factor=scale, viewport={'width': int(w), 'height': int(h)})
            p2.set_content(html); p2.locator('svg').screenshot(path=str(OUT / n.replace('.svg', '.png')), omit_background=True); p2.close()
        pg.pdf(path=str(OUT / n.replace('.svg', '.pdf')), width=f'{w/96:.3f}in', height=f'{h/96:.3f}in', print_background=True,
               margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}, page_ranges='1')
    b.close()
print('\n'.join(sorted(x.name for x in OUT.iterdir())))
