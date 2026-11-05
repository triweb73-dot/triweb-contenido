"""Semana del 2/11: 4 reels distintos entre sí (formato, layout, ritmo y música), con la paleta y el Nudo nuevo."""
import sys, pathlib, subprocess, shutil
sys.path.insert(0, '/home/claude/triweb'); sys.path.insert(0, '/home/claude/triweb/semana1')
from kit import *

OUT = pathlib.Path('/home/claude/triweb/semana3/out'); OUT.mkdir(parents=True, exist_ok=True)
FPS = 30; M = 96
SRC = 'file:///home/claude/triweb/sura/src/'

JS = """<script>
const cl=x=>x<0?0:x>1?1:x, ease=x=>1-Math.pow(1-cl(x),3), back=x=>{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
function out(el,t){const b=el.dataset.out?+el.dataset.out:1e9;return t>b?1-ease((t-b)/.25):1}
function render(t){
 document.querySelectorAll('[data-in]').forEach(el=>{const a=+el.dataset.in,p=ease((t-a)/.4);
   el.style.opacity=p*out(el,t); el.style.transform=`translateY(${(1-p)*50}px)`;});
 document.querySelectorAll('[data-left]').forEach(el=>{const a=+el.dataset.left,p=ease((t-a)/.35);
   el.style.opacity=p*out(el,t); el.style.transform=`translateX(${(1-p)*-140}px)`;});
 document.querySelectorAll('[data-pop]').forEach(el=>{const a=+el.dataset.pop,p=back((t-a)/.4);
   el.style.transform=`scale(${Math.max(0,p)})`; el.style.opacity=(t>=a?1:0)*out(el,t);});
 document.querySelectorAll('[data-grow]').forEach(el=>{const a=+el.dataset.grow,p=ease((t-a)/.35);
   el.style.transformOrigin='left center'; el.style.transform=`scaleX(${p})`; el.style.opacity=(p>0?1:0)*out(el,t);});
 document.querySelectorAll('[data-wipe]').forEach(el=>{const a=+el.dataset.wipe,p=ease((t-a)/.3);
   el.style.clipPath=`inset(0 ${100-p*100}% 0 0)`; el.style.opacity=(t>=a?1:0)*out(el,t);});
 document.querySelectorAll('[data-scene]').forEach(el=>{const [a,b]=el.dataset.scene.split(',').map(Number);
   el.style.opacity=(t>=a&&t<b)?1:0;});
 document.querySelectorAll('[data-zoom]').forEach(el=>{const [a,b,s0,s1]=el.dataset.zoom.split(',').map(Number),p=cl((t-a)/(b-a));
   el.style.transform=`scale(${s0+(s1-s0)*p})`;});
 const f=document.getElementById('frame'); let sh=0;
 document.querySelectorAll('[data-shake]').forEach(el=>{const a=+el.dataset.shake; if(t>=a&&t<a+.22){sh=Math.max(sh,1-(t-a)/.22);}});
 f.style.transform=sh?`translate(${Math.sin(t*90)*14*sh}px,${Math.cos(t*70)*10*sh}px)`:'';
}
render(0);
</script>"""
CSS = ('.c{position:absolute;left:96px;right:96px} [data-in],[data-pop],[data-grow],[data-wipe],[data-left]{opacity:0} '
       '.c.d{line-height:1.04} img{display:block}')

def scene(inner, cls='negro'):
    return page(inner + JS, 1080, 1920, cls, extra_css=CSS)

def pill(txt, bg, fg, size=44):
    return f'<span class="pill" style="background:{bg};color:{fg};font-size:{size}px;padding:26px 52px">{txt}</span>'

def ending(a, line, dark=True):
    bg, fg = (NEGRO, CREMA) if dark else (CREMA, NEGRO)
    return (f'<div style="position:absolute;inset:0;background:{bg}" data-in="{a}"></div>'
            f'<div style="position:absolute;left:50%;top:520px;margin-left:-170px;width:340px;height:340px" data-pop="{a+.15}">{mark_svg(fg, 340)}</div>'
            f'<div class="c d" data-in="{a+.5}" style="top:960px;font-size:92px;text-align:center;color:{fg}">{line}</div>'
            f'<div class="c" data-in="{a+.9}" style="top:1250px;text-align:center">{pill("<b>Consultanos</b> · Trabajemos juntos", VERDE, NEGRO)}</div>'
            f'<div class="c" data-in="{a+.9}" style="top:1400px;text-align:center;font-size:34px;color:{GRIS_D if dark else GRIS}">@triweb_73</div>')

