"""Semana del 9/11: 3 reels nuevos (antes/después, noticia, tutorial), cada uno con layout, ritmo y música propios.
Motor de animación nuevo (slider, máquina de escribir, marquesina, golpes de zoom), Nudo nuevo vía kit.mark_svg."""
import sys, pathlib, subprocess, shutil
sys.path.insert(0, '/home/claude/triweb')
from kit import *

OUT = pathlib.Path('/home/claude/triweb/semana4/out'); OUT.mkdir(parents=True, exist_ok=True)
FPS = 30

JS = """<script>
const cl=x=>x<0?0:x>1?1:x, ease=x=>1-Math.pow(1-cl(x),3), back=x=>{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
function out(el,t){const b=el.dataset.out?+el.dataset.out:1e9;return t>b?1-ease((t-b)/.2):1}
function kf(spec,t){const k=spec.split(';').map(s=>s.split(',').map(Number));
  if(t<=k[0][0])return k[0][1]; for(let i=1;i<k.length;i++){if(t<=k[i][0]){const [a,va]=k[i-1],[b,vb]=k[i];return va+(vb-va)*ease((t-a)/(b-a));}} return k[k.length-1][1];}
function render(t){
 document.querySelectorAll('[data-in]').forEach(el=>{const a=+el.dataset.in,p=ease((t-a)/.35);
   el.style.opacity=p*out(el,t); el.style.transform=`translateY(${(1-p)*40}px)`;});
 document.querySelectorAll('[data-pop]').forEach(el=>{const a=+el.dataset.pop,p=back((t-a)/.35);
   el.style.transform=`scale(${Math.max(0,p)})`; el.style.opacity=(t>=a?1:0)*out(el,t);});
 document.querySelectorAll('[data-punch]').forEach(el=>{const a=+el.dataset.punch,p=ease((t-a)/.22);
   el.style.transform=`scale(${1.6-0.6*p})`; el.style.opacity=(t>=a?Math.min(1,p*2):0)*out(el,t);});
 document.querySelectorAll('[data-swipe]').forEach(el=>{const a=+el.dataset.swipe,p=ease((t-a)/.3),b=el.dataset.out?+el.dataset.out:1e9,q=t>b?ease((t-b)/.3):0;
   el.style.transform=`translateX(${(1-p)*1100 - q*1100}px)`; el.style.opacity=t>=a?1:0;});
 document.querySelectorAll('[data-type]').forEach(el=>{const [a,d]=el.dataset.type.split(',').map(Number),txt=el.dataset.txt,n=Math.floor(txt.length*cl((t-a)/d));
   el.innerHTML=txt.slice(0,n)+((t>=a&&Math.floor(t*3)%2==0)?'<span style="opacity:.6">|</span>':''); el.style.opacity=(t>=a?1:0)*out(el,t);});
 document.querySelectorAll('[data-scene]').forEach(el=>{const [a,b]=el.dataset.scene.split(',').map(Number); el.style.opacity=(t>=a&&t<b)?1:0;});
 document.querySelectorAll('[data-clip]').forEach(el=>{const v=kf(el.dataset.clip,t); el.style.clipPath=`inset(0 0 0 ${v}%)`;});
 document.querySelectorAll('[data-left]').forEach(el=>{el.style.left=kf(el.dataset.left,t)+'%';});
 document.querySelectorAll('[data-zk]').forEach(el=>{el.style.transform=`scale(${kf(el.dataset.zk,t)})`;});
 document.querySelectorAll('[data-wk]').forEach(el=>{el.style.width=kf(el.dataset.wk,t)+'%';});
 document.querySelectorAll('[data-marq]').forEach(el=>{el.style.transform=`translateX(${-(t*+el.dataset.marq)}px)`;});
 document.querySelectorAll('[data-cover]').forEach(el=>{const a=+el.dataset.cover,p=ease((t-a)/.35); el.style.clipPath=`inset(${100-p*100}% 0 0 0)`; el.style.opacity=t>=a?1:0;});
 const f=document.getElementById('frame'); let sh=0;
 document.querySelectorAll('[data-shake]').forEach(el=>{const a=+el.dataset.shake; if(t>=a&&t<a+.2){sh=Math.max(sh,1-(t-a)/.2);}});
 f.style.transform=sh?`translate(${Math.sin(t*95)*12*sh}px,${Math.cos(t*80)*9*sh}px)`:'';
}
render(0);
</script>"""
CSS = ('.c{position:absolute;left:96px;right:96px} [data-in],[data-pop],[data-punch]{opacity:0} img{display:block} '
       '.k{font-size:32px;font-weight:700;letter-spacing:.12em}')

