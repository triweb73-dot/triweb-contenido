"""Three service motion-graphics reels for TriWeb (1080x1920, 30 fps), rendered frame by frame."""
import sys, pathlib, subprocess, shutil
sys.path.insert(0, '/home/claude/triweb')
from kit import *

OUT = pathlib.Path('/home/claude/triweb/semana1/motion'); OUT.mkdir(exist_ok=True)
FPS = 30; M = 96

JS = """<script>
const cl=x=>x<0?0:x>1?1:x, ease=x=>1-Math.pow(1-cl(x),3), back=x=>{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
function out(el,t){const b=el.dataset.out?+el.dataset.out:1e9;return t>b?1-ease((t-b)/.3):1}
function render(t){
 document.querySelectorAll('[data-in]').forEach(el=>{const a=+el.dataset.in,p=ease((t-a)/.45);
   el.style.opacity=p*out(el,t); el.style.transform=`translateY(${(1-p)*50}px)`;});
 document.querySelectorAll('[data-grow]').forEach(el=>{const a=+el.dataset.grow,p=ease((t-a)/.5);
   el.style.transformOrigin='left center'; el.style.transform=`scaleX(${p})`; el.style.opacity=(p>0?1:0)*out(el,t);});
 document.querySelectorAll('[data-pop]').forEach(el=>{const a=+el.dataset.pop,p=back((t-a)/.45);
   el.style.transform=`scale(${Math.max(0,p)})`; el.style.opacity=(t>=a?1:0)*out(el,t);});
 document.querySelectorAll('[data-type]').forEach(el=>{const a=+el.dataset.type,s=el.dataset.text,n=Math.floor(cl((t-a)/.8)*s.length);
   el.textContent=s.slice(0,n); el.style.opacity=(t>=a?1:0)*out(el,t);});
 document.querySelectorAll('[data-move]').forEach(el=>{const [a,b,x0,x1]=el.dataset.move.split(',').map(Number),p=cl((t-a)/(b-a));
   el.style.left=(x0+(x1-x0)*p)+'px'; el.style.opacity=t>=a?1:0;});
 document.querySelectorAll('[data-scene]').forEach(el=>{const [a,b]=el.dataset.scene.split(',').map(Number);
   el.style.opacity=(t>=a&&t<b)?1:0;});
}
render(0);
</script>"""

CSS = '.c{position:absolute;left:96px;right:96px} [data-in],[data-grow],[data-pop],[data-type]{opacity:0} .c.d{line-height:1.04}'

def scene(inner, cls='negro'):
    return page(inner + JS, 1080, 1920, cls, extra_css=CSS)

def kicker(txt, a, top=250):
    return f'<div class="c" data-in="{a}" style="top:{top}px;font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:{VERDE}">{txt}</div>'

def title(txt, a, top=310, size=104, b=None):
    o = f' data-out="{b}"' if b else ''
    return f'<div class="c d" data-in="{a}"{o} style="top:{top}px;font-size:{size}px">{txt}</div>'

def ending(a, line):
    return (f'<div style="position:absolute;inset:0;background:{NEGRO}" data-in="{a}"></div>'
            f'<div style="position:absolute;left:50%;top:560px;margin-left:-180px;width:360px;height:360px" data-pop="{a+.2}">{mark_svg(CREMA, 360)}</div>'
            f'<div class="c d" data-in="{a+.6}" style="top:1010px;font-size:96px;text-align:center">{line}</div>'
            f'<div class="c" data-in="{a+1.1}" style="top:1290px;text-align:center"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:44px;padding:26px 52px"><b>Consultanos</b> · Trabajemos juntos</span></div>'
            f'<div class="c" data-in="{a+1.1}" style="top:1440px;text-align:center;font-size:34px;color:{GRIS_D}">@triweb_73</div>')

def label(txt, a, top, side='left'):
    pos = f'left:{M}px' if side == 'left' else f'right:{M}px'
    return (f'<div data-pop="{a}" style="position:absolute;{pos};top:{top}px;background:{CREMA};color:{NEGRO};border-radius:999px;'
            f'padding:16px 28px;font-size:30px;font-weight:700;box-shadow:0 0 0 6px {NEGRO}">{txt}</div>')

# ---------- 1. Desarrollo web ----------
PX, PY, PW, PH = 290, 620, 500, 820   # phone frame
def blk(x, y, w, h, a, col=RAISED_D, r=14, kind='grow'):
    return f'<div data-{kind}="{a}" style="position:absolute;left:{PX+x}px;top:{PY+y}px;width:{w}px;height:{h}px;border-radius:{r}px;background:{col}"></div>'