def handle(dark=True):
    return (f'<div style="position:absolute;left:96px;bottom:360px;display:flex;align-items:center;gap:14px">'
            f'{mark_svg(CREMA if dark else NEGRO, 56)}<span style="font-size:28px;font-weight:600;color:{GRIS_D if dark else GRIS}">@triweb_73</span></div>')

# ---------------- R1 · Martes · Web · MITO vs VERDAD (crema, funk) ----------------
MYTHS = [('Una web es carísima.', 'Un rediseño arranca <span class="hl">desde $197.000</span>.'),
         ('Con Instagram me alcanza.', 'Cuando te buscan en Google, aparece tu <span class="hl">web</span>.'),
         ('Hacer una web tarda meses.', 'Una landing page está lista en <span class="hl">7 días hábiles</span>.')]
def myth(i, a, m, v):
    b = a + 3.7
    return (f'<div class="c" data-in="{a}" data-out="{b}" style="top:330px;font-size:34px;font-weight:700;letter-spacing:.1em;color:{GRIS}">MITO {i+1}/3</div>'
            f'<div class="c" data-in="{a}" data-out="{b}" style="top:400px"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:34px">MITO</span></div>'
            f'<div class="c d" data-in="{a+.15}" data-out="{b}" style="top:520px;font-size:104px;color:{GRIS}">{m}'
            f'<div data-grow="{a+1.1}" data-out="{b}" style="position:absolute;left:-10px;right:-10px;top:27%;height:14px;background:{VERDE};border-radius:7px"></div>'
            f'<div data-grow="{a+1.3}" data-out="{b}" style="position:absolute;left:-10px;right:30%;top:77%;height:14px;background:{VERDE};border-radius:7px"></div></div>'
            f'<div class="c" data-pop="{a+1.6}" data-out="{b}" style="top:960px"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:34px">VERDAD</span></div>'
            f'<div class="c d" data-left="{a+1.8}" data-out="{b}" data-shake="{a+1.6}" style="top:1080px;font-size:96px">{v}</div>')
r1 = scene(f'''
<div class="c d" data-in=".15" data-out="2.5" style="top:560px;font-size:132px">3 mitos que te frenan de tener <span class="hl">web</span>.</div>
<div class="c" data-in=".6" data-out="2.5" style="top:1060px;font-size:44px;color:{GRIS}">El tercero es el más común.</div>
{''.join(myth(i, 2.7 + i*4.0, m, v) for i, (m, v) in enumerate(MYTHS))}
{handle(False)}
{ending(14.7, 'Tu web, más cerca<br>de lo que pensás.', dark=False)}''', 'crema')