def scene(inner, cls='negro'):
    return page(inner + JS, 1080, 1920, cls, extra_css=CSS + 'body{background:%s}' % (CREMA if cls == 'crema' else NEGRO))

# =============== R5 · Miércoles · TRIAL_REEL · Web · ANTES / DESPUÉS con slider (crema, house) ===============
PX, PY, PW, PH = 260, 580, 560, 1030
def mock_before():
    lines = ''.join(f'<div style="height:10px;margin:9px 24px;background:#C9C3B5;border-radius:4px;width:{w}%"></div>' for w in (88, 80, 92, 70, 85, 60, 90, 76, 82, 66, 88, 72))
    nav = ''.join(f'<span style="font-size:13px;color:#8A857B;margin-right:9px">{x}</span>' for x in ['Inicio', 'Nosotros', 'Productos', 'Galería', 'Novedades', 'Blog', 'Contacto'])
    boxes = ''.join(f'<div style="flex:1;height:110px;background:#D9D3C5;border-radius:6px"></div>' for _ in range(3))
    return (f'<div style="position:absolute;inset:0;background:#EDE8DC">'
            f'<div style="padding:22px 24px 10px;display:flex;flex-wrap:wrap">{nav}</div>'
            f'<div style="margin:6px 24px;height:230px;background:#BDB6A6;border-radius:8px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:19px;font-weight:700;color:#EDE8DC;padding:20px">BIENVENIDOS A NUESTRA PÁGINA WEB OFICIAL</div>'
            f'<div style="display:flex;gap:10px;margin:14px 24px">{boxes}</div>{lines}'
            f'<div style="position:absolute;left:40px;right:40px;top:420px;background:#FFFFFF;border:2px solid #C9C3B5;border-radius:10px;padding:26px;font-size:17px;color:#6F6A60;box-shadow:0 10px 30px rgba(0,0,0,.15)">'
            f'<b>¡Suscribite a nuestro newsletter!</b><div style="height:34px;margin-top:14px;background:#EDE8DC;border-radius:6px"></div><div style="position:absolute;right:12px;top:8px">✕</div></div>'
            f'<div style="position:absolute;left:24px;bottom:30px;font-size:12px;color:#A8A29A">© Todos los derechos reservados</div></div>')
def mock_after():
    prods = ''.join(f'<div style="background:{CREMA};border-radius:18px;height:150px;display:flex;align-items:flex-end;padding:12px;font-size:17px;font-weight:700;color:{NEGRO}">{n}</div>' for n in ['Masa madre', 'Medialunas', 'Budines', 'Tortas'])
    return (f'<div style="position:absolute;inset:0;background:{NEGRO};color:{CREMA}">'
            f'<div style="padding:30px 34px;font-size:20px;font-weight:700;display:flex;justify-content:space-between"><span>Panadería Ejemplo</span><span style="color:{GRIS_D}">☰</span></div>'
            f'<div class="d" style="padding:40px 34px 0;font-size:58px">Pan de masa madre, recién horneado.</div>'
            f'<div style="padding:18px 34px;font-size:21px;color:{GRIS_D}">Pedí hoy, retirá mañana a las 8.</div>'
            f'<div style="margin:16px 34px"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:24px;padding:18px 30px">Pedí por WhatsApp</span></div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:34px 34px">{prods}</div></div>')
# slider: % de la izquierda donde empieza "después" (100 = todo antes, 0 = todo después)
SL = '0,100;2.3,100;2.9,0;4.0,0;4.35,100;4.7,0;6.6,0;6.95,100;7.3,0;9.2,0;9.55,100;9.9,0'
CALL = [(4.7, '1', 'Un solo mensaje,<br>bien grande.', 1330, 40), (7.3, '2', 'El botón para<br>escribirte, a la vista.', 1080, 660), (9.9, '3', 'Nada que tape<br>lo importante.', 1440, 660)]
calls = ''.join(f'<div data-pop="{a}" data-out="12.0" data-shake="{a}" style="position:absolute;left:{x}px;top:{y}px;width:380px;'
                f'background:{NEGRO};color:{CREMA};border-radius:26px;padding:22px 26px;box-shadow:0 20px 40px rgba(0,0,0,.25)">'
                f'<div class="d" style="font-size:40px;color:{VERDE}">{n}</div><div style="font-size:30px;font-weight:600;line-height:1.25;margin-top:6px">{t}</div></div>'
                for i, (a, n, t, y, x) in enumerate(CALL))
