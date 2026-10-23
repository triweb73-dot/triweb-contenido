import sys, pathlib, subprocess, shutil
sys.path.insert(0, '/home/claude/triweb')
from kit import *

OUT = pathlib.Path('/home/claude/triweb/semana1')
FPS = 30

ANIM_JS = """
<script>
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
function render(t){
  document.querySelectorAll('[data-in]').forEach(el=>{
    const a=+el.dataset.in, b=el.dataset.out?+el.dataset.out:1e9, d=.45;
    let o=ease((t-a)/d); if(t>b) o=1-ease((t-b)/.3);
    el.style.opacity=o; el.style.transform=`translateY(${(1-Math.min(1,ease((t-a)/d)))*60}px)`;
  });
  document.querySelectorAll('[data-draw]').forEach(el=>{
    const a=+el.dataset.draw, L=+el.dataset.len; const p=ease((t-a)/.6);
    el.style.strokeDasharray=L+" "+(L+10); el.style.strokeDashoffset=L*(1-p); el.style.opacity=t>=a?1:0;
  });
}
render(0);
</script>"""

def scene(css_cls, inner):
    return page(inner + ANIM_JS, 1080, 1920, css_cls,
                extra_css='.c{position:absolute;left:96px;right:96px} [data-in]{opacity:0} .c.d{line-height:1.08}')

def footer(dark=True):
    col = GRIS_D if dark else GRIS
    return f'<div class="handle" style="left:96px;bottom:150px;color:{col}">@triweb_73</div>'

# Reel A: the 5-second test (15 s)
big = lambda txt, a, b, top, size=120, extra='': f'<div class="c d" data-in="{a}" data-out="{b}" style="top:{top}px;font-size:{size}px;{extra}">{txt}</div>'
small = lambda txt, a, b, top: f'<div class="c" data-in="{a}" data-out="{b}" style="top:{top}px;font-size:48px;line-height:1.3;color:{GRIS_D}">{txt}</div>'
count = ''.join(f'<div class="c d" data-in="{4.2+i*.5}" data-out="{4.2+i*.5+.45}" style="top:640px;font-size:520px;text-align:center;color:{[CREMA,CREMA,CREMA,CREMA,VERDE][i]}">{5-i}</div>' for i in range(5))
reel_a = scene('negro', f'''
{big('¿Tu web pasa la prueba de los <span class="hl">5 segundos</span>?', .2, 2.6, 560)}
{big('Entrá a tu web desde el celular.', 2.9, 4.0, 640, 112)}
{small('y contá hasta cinco', 3.2, 4.0, 980)}
{count}
{big('¿Ya sabés qué vende,', 6.9, 10.3, 520, 104)}
{big('dónde está', 7.6, 10.3, 740, 104, f'color:{VERDE}')}
{big('y cómo escribirle?', 8.3, 10.3, 860, 104)}
{big('Si no, estás <span class="hl">perdiendo clientes</span>.', 10.6, 12.6, 620, 120)}
<div class="c" data-in="12.9" style="top:520px"><div style="width:180px;height:180px">{mark_svg(CREMA, 180)}</div></div>
{big('Trabajemos juntos.', 13.1, 99, 760, 112)}
<div class="c" data-in="13.6" style="top:1040px"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:44px;padding:26px 52px"><b>Consultanos</b> · Trabajemos juntos</span></div>
{footer()}''')

# Reel B: the Nudo draws itself, one strand per service (11 s)
import math, nudo
SC, CX, CY0 = 4.4, 540, 760
_runs = nudo.runs(24, 18*1.12)
def _strand(run, a):
    pts = [(CX + x*SC, CY0 + (y - nudo.CY)*SC) for x, y in run]
    L = sum(math.dist(pts[k], pts[k+1]) for k in range(len(pts)-1))
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
    return (f'<path d="{d}" fill="none" stroke="{CREMA}" stroke-width="{18*SC:.0f}" stroke-linecap="butt" stroke-linejoin="round" '
            f'data-draw="{a}" data-len="{L:.0f}" style="stroke-dasharray:{L:.0f};stroke-dashoffset:{L:.0f}"/>')
_seed = f'<path d="{SEED}" fill="{VERDE}" transform="translate({CX} {CY0 - nudo.CY*SC:.1f}) scale({SC})"/>'
knot = (f'<svg width="1080" height="1920" style="position:absolute;left:0;top:0">'
        + ''.join(_strand(r, a) for r, a in zip(_runs, (.4, 2.4, 4.4)))
        + f'<g data-in="6.4">{_seed}</g></svg>')
lab = lambda txt, sub, a, b: (f'<div class="c d" data-in="{a}" data-out="{b}" style="top:1280px;font-size:120px;text-align:center">{txt}</div>'
                              f'<div class="c" data-in="{a+.2}" data-out="{b}" style="top:1430px;font-size:46px;text-align:center;color:{GRIS_D}">{sub}</div>')
reel_b = scene('negro', f'''{knot}
{lab('Web', 'sitios rápidos que venden', .5, 2.2)}
{lab('Diseño', 'logo, marca y piezas', 2.5, 4.2)}
{lab('Video', 'reels y edición', 4.5, 6.2)}
<div class="c d" data-in="6.6" style="top:1250px;font-size:112px;text-align:center">3 servicios.<br><span class="hl">1 solo equipo.</span></div>
<div class="c" data-in="8.0" style="top:1560px;text-align:center"><span class="pill" style="background:{CREMA};color:{NEGRO};font-size:42px;padding:24px 48px"><b>Consultanos</b> · Trabajemos juntos</span></div>
{footer()}''')

def make(name, html, secs):
    d = OUT / name; fr = d / 'frames'; shutil.rmtree(fr, ignore_errors=True); fr.mkdir(parents=True)
    h = d / 'reel.html'; h.write_text(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(h.resolve().as_uri()); pg.wait_for_timeout(300)
        el = pg.query_selector('#frame')
        for i in range(int(secs * FPS)):
            pg.evaluate(f'render({i/FPS})')
            el.screenshot(path=str(fr / f'{i:04d}.jpg'), type='jpeg', quality=92)
        b.close()
    mp4 = d / f'triweb-{name}.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', str(fr / '%04d.jpg'),
                    '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest',
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-crf', '20', '-movflags', '+faststart',
                    '-c:a', 'aac', '-b:a', '128k', str(mp4)], check=True)
    # cover frame for the feed
    shutil.copy(fr / f'{int(FPS*1.8):04d}.jpg', d / f'triweb-{name}-portada.jpg')
    shutil.rmtree(fr)
    print('ok', mp4)

if __name__ == '__main__':
    which = sys.argv[1:] or ['2-reel-prueba-5-segundos', '4-reel-tres-servicios']
    if '2-reel-prueba-5-segundos' in which: make('2-reel-prueba-5-segundos', reel_a, 15)
    if '4-reel-tres-servicios' in which: make('4-reel-tres-servicios', reel_b, 11)