# ---------------- R2 · Jueves · CM · POV con celular (negro, lo-fi) ----------------
PX, PY, PW, PH = 250, 560, 580, 1000
def tile_grid(a, filled):
    out = ''
    for k in range(9):
        x, y = PX + 30 + (k % 3)*178, PY + 300 + (k//3)*178
        col = RAISED_D if k >= filled else ['#2A2A2E', '#34343A', '#2A2A2E'][k % 3]
        out += f'<div data-pop="{a + k*.05:.2f}" data-out="4.3" style="position:absolute;left:{x}px;top:{y}px;width:168px;height:168px;background:{col};border-radius:8px"></div>'
    return out
cal = ''
for k in range(28):
    x, y = 150 + (k % 7)*116, 760 + (k//7)*116
    on = k % 7 not in (6,)  # todos los días menos uno de descanso en la grilla visual
    cal += f'<div data-pop="{4.9 + k*.07:.2f}" data-out="9.6" style="position:absolute;left:{x}px;top:{y}px;width:100px;height:100px;border-radius:18px;background:{RAISED_D}">' \
           + (f'<div style="position:absolute;left:34px;top:34px;width:32px;height:32px;border-radius:50%;background:{VERDE}"></div>' if on else '') + '</div>'
chips = ''.join(f'<div class="c" data-left="{7.2 + i*.35:.2f}" data-out="9.6" style="top:{1290 + (i//2)*110}px;left:{150 + (i%2)*410}px;right:auto">'
                f'<span class="pill" style="background:{CREMA};color:{NEGRO};font-size:36px">{t}</span></div>'
                for i, t in enumerate(['Planificar', 'Diseñar', 'Responder', 'Medir']))
r2 = scene(f'''
<div class="c d" data-in=".15" data-out="4.3" style="top:250px;font-size:96px">POV: publicás<br><span class="hl">cuando hay tiempo</span>.</div>
<div data-in=".5" data-out="4.3" style="position:absolute;left:{PX}px;top:{PY}px;width:{PW}px;height:{PH}px;border-radius:60px;background:#151517;box-shadow:0 0 0 12px #26262A"></div>
<div data-in=".7" data-out="4.3" style="position:absolute;left:{PX+40}px;top:{PY+70}px;display:flex;gap:24px;align-items:center">
  <div style="width:130px;height:130px;border-radius:50%;background:#26262A"></div>
  <div style="font-size:30px;color:{GRIS_D};line-height:1.5">tu_negocio<br><b style="color:{CREMA}">3</b> publicaciones</div></div>
{tile_grid(.9, 3)}
<div data-pop="2.4" data-out="4.3" style="position:absolute;left:150px;top:1440px;background:{CREMA};color:{NEGRO};border-radius:28px;padding:26px 34px;font-size:36px;font-weight:600">Última publicación: hace 47 días</div>
<div data-pop="3.1" data-out="4.3" style="position:absolute;right:150px;top:1560px;background:{RAISED_D};color:{GRIS_D};border-radius:28px;padding:22px 30px;font-size:32px">0 mensajes nuevos</div>
<div class="c d" data-in="4.6" data-out="9.6" style="top:300px;font-size:100px">Con un plan,<br>tu Instagram <span class="hl">no para</span>.</div>
<div class="c" data-in="4.8" data-out="9.6" style="top:640px;font-size:38px;color:{GRIS_D}">Un mes de contenido, organizado de antemano.</div>
{cal}{chips}
<div data-in="9.8" data-out="12.2" style="position:absolute;inset:0;background:{CREMA}"></div>
<div class="c" data-in="10.0" data-out="12.2" style="top:420px;font-size:36px;font-weight:700;letter-spacing:.1em;color:{VERDE_TXT}">CASO REAL · CONCESIONARIA</div>
<div class="c d" data-pop="10.2" data-out="12.2" data-shake="10.2" style="top:560px;font-size:250px;color:{NEGRO}">+1.500</div>
<div class="c d" data-in="10.6" data-out="12.2" style="top:860px;font-size:96px;color:{NEGRO}">seguidores en un año.</div>
<div class="c" data-in="11.0" data-out="12.2" style="top:1120px;font-size:44px;color:{GRIS}">Dalinger Automotores, con nuestro community manager.</div>
{ending(12.3, 'Tu Instagram,<br>al día y vendiendo.')}''')

# ---------------- R3 · Viernes · Branding · "Esto no es una marca" (alterna, cumbia) ----------------
GRID = ['papeleria', 'cartel-obra', 'celular', 'casco', 'local', 'tarjetas']
grid = ''
for k, n in enumerate(GRID):
    x, y = 96 + (k % 2)*456, 520 + (k//2)*456
    grid += (f'<div data-pop="{3.0 + k*.31:.2f}" data-out="5.9" style="position:absolute;left:{x}px;top:{y}px;width:432px;height:432px;border-radius:28px;overflow:hidden;background:#ddd">'
             f'<img src="{SRC}{n}.png" style="width:100%;height:100%;object-fit:cover"></div>')
ITEMS = [('Logo', 'logo-verde'), ('Colores', 'moodboard'), ('Tipografía', 'tarjeta'), ('Aplicaciones', 'local')]
items = ''.join(
    f'<div data-left="{6.5 + i*.62:.2f}" data-out="10.5" style="position:absolute;left:96px;right:96px;top:{560 + i*250}px;height:210px;display:flex;align-items:center;gap:40px;'
    f'background:{RAISED_D};border-radius:32px;padding:0 36px">'
    f'<div class="d" style="font-size:96px;color:{VERDE};width:110px">{i+1}</div>'
    f'<div class="d" style="font-size:80px;flex:1">{t}</div>'
    f'<div style="width:150px;height:150px;border-radius:20px;overflow:hidden"><img src="{SRC}{img}.png" style="width:100%;height:100%;object-fit:cover"></div></div>'
    for i, (t, img) in enumerate(ITEMS))
r3 = scene(f'''
<div class="c d" data-in=".15" data-out="2.5" style="top:300px;font-size:130px">Esto <span class="hl">no</span> es<br>una marca.</div>
<div data-pop=".7" data-out="2.5" style="position:absolute;left:190px;top:760px;width:700px;height:495px;border-radius:32px;overflow:hidden">
  <img src="{SRC}logo-negro.png" style="width:100%;height:100%;object-fit:cover"></div>
<div class="c" data-in="1.3" data-out="2.5" style="top:1320px;font-size:48px;color:{GRIS_D}">Es un logo.</div>
<div data-in="2.6" data-out="5.9" style="position:absolute;inset:0;background:{CREMA}"></div>
<div class="c d" data-in="2.7" data-out="5.9" data-shake="2.7" style="top:290px;font-size:130px;color:{NEGRO}">Esto <span class="hl">sí</span>.</div>
{grid}
<div class="c d" data-in="6.1" data-out="10.5" style="top:270px;font-size:96px">Una marca es<br>un <span class="hl">sistema</span>:</div>
{items}
<div data-in="10.7" data-out="13.0" style="position:absolute;inset:0;background:{CREMA}"></div>
<div class="c" data-in="10.8" data-out="13.0" style="top:330px;font-size:34px;font-weight:700;letter-spacing:.1em;color:{VERDE_TXT}">PROYECTO DE BRANDING</div>
<div class="c d" data-in="10.9" data-out="13.0" style="top:400px;font-size:110px;color:{NEGRO}">Sura<br>Arquitectura</div>
<div data-in="11.2" data-out="13.0" style="position:absolute;left:96px;right:96px;top:740px;height:600px;border-radius:32px;overflow:hidden">
  <img data-zoom="11.2,13.0,1.0,1.12" src="{SRC}collage.png" style="width:100%;height:100%;object-fit:cover"></div>
{ending(13.1, '¿Tu marca habla<br>un solo idioma?')}''')

# ---------------- R4 · Sábado · Video · 3 errores, texto cinético (negro, trap) ----------------
ERR = [('Arrancás con el logo.', 'Arrancá con el problema.'),
       ('Texto chiquito y sin subtítulos.', 'Que se entienda sin sonido.'),
       ('Terminás sin decir qué hacer.', 'Cerrá con un llamado a la acción.')]
def err(i, a, e, f):
    b = a + 3.0
    words = e.split()
    w = ''.join(f'<span data-in="{a + .25 + k*.12:.2f}" data-out="{b}" style="display:inline-block;margin-right:.25em">{x}</span>' for k, x in enumerate(words))
    return (f'<div class="c d" data-pop="{a}" data-out="{b}" data-shake="{a}" style="top:300px;font-size:300px;color:transparent;-webkit-text-stroke:6px {VERDE}">0{i+1}</div>'
            f'<div class="c d" style="top:700px;font-size:110px">{w}</div>'
            f'<div data-wipe="{a+1.4}" data-out="{b}" style="position:absolute;left:0;right:0;top:1130px;height:330px;background:{CREMA}"></div>'
            f'<div class="c" data-in="{a+1.55}" data-out="{b}" style="top:1165px;font-size:34px;font-weight:700;letter-spacing:.1em;color:{VERDE_TXT}">MEJOR ASÍ</div>'
            f'<div class="c d" data-in="{a+1.65}" data-out="{b}" style="top:1225px;font-size:84px;color:{NEGRO}">{f}</div>')
hook_words = '3 errores que hacen que nadie mire tu reel.'.split()
hook = ''.join(f'<span data-in="{.1 + k*.14:.2f}" data-out="2.1" style="display:inline-block;margin-right:.22em">'
               + (f'<span class="hl">{x}</span>' if x in ('nadie',) else x) + '</span>' for k, x in enumerate(hook_words))
r4 = scene(f'''
<div class="c d" data-shake=".1" style="top:520px;font-size:150px">{hook}</div>
{''.join(err(i, 2.3 + i*3.2, e, f) for i, (e, f) in enumerate(ERR))}
{handle()}
{ending(11.9, 'Editamos videos que<br>se miran hasta el final.')}''')

REELS = {  # nombre: (html, duración, segundo para la portada)
    'mitos-web': (r1, 17.3, 1.2),
    'pov-instagram': (r2, 15.0, 2.9),
    'esto-no-es-una-marca': (r3, 15.8, 1.6),
    'errores-reel': (r4, 14.6, 1.6),
}

def make(name):
    html, secs, cover = REELS[name]
    d = OUT / name; fr = d / 'frames'; shutil.rmtree(fr, ignore_errors=True); fr.mkdir(parents=True)
    h = d / 'reel.html'; h.write_text(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(h.resolve().as_uri()); pg.wait_for_timeout(600)
        for i in range(int(secs * FPS)):
            pg.evaluate(f'render({i/FPS})')
            pg.screenshot(path=str(fr / f'{i:04d}.jpg'), type='jpeg', quality=90, clip={'x': 0, 'y': 0, 'width': 1080, 'height': 1920})
        b.close()
    mp4 = d / f'triweb-{name}.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', str(fr / '%04d.jpg'),
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-crf', '20', '-movflags', '+faststart', str(mp4)], check=True)
    shutil.copy(fr / f'{int(FPS*cover):04d}.jpg', d / f'triweb-{name}-portada.jpg')
    shutil.rmtree(fr); print('ok', mp4)

if __name__ == '__main__':
    for n in (sys.argv[1:] or REELS): make(n)