r5 = scene(f'''
<div class="c d" data-in=".1" data-out="12.0" style="top:300px;font-size:100px;color:{NEGRO}">Misma web.<br>¿Cuál te <span class="hl">escribe</span>?</div>
<div style="position:absolute;left:{PX-14}px;top:{PY-14}px;width:{PW+28}px;height:{PH+28}px;border-radius:70px;background:{NEGRO}" data-in="0" data-out="12.0"></div>
<div data-in="0" data-out="12.0" style="position:absolute;left:{PX}px;top:{PY}px;width:{PW}px;height:{PH}px;border-radius:58px;overflow:hidden">
  {mock_before()}<div data-clip="{SL}" style="position:absolute;inset:0">{mock_after()}</div>
  <div data-left="{SL}" style="position:absolute;top:0;bottom:0;width:8px;margin-left:-4px;background:{VERDE}"></div></div>
<div data-in=".3" data-out="2.4" style="position:absolute;left:{PX}px;top:{PY+PH+40}px"><span class="pill" style="background:#D9D3C5;color:{NEGRO};font-size:30px">ANTES</span></div>
<div data-in="2.9" data-out="12.0" style="position:absolute;left:{PX}px;top:{PY+PH+40}px"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:30px">DESPUÉS</span></div>
{calls}
<div data-cover="12.1" style="position:absolute;inset:0;background:{NEGRO}"></div>
<div class="c" data-in="12.3" style="top:420px;display:flex;align-items:center;gap:22px">{mark_svg(CREMA, 90)}<span style="font-size:34px;font-weight:600;color:{GRIS_D}">@triweb_73</span></div>
<div class="c d" data-in="12.45" style="top:620px;font-size:110px;color:{CREMA}">¿Tu web es la de <span class="hl">antes</span>?</div>
<div class="c" data-in="12.8" style="top:1000px;font-size:42px;color:{GRIS_D};line-height:1.35">La pasamos a la de después.<br>Diseño web para negocios.</div>
<div class="c" data-in="13.1" style="top:1250px"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:42px;padding:24px 46px"><b>Consultanos</b> · Trabajemos juntos</span></div>
''', 'crema')

# =============== R6 · Viernes · CM · NOTICIA de Instagram (negro, dembow) ===============
marq = ' · '.join(['NOVEDAD INSTAGRAM'] * 14)
TIPS = [(3.5, 'Grabá tu propio producto.', 'No subas el video de otra cuenta.'),
        (5.6, 'Usá la tendencia, con tu marca.', 'La idea se adapta, no se copia.'),
        (7.7, 'Nada de marcas de agua de otras apps.', 'Exportá el video limpio.')]
tips = ''
for i, (a, h, s) in enumerate(TIPS):
    b = a + 2.05
    tips += (f'<div class="c d" data-punch="{a}" data-out="{b}" data-shake="{a}" style="top:520px;font-size:330px;color:{VERDE}">{i+1}</div>'
             f'<div class="c d" data-in="{a+.15}" data-out="{b}" style="top:930px;font-size:100px">{h}</div>'
             f'<div class="c" data-in="{a+.45}" data-out="{b}" style="top:1240px;font-size:46px;color:{GRIS_D}">{s}</div>')