web = scene(f'''
{kicker('Desarrollo web', .2)}
{title('Tu web, lista<br>para <span class="hl">vender</span>.', .35)}
<div data-pop="1.0" style="position:absolute;left:{PX}px;top:{PY}px;width:{PW}px;height:{PH}px;border-radius:56px;background:{CREMA};box-shadow:0 0 0 14px #26262A"></div>
{blk(36, 46, 120, 26, 1.5, NEGRO, 13)}{blk(PW-36-60, 46, 60, 26, 1.6, NEGRO, 13)}
{blk(36, 110, PW-72, 300, 1.9, NEGRO, 26, 'pop')}
<div data-in="2.3" style="position:absolute;left:{PX+70}px;top:{PY+170}px;width:{PW-140}px;font-family:'Inter Display';font-weight:800;font-size:48px;line-height:1.02;color:{CREMA};letter-spacing:-.03em">Pastelería<br>Don Julio</div>
{blk(70, 330, 150, 22, 2.6, VERDE, 11)}
{blk(36, 440, PW-72, 22, 2.9, '#D8D1C0', 11)}{blk(36, 476, PW-160, 22, 3.0, '#D8D1C0', 11)}
{blk(36, 540, (PW-90)/2, 170, 3.3, '#E4DDCC', 20, 'pop')}{blk(54+(PW-90)/2, 540, (PW-90)/2, 170, 3.45, '#E4DDCC', 20, 'pop')}
<div data-pop="3.9" style="position:absolute;left:{PX+36}px;top:{PY+700}px;width:{PW-72}px;height:86px;border-radius:999px;background:{VERDE};color:{NEGRO};display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:800">Pedí por WhatsApp</div>
{label('Carga rápida', 4.6, 760, 'left')}
{label('Perfecta en el celular', 5.2, 1180, 'right')}
{label('Directo a WhatsApp', 5.8, 1480, 'left')}
{ending(9.4, 'Webs que traen<br>consultas.')}''')