r6 = scene(f'''
<div data-in="0" data-out="9.75" style="position:absolute;left:0;right:0;top:150px;height:90px;background:{VERDE};overflow:hidden">
  <div data-marq="260" class="k" style="white-space:nowrap;color:{NEGRO};font-size:40px;line-height:90px;padding-left:40px">{marq}</div></div>
<div class="c d" data-type=".2,1.6" data-out="3.3" data-txt="Instagram le da prioridad al contenido original." style="top:520px;font-size:118px"></div>
<div class="c" data-in="2.1" data-out="3.3" style="top:1180px;font-size:46px;color:{GRIS_D}">Lo copiado o resubido llega a menos gente.</div>
<div class="c k" data-in="3.4" data-out="9.75" style="top:340px;color:{GRIS_D}">QUÉ HACER EN TU NEGOCIO</div>
{tips}
<div data-cover="9.8" style="position:absolute;inset:0;background:{CREMA}"></div>
<div data-in="9.9" style="position:absolute;left:-260px;top:300px;width:760px;height:760px">{mark_svg(NEGRO, 760)}</div>
<div data-in="10.1" style="position:absolute;left:560px;right:80px;top:420px;font-size:72px;color:{NEGRO}" class="d">Contenido original para tu marca.</div>
<div data-in="10.4" style="position:absolute;left:560px;right:80px;top:820px;font-size:36px;color:{GRIS};line-height:1.35">Lo pensamos, lo diseñamos y lo publicamos todas las semanas.</div>
<div class="c" data-in="10.7" style="top:1200px;text-align:center"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:42px;padding:24px 46px"><b style="color:{VERDE}">Consultanos</b> · Trabajemos juntos</span></div>
<div class="c" data-in="10.8" style="top:1340px;text-align:center;font-size:32px;color:{GRIS}">@triweb_73</div>
''')

# =============== R7 · Domingo · Web · TUTORIAL 3 pasos: aparecer en Google (crema, bossa) ===============
def res(a, out, name, sub):
    return (f'<div data-swipe="{a}" data-out="{out}" style="position:absolute;left:96px;right:96px;height:150px;background:#FFFFFF;border-radius:26px;padding:26px 32px;'
            f'top:{{y}}px"><div style="font-size:36px;font-weight:700;color:{NEGRO}">{name}</div><div style="font-size:28px;color:{GRIS};margin-top:8px">{sub}</div></div>')
results = ''.join(res(1.9 + i*.25, 4.1, n, s).replace('{y}', str(800 + i*175)) for i, (n, s) in enumerate(
    [('Panadería del Centro', '★ 4,8 · Abierto · Web'), ('La Esquina Panes', '★ 4,6 · Abierto · Web'), ('Pan & Co.', '★ 4,7 · Abierto · Web')]))
STEPS = [(4.4, 8.6), (8.6, 12.8), (12.8, 17.0)]
def stepbar(i):
    a, b = STEPS[i]
    return (f'<div data-scene="{a},{b}" style="position:absolute;left:96px;right:96px;top:150px">'
            f'<div class="k" style="color:{VERDE_TXT}">PASO {i+1} DE 3</div>'
            f'<div style="margin-top:20px;height:14px;background:#DDD6C6;border-radius:7px;overflow:hidden"><div data-wk="{a},{i*33.3};{a+.6},{(i+1)*33.4}" style="height:100%;background:{NEGRO};border-radius:7px"></div></div></div>')
fields = ''.join(f'<div data-in="{5.6 + k*.45:.2f}" data-out="8.6" style="display:flex;align-items:center;gap:22px;margin-bottom:26px;font-size:40px;font-weight:600">'
                 f'<span data-pop="{5.8 + k*.45:.2f}" data-out="8.6" style="width:56px;height:56px;border-radius:16px;background:{VERDE};display:inline-flex;align-items:center;justify-content:center;font-size:36px;color:{NEGRO}">✓</span>{f}</div>'
                 for k, f in enumerate(['Horarios reales', 'Fotos del local y productos', 'Teléfono y WhatsApp', 'Link a tu web']))
r7 = scene(f'''
<div class="c d" data-in=".1" data-out="4.2" style="top:300px;font-size:88px;color:{NEGRO}">¿Por qué tu competencia aparece en Google <span class="hl">y vos no</span>?</div>
<div data-in=".4" data-out="4.2" style="position:absolute;left:96px;right:96px;top:640px;height:120px;background:#FFFFFF;border-radius:60px;display:flex;align-items:center;padding:0 44px;gap:24px;box-shadow:0 14px 30px rgba(0,0,0,.08)">
  <div style="width:40px;height:40px;border:6px solid {GRIS};border-radius:50%"></div><div data-type=".6,1.1" data-txt="panadería cerca de mí" style="font-size:42px;color:{NEGRO}"></div></div>
{results}
<div class="c" data-pop="3.2" data-out="4.2" data-shake="3.2" style="top:1370px;text-align:center"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:40px;padding:22px 40px">Tu negocio: no aparece</span></div>
{stepbar(0)}{stepbar(1)}{stepbar(2)}
<div class="c d" data-in="4.5" data-out="8.6" style="top:330px;font-size:96px;color:{NEGRO}">Completá tu ficha de <span class="hl">Google</span>.</div>
<div class="c" data-in="5.0" data-out="8.6" style="top:610px;font-size:40px;color:{GRIS}">Es gratis. Google la muestra primero.</div>
<div class="c" style="top:800px">{fields}</div>
<div class="c d" data-in="8.7" data-out="12.8" style="top:330px;font-size:96px;color:{NEGRO}">Decí <span class="hl">qué</span> y <span class="hl">dónde</span> en tu web.</div>
<div data-in="9.2" data-out="12.8" style="position:absolute;left:96px;right:96px;top:740px;background:#FFFFFF;border-radius:26px;padding:34px">
  <div class="k" style="color:{GRIS};font-size:26px">TÍTULO DE TU WEB</div>
  <div style="font-size:52px;font-weight:700;color:{GRIS};margin-top:18px;position:relative;display:inline-block">Inicio<div data-pop="9.8" data-out="12.8" style="position:absolute;left:-8px;right:-8px;top:52%;height:8px;background:{NEGRO}"></div></div>
  <div data-in="10.3" data-out="12.8" data-shake="10.3" style="font-size:48px;font-weight:800;color:{NEGRO};margin-top:26px;line-height:1.2">Panadería en Morón · Pan de masa madre</div></div>
<div class="c" data-in="10.8" data-out="12.8" style="top:1260px;font-size:40px;color:{GRIS}">Rubro + barrio: así te busca la gente.</div>
<div class="c d" data-in="12.9" data-out="17.0" style="top:330px;font-size:96px;color:{NEGRO}">Pedí reseñas que nombren <span class="hl">el producto</span>.</div>
<div data-swipe="13.5" data-out="17.0" style="position:absolute;left:96px;right:200px;top:760px;background:#FFFFFF;border-radius:30px 30px 30px 6px;padding:32px;font-size:40px;color:{NEGRO}">
  <div style="color:{VERDE_TXT};font-size:34px;letter-spacing:.1em">★★★★★</div>"El mejor <b style="background:{VERDE};padding:0 6px;border-radius:6px">pan de masa madre</b> de la zona."</div>
<div data-swipe="14.2" data-out="17.0" style="position:absolute;left:200px;right:96px;top:1060px;background:#FFFFFF;border-radius:30px 30px 6px 30px;padding:32px;font-size:40px;color:{NEGRO}">
  <div style="color:{VERDE_TXT};font-size:34px;letter-spacing:.1em">★★★★★</div>"Las <b style="background:{VERDE};padding:0 6px;border-radius:6px">medialunas</b> salen calentitas a las 8."</div>
<div class="c" data-in="15.0" data-out="17.0" style="top:1380px;font-size:40px;color:{GRIS}">Google lee esas palabras.</div>
<div data-cover="17.1" style="position:absolute;inset:0;background:{NEGRO}"></div>
<div class="c d" data-in="17.3" style="top:430px;font-size:150px;color:{CREMA}">Que te encuentren <span class="hl">primero</span>.</div>
<div class="c" data-in="17.7" style="top:1000px;font-size:42px;color:{GRIS_D};line-height:1.4">Webs pensadas para Google y para vender.<br>Planes en triweb.com.ar · link en la bio.</div>
<div class="c" data-in="18.0" style="top:1220px;display:flex;align-items:center;justify-content:space-between">
  <span class="pill" style="background:{VERDE};color:{NEGRO};font-size:40px;padding:24px 44px"><b>Consultanos</b> · Trabajemos juntos</span>{mark_svg(CREMA, 120)}</div>
''', 'crema')

REELS = {  # nombre: (html, duración, segundo de portada)
    'antes-despues-web': (r5, 15.0, 1.6),
    'instagram-original': (r6, 13.0, 2.4),
    'google-3-pasos': (r7, 20.0, 3.5),
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
    mp4 = d / 'video.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', str(fr / '%04d.jpg'),
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-crf', '20', '-movflags', '+faststart', str(mp4)], check=True)
    shutil.copy(fr / f'{int(FPS*cover):04d}.jpg', d / f'triweb-{name}-portada.jpg')
    for s in (1, 4, 7, 10, 12, 13, 16, 19):
        if s*FPS < secs*FPS: shutil.copy(fr / f'{int(s*FPS):04d}.jpg', d / f'check-{s:02d}.jpg')
    shutil.rmtree(fr); print('ok', mp4)

if __name__ == '__main__':
    for n in (sys.argv[1:] or REELS): make(n)