# ---------- 2. Diseño y branding ----------
G = 24; CW = (1080 - 2*M - G)//2; CH = 430; Y0 = 640
def card(i, a, inner, bg=RAISED_D):
    x = M + (i % 2)*(CW + G); y = Y0 + (i//2)*(CH + G)
    return (f'<div data-pop="{a}" style="position:absolute;left:{x}px;top:{y}px;width:{CW}px;height:{CH}px;border-radius:32px;background:{bg};overflow:hidden">{inner}</div>')
cap = lambda t, col=GRIS_D: f'<div style="position:absolute;left:32px;bottom:28px;font-size:30px;font-weight:700;color:{col}">{t}</div>'
logo_demo = (f'<svg viewBox="0 0 200 200" width="230" height="230" style="position:absolute;left:{(CW-230)//2}px;top:70px">'
             f'<circle cx="80" cy="100" r="56" fill="none" stroke="{CREMA}" stroke-width="18"/>'
             f'<rect x="96" y="44" width="96" height="112" rx="48" fill="{VERDE}"/></svg>')
sw = ''.join(f'<div data-grow="{2.4+k*.15}" style="position:absolute;left:32px;top:{60+k*72}px;width:{CW-64}px;height:56px;border-radius:16px;background:{c}"></div>'
             for k, c in enumerate([CREMA, VERDE, '#3A3A40', '#8B7355']))
brand = scene(f'''
{kicker('Diseño y branding', .2)}
{title('Una marca que<br>se <span class="hl">recuerda</span>.', .35)}
{card(0, 1.2, logo_demo + cap('Logo'))}
{card(1, 2.1, sw + cap('Colores'))}
{card(2, 3.0, f'<div style="position:absolute;left:32px;top:40px;font-family:Inter Display;font-weight:800;font-size:200px;letter-spacing:-.05em;color:{NEGRO}">Aa</div>' + cap('Tipografía', GRIS), CREMA)}
{card(3, 3.9, f'<div data-pop="4.3" style="position:absolute;left:44px;top:60px;width:{CW-88}px;height:150px;border-radius:14px;background:{CREMA};transform:rotate(-4deg)"></div>'
            f'<div data-pop="4.6" style="position:absolute;left:84px;top:150px;width:{CW-150}px;height:150px;border-radius:14px;background:{VERDE};transform:rotate(3deg)"></div>' + cap('Piezas'))}
<div class="c" data-in="5.2" data-out="9.2" style="top:1560px;font-size:40px;line-height:1.3;color:{GRIS_D}">Logo, colores, tipografía y piezas que hablan el mismo idioma.</div>
{ending(9.4, 'Marcas que se ven<br>profesionales.')}''')

# ---------- 3. Edición de video ----------
TL_Y = 1110; TX0, TX1 = M, 1080 - M
def clip(track, x, w, a, col):
    return f'<div data-grow="{a}" style="position:absolute;left:{x}px;top:{TL_Y + 70 + track*92}px;width:{w}px;height:72px;border-radius:14px;background:{col}"></div>'
video = scene(f'''
{kicker('Edición de video', .2)}
{title('Videos que se miran<br><span class="hl">hasta el final</span>.', .35, size=92)}
<div data-pop="1.0" style="position:absolute;left:{M}px;top:580px;width:{1080-2*M}px;height:480px;border-radius:32px;background:{RAISED_D};overflow:hidden">
  <div data-scene="1.4,3.6" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:'Inter Display';font-weight:800;font-size:96px;color:{CREMA}">Gancho</div>
  <div data-scene="3.6,5.8" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:'Inter Display';font-weight:800;font-size:96px;color:{CREMA}">Historia</div>
  <div data-scene="5.8,9.4" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:{VERDE};font-family:'Inter Display';font-weight:800;font-size:84px;color:{NEGRO}">Llamado a la acción</div>
</div>
<div data-in="1.2" style="position:absolute;left:{M}px;right:{M}px;top:{TL_Y}px;height:360px;border-radius:24px;background:#151517"></div>
{clip(0, M+20, 300, 1.6, CREMA)}{clip(0, M+330, 260, 2.1, CREMA)}{clip(0, M+600, 268, 2.6, VERDE)}
{clip(1, M+20, 520, 1.9, '#3A3A40')}{clip(1, M+550, 318, 2.4, '#3A3A40')}
{clip(2, M+20, 848, 2.2, '#26413A')}
<div data-move="1.4,9.2,{M+20},{1080-M-24}" style="position:absolute;top:{TL_Y+40}px;width:6px;height:320px;border-radius:3px;background:{VERDE}"></div>
{label('Cortes al ritmo de la música', 4.0, 1510, 'left')}
{ending(9.4, 'Videos que<br>venden por vos.')}''')


# ---------- 4. Community manager ----------
FX, FY, FS, FG = 150, 640, 250, 15   # feed grid
def tile(i, a, bg, inner=''):
    x = FX + (i % 3)*(FS + FG); y = FY + (i//3)*(FS + FG)
    return f'<div data-pop="{a}" style="position:absolute;left:{x}px;top:{y}px;width:{FS}px;height:{FS}px;border-radius:18px;background:{bg};overflow:hidden">{inner}</div>'
_t = lambda txt, col: f'<div style="position:absolute;left:20px;bottom:18px;right:16px;font-family:Inter Display;font-weight:800;font-size:34px;line-height:1;color:{col}">{txt}</div>'
cols = [('#2E2E33', CREMA, 'Tips'), (VERDE, NEGRO, 'Oferta'), (CREMA, NEGRO, 'Caso'),
        (CREMA, NEGRO, 'Reel'), ('#2E2E33', CREMA, 'Equipo'), (VERDE, NEGRO, 'Promo'),
        (VERDE, NEGRO, 'Clientes'), (CREMA, NEGRO, 'Tips'), ('#2E2E33', CREMA, 'Reel')]
grid = ''.join(tile(i, 1.3 + i*.22, bg, _t(t, fg)) for i, (bg, fg, t) in enumerate(cols))
cmreel = scene(f'''
{kicker('Community manager', .2)}
{title('Tu Instagram,<br>al día y <span class="hl">vendiendo</span>.', .35, size=100)}
<div data-in="1.1" style="position:absolute;left:{FX-24}px;top:{FY-24}px;width:{3*FS+2*FG+48}px;height:{3*FS+2*FG+48}px;border-radius:30px;background:{RAISED_D}"></div>
{grid}
{label('Plan mensual de contenido', 3.6, 600, 'right')}
{label('Diseño y textos', 4.2, 1000, 'left')}
{label('Respuestas a mensajes', 4.8, 1330, 'right')}
<div data-in="5.6" data-out="9.2" style="position:absolute;left:{M}px;right:{M}px;top:1480px;background:{CREMA};color:{NEGRO};border-radius:28px;padding:28px 36px">
  <div style="font-family:Inter Display;font-weight:800;font-size:76px;letter-spacing:-.03em">+1.500 seguidores</div>
  <div style="font-size:30px;margin-top:6px;color:{GRIS}">en un año, con una concesionaria que manejamos</div></div>
{ending(9.4, 'Redes que trabajan<br>por tu negocio.')}''', )

def make(name, html, secs, cover_t):
    d = OUT; fr = d / f'frames-{name}'; shutil.rmtree(fr, ignore_errors=True); fr.mkdir(parents=True)
    h = d / f'{name}.html'; h.write_text(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(h.resolve().as_uri()); pg.wait_for_timeout(300)
        el = pg.query_selector('#frame')
        for i in range(int(secs*FPS)):
            pg.evaluate(f'render({i/FPS})')
            el.screenshot(path=str(fr / f'{i:04d}.jpg'), type='jpeg', quality=92)
        b.close()
    mp4 = d / f'triweb-{name}.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', str(fr / '%04d.jpg'),
                    '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                    '-profile:v', 'high', '-crf', '20', '-movflags', '+faststart', '-c:a', 'aac', '-b:a', '128k', str(mp4)], check=True)
    shutil.copy(fr / f'{int(FPS*cover_t):04d}.jpg', d / f'triweb-{name}-portada.jpg')
    shutil.rmtree(fr); h.unlink(); print('ok', mp4.name)

if __name__ == '__main__':
    todo = sys.argv[1:] or ['servicio-web', 'servicio-branding', 'servicio-video', 'servicio-community']
    if 'servicio-web' in todo: make('servicio-web', web, 12, 7.0)
    if 'servicio-branding' in todo: make('servicio-branding', brand, 12, 6.0)
    if 'servicio-video' in todo: make('servicio-video', video, 12, 6.5)
    if 'servicio-community' in todo: make('servicio-community', cmreel, 12, 7.0)
