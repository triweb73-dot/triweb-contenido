"""Semana del 30/11: 4 reels nuevos, cada uno con layout, ritmo y música propios.
A mito vs. verdad del logo (tarjetas que giran) · B página de links vs. tu web (barra de cinchada con marcador)
C preguntas frecuentes (acordeón que se abre al beat) · D antes/después de marca (grilla 2×2 con barrido diagonal)."""
import sys, pathlib, subprocess, shutil
sys.path.insert(0, '/home/claude/triweb'); sys.path.insert(0, '/home/claude/triweb/semana4'); sys.path.insert(0, '/home/claude/triweb/semana5'); sys.path.insert(0, '/home/claude/triweb/semana6')
from kit import *
from reels4 import JS as JS4, CSS as CSS4
from reels5 import JS_EXTRA
from reels6 import JS6, CSS as CSS6

OUT = pathlib.Path('/home/claude/triweb/semana7/out'); OUT.mkdir(parents=True, exist_ok=True)
FPS = 30
JS7 = """<script>
const _r6=render;
render=function(t){_r6(t);
 document.querySelectorAll('[data-slide]').forEach(el=>{const [a,b]=el.dataset.slide.split(',').map(Number);
   const x=t<b?(1-ease((t-a)/.32))*1200:-ease((t-b)/.3)*1200; el.style.left=(+el.dataset.x)+x+'px'; el.style.opacity=(t>=a&&t<b+.3)?1:0;});
 document.querySelectorAll('[data-flip]').forEach(el=>{const a=+el.dataset.flip; el.style.transform=`perspective(2400px) rotateY(${180*ease((t-a)/.42)}deg)`;});
 document.querySelectorAll('[data-acc]').forEach(el=>{const [a,b,h0,h1]=el.dataset.acc.split(',').map(Number);
   const p=t<b?ease((t-a)/.35):1-ease((t-b)/.3); el.style.height=(h0+(h1-h0)*p)+'px';
   const pl=el.querySelector('.plus'); if(pl) pl.style.transform=`rotate(${45*p}deg)`; const an=el.querySelector('.ans'); if(an) an.style.opacity=cl((p-.5)*2);
   el.style.background=p>.5?el.dataset.on:el.dataset.off;});
 document.querySelectorAll('[data-diag]').forEach(el=>{const a=+el.dataset.diag,p=ease((t-a)/.3)*220-20;
   el.style.clipPath=`polygon(0 0,${p}% 0,${p-100}% 100%,0 100%)`; el.style.opacity=t>=a?1:0;});
 document.querySelectorAll('[data-left]').forEach(el=>{el.style.left=kf(el.dataset.left,t)+'%';});
};
render(0);
</script>"""
CSS = CSS6 + ' [data-slide]{opacity:0} [data-diag]{opacity:0} .face{position:absolute;inset:0;border-radius:48px;backface-visibility:hidden;-webkit-backface-visibility:hidden;padding:70px}'

def scene(inner, bg=NEGRO):
    return page(inner + JS4 + JS_EXTRA + JS6 + JS7, 1080, 1920, '', extra_css=CSS + 'body{background:%s} #frame{background:%s;color:%s}' % (bg, bg, CREMA if bg == NEGRO else NEGRO))

def cta_block(a, fg, mut, pillbg, pillfg, top=1180):
    return (f'<div class="c" data-pop="{a}" style="top:{top}px;display:flex;align-items:center;justify-content:space-between">'
            f'<span class="pill" style="background:{pillbg};color:{pillfg};font-size:40px;padding:24px 44px"><b>Consultanos</b> · Trabajemos juntos</span>{mark_svg(fg, 116)}</div>'
            f'<div class="c" data-in="{a+.1}" style="top:{top+180}px;font-size:32px;color:{mut}">@triweb_73</div>')

# ===== A · Martes 01/12 · Branding · MITO VS. VERDAD del logo · tarjetas que giran · electro swing 124 bpm · 15,5 s =====
MITOS = [('“Más colores, más llamativo.”', '2 o 3 colores se recuerdan más. El resto es ruido.'),
         ('“Lo cambio cuando me aburra.”', 'Cambiarlo seguido confunde. La constancia hace que te reconozcan.'),
         ('“Con una plantilla gratis alcanza.”', 'Si es de plantilla, lo puede tener cualquiera. Hasta tu competencia.')]
TA = [(2.2, 4.1, 5.9), (5.9, 7.8, 9.6), (9.6, 11.5, 13.3)]  # entra, gira, sale
cardsA = ''
for i, ((m, v), (a, f, o)) in enumerate(zip(MITOS, TA)):
    cardsA += (f'<div data-slide="{a},{o}" data-x="110" style="position:absolute;top:560px;width:860px;height:900px">'
               f'<div data-flip="{f}" data-shake="{f+.2}" style="position:absolute;inset:0;transform-style:preserve-3d">'
               f'<div class="face" style="background:{CREMA};color:{NEGRO}"><div class="k" style="color:{GRIS}">MITO {i+1}/3</div>'
               f'<div class="d" style="margin-top:60px;font-size:104px">{m}</div>'
               f'<div style="position:absolute;left:70px;bottom:70px;font-size:34px;font-weight:700;color:{GRIS}">¿Verdad o mito?</div></div>'
               f'<div class="face" style="background:{VERDE};color:{NEGRO};transform:rotateY(180deg)"><div class="k">LA VERDAD</div>'
               f'<div class="d" style="margin-top:60px;font-size:92px">{v}</div>'
               f'<div style="position:absolute;left:70px;bottom:70px;font-size:34px;font-weight:700;text-decoration:line-through;text-decoration-thickness:4px">{m}</div></div>'
               f'</div></div>')
rA = scene(f'''
<div data-scene="0,2.2" style="position:absolute;inset:0">
 <div class="c" data-pop="0" style="top:300px"><span class="pill" style="background:{CREMA};color:{NEGRO};font-size:34px">MITO VS. VERDAD · BRANDING</span></div>
 <div class="c d" data-words=".15,.12" style="top:430px;font-size:150px">3 mitos que arruinan tu logo.</div></div>
<div class="c k" data-in="2.2" data-out="13.3" style="top:400px;color:{GRIS_D}">TOCÁ PAUSA Y ADIVINÁ</div>
{cardsA}
<div data-cover="13.35" style="position:absolute;inset:0;background:{CREMA}"></div>
<div class="c d" data-punch="13.5" data-shake="13.5" style="top:420px;font-size:120px;color:{NEGRO}">Un logo simple, <span class="hl">tuyo</span> y constante.</div>
<div class="c" data-in="13.8" style="top:820px;font-size:42px;color:{GRIS};line-height:1.4">Branding y diseño de logos para negocios.</div>
{cta_block(14.0, NEGRO, GRIS, NEGRO, CREMA, 1020)}
''', NEGRO)

# ===== B · Miércoles 02/12 · TRIAL_REEL · Web · COMPARACIÓN: página de links vs. tu web · barra de cinchada · techno minimal 126 bpm · 13 s =====
R = [('Te encuentran en Google', 'Casi nunca aparece cuando buscan tu rubro.', 'Puede aparecer con tu rubro y tu barrio.'),
     ('Tu nombre en la dirección', 'Dirección de otra empresa.', 'tunegocio.com.ar'),
     ('Fotos, precios y servicios', 'Una lista de botones.', 'Todo ordenado en un lugar.'),
     ('Se ve como un negocio', 'Igual que miles de perfiles.', 'Con tu marca, de punta a punta.')]
RT = [2.4, 4.4, 6.4, 8.4]
roundsB = ''
for i, ((t, l, w), a) in enumerate(zip(R, RT)):
    b = a + 2.0
    roundsB += (f'<div data-scene="{a},{b}" style="position:absolute;inset:0">'
                f'<div class="c k" data-pop="{a}" style="top:330px;color:{VERDE}">RONDA {i+1}/4</div>'
                f'<div class="c d" data-punch="{a}" data-shake="{a}" style="top:400px;font-size:96px">{t}</div>'
                f'<div data-in="{a+.25}" style="position:absolute;left:70px;width:450px;top:760px;height:420px;border-radius:36px;border:4px solid #2A2A2E;padding:40px;color:{GRIS_D}">'
                f'<div class="k" style="font-size:26px">PÁGINA DE LINKS</div><div style="margin-top:30px;font-size:42px;font-weight:700;line-height:1.25">{l}</div></div>'
                f'<div data-pop="{a+.55}" style="position:absolute;left:560px;width:450px;top:760px;height:420px;border-radius:36px;background:{CREMA};color:{NEGRO};padding:40px">'
                f'<div class="k" style="font-size:26px;color:{VERDE_TXT}">TU WEB ✓</div><div style="margin-top:30px;font-size:44px;font-weight:800;line-height:1.2">{w}</div></div></div>')
rB = scene(f'''
<div data-scene="0,2.4" style="position:absolute;inset:0">
 <div class="c d" data-punch="0" data-shake="0" style="top:360px;font-size:118px;color:{GRIS_D}">¿Página de links</div>
 <div class="c d" data-punch=".7" data-shake=".7" style="top:700px;font-size:190px">o tu <span class="hl">web</span>?</div>
 <div class="c" data-in="1.2" style="top:1150px;font-size:44px;color:{GRIS_D}">4 rondas. Un ganador.</div></div>
{roundsB}
<div data-in="2.4" data-out="10.4" style="position:absolute;left:70px;right:70px;top:1300px">
 <div style="display:flex;justify-content:space-between;font-size:30px;font-weight:700;color:{GRIS_D}"><span>Links <b class="d" style="font-size:60px;color:{CREMA}">0</b></span>
  <span>Web <b class="d" style="position:relative;display:inline-block;width:50px;font-size:60px;color:{VERDE}">{''.join(f'<span data-scene="{a},{b}" style="position:absolute;left:0;bottom:-8px">{n}</span>' for n,(a,b) in enumerate([(0,2.9),(2.9,4.9),(4.9,6.9),(6.9,8.9),(8.9,99)]))}</b></span></div>
 <div style="position:relative;margin-top:24px;height:28px;border-radius:14px;background:#2A2A2E">
  <div style="position:absolute;left:50%;top:-14px;bottom:-14px;width:4px;background:#4A4A4E"></div>
  <div data-left="2.4,50;2.9,60;4.9,70;6.9,80;8.9,92" style="position:absolute;top:-22px;width:72px;height:72px;margin-left:-36px;border-radius:36px;background:{VERDE};box-shadow:0 0 0 8px {NEGRO}"></div></div></div>
<div data-cover="10.45" style="position:absolute;inset:0;background:{CREMA}"></div>
<div class="c k" data-in="10.55" style="top:300px;color:{VERDE_TXT}">RESULTADO: 4 A 0</div>
<div class="c d" data-punch="10.6" data-shake="10.6" style="top:380px;font-size:104px;color:{NEGRO}">Los links sirven para empezar. Para vender: <span class="hl">tu web</span>.</div>
<div class="c" data-in="10.9" style="top:880px;font-size:40px;color:{GRIS}">Diseño web para negocios · triweb.com.ar</div>
{cta_block(11.1, NEGRO, GRIS, NEGRO, CREMA, 1040)}
''', NEGRO)

# ===== C · Viernes 04/12 · Web · PREGUNTA FRECUENTE con datos de la web (promo de la semana) · acordeón · amapiano 112 bpm · 17,5 s =====
QA = [('¿Tengo que tener todo listo para arrancar?', 'No. Contanos qué hacés y te asesoramos gratis.'),
      ('¿Cuánto tarda una landing page?', '7 días hábiles: la idea, el diseño y online.'),
      ('¿Y si ya tengo web?', 'La rediseñamos. Rediseños desde $197.000.*'),
      ('¿Me sirve si vendo por Instagram?', 'Sí: la web te hace aparecer en Google y ordena tus precios.')]
QT = [(2.6, 5.4), (5.4, 8.2), (8.2, 11.0), (11.0, 13.8)]
H0, H1 = 150, 430
accC = ''
for i, ((q, ans), (a, b)) in enumerate(zip(QA, QT)):
    accC += (f'<div data-acc="{a},{b},{H0},{H1}" data-on="{NEGRO}" data-off="#FFFFFF" data-in="{1.9+i*.12:.2f}" data-out="13.85" '
             f'style="position:relative;overflow:hidden;border-radius:32px;margin-bottom:22px;height:{H0}px;padding:0 40px;color:inherit">'
             f'<div style="height:{H0}px;display:flex;align-items:center;justify-content:space-between;gap:24px">'
             f'<span style="font-size:42px;font-weight:800;line-height:1.15;mix-blend-mode:difference;color:{CREMA}">{q}</span>'
             f'<span class="plus" style="flex:none;width:70px;height:70px;border-radius:35px;background:{VERDE};color:{NEGRO};display:flex;align-items:center;justify-content:center;font-size:56px;font-weight:500">+</span></div>'
             f'<div class="ans d" style="font-size:66px;color:{CREMA};line-height:1.05">{ans}</div></div>')
rC = scene(f'''
<div data-scene="0,1.9" style="position:absolute;inset:0">
 <div data-sticker="0" data-rot="-4" style="position:absolute;left:96px;top:330px;background:{VERDE};color:{NEGRO};font-weight:900;font-size:46px;padding:10px 28px;border-radius:14px;letter-spacing:.06em">FAQ</div>
 <div class="c d" data-words=".2,.1" style="top:470px;font-size:124px;color:{NEGRO}">Lo que más nos preguntan antes de hacer una web.</div></div>
<div class="c k" data-in="1.9" data-out="13.85" style="top:250px;color:{VERDE_TXT}">PREGUNTAS FRECUENTES · TRIWEB.COM.AR</div>
<div class="c" style="top:330px">{accC}</div>
<div data-in="9.0" data-out="13.85" style="position:absolute;left:96px;right:96px;top:1500px;font-size:28px;color:{GRIS}">*Precio publicado en triweb.com.ar al 2/11/2026. Mirá los actualizados en la web.</div>
<div data-cover="13.9" style="position:absolute;inset:0;background:{NEGRO}"></div>
<div class="c d" data-punch="14.05" data-shake="14.05" style="top:400px;font-size:120px;color:{CREMA}">¿Te quedó una <span class="hl">duda</span>?</div>
<div class="c" data-in="14.35" style="top:800px;font-size:42px;color:{GRIS_D};line-height:1.4">Escribinos por mensaje o mirá los planes en triweb.com.ar (link en la bio).</div>
{cta_block(14.6, CREMA, GRIS_D, VERDE, NEGRO, 1060)}
''', CREMA)
# las tarjetas usan texto con mix-blend para leerse tanto en blanco (cerradas) como en negro (abiertas)

# ===== D · Sábado 05/12 · Branding · ANTES / DESPUÉS de marca (ejemplo ilustrativo) · grilla 2×2 con barrido diagonal · chacarera electrónica 6/8 · 12,5 s =====
def before(k):
    s = [('background:#E84A8A;color:#FFFFFF;font-family:Georgia,serif;font-style:italic', 'Heladería<br>Nube', 'Cartel'),
         ('background:#3A7BD5;color:#FFEB3B;font-family:Impact,sans-serif;letter-spacing:.04em', 'HELADOS<br>NUBE!!', 'Post'),
         ('background:#F2C94C;color:#7B3F00;font-family:cursive', 'nube<br>helados', 'Vaso'),
         ('background:#FFFFFF;color:#2E7D32;font-family:monospace', 'H. NUBE<br>S.R.L.', 'Bolsa')][k]
    return (f'<div style="position:absolute;inset:0;{s[0]};display:flex;align-items:center;justify-content:center;text-align:center;font-size:62px;font-weight:700;line-height:1.05">{s[1]}</div>'
            f'<div style="position:absolute;left:22px;bottom:18px;font-size:24px;font-weight:700;font-family:Inter;color:rgba(0,0,0,.45)">{s[2]}</div>')
def cloud(c, size):
    return (f'<svg width="{size}" height="{size*0.62:.0f}" viewBox="0 0 100 62"><path d="M22 60 a20 20 0 0 1 2-40 a26 26 0 0 1 50 4 a18 18 0 0 1 4 36 z" fill="{c}"/>'
            f'<circle cx="50" cy="34" r="7" fill="{VERDE}"/></svg>')
def after(k):
    bg, fg = [(NEGRO, CREMA), (CREMA, NEGRO), (CREMA, NEGRO), (NEGRO, CREMA)][k]
    lab = ['Cartel', 'Post', 'Vaso', 'Bolsa'][k]
    return (f'<div style="position:absolute;inset:0;background:{bg};color:{fg};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;border-radius:30px;box-shadow:inset 0 0 0 4px #2A2A2E">'
            f'{cloud(fg, 170)}<div class="d" style="font-size:54px">nube</div><div style="font-size:20px;font-weight:700;letter-spacing:.2em">HELADOS</div></div>'
            f'<div style="position:absolute;left:22px;bottom:18px;font-size:24px;font-weight:700;color:{GRIS}">{lab}</div>')
BEAT6 = 60/100/2*3  # negra con punto a 100 bpm (6/8): 0,9 s
DT = [4.6 + i*0.6 for i in range(4)]
gridD = ''
for k in range(4):
    x, y = 70 + (k % 2)*480, 520 + (k//2)*480
    gridD += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:460px;height:460px;border-radius:30px;overflow:hidden">'
              f'<div data-pop="{.9+k*.15:.2f}" data-shake="{.9+k*.15:.2f}" style="position:absolute;inset:0">{before(k)}</div>'
              f'<div data-diag="{DT[k]:.2f}" data-shake="{DT[k]:.2f}" style="position:absolute;inset:0">{after(k)}</div></div>')
rD = scene(f'''
<div data-out="8.3" style="position:absolute;inset:0">
 <div data-zk="0,1;7.0,1;8.2,1.3" style="position:absolute;inset:0;transform-origin:50% 55%">
  <div class="c" data-in="0" style="top:230px;display:flex;gap:16px"><span data-out="4.4" class="pill" style="background:#2A2A2E;color:{CREMA};font-size:32px">ANTES</span></div>
  <div class="c" data-pop="4.5" style="top:230px"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:32px">DESPUÉS</span></div>
  <div class="c d" data-punch=".1" data-out="4.4" style="top:330px;font-size:84px">4 piezas, 4 marcas.</div>
  <div class="c d" data-punch="4.6" style="top:330px;font-size:84px">4 piezas, <span class="hl">1 marca</span>.</div>
  {gridD}
  <div class="c" data-in="1.6" style="top:1500px;font-size:28px;color:{GRIS_D}">Ejemplo ilustrativo: “Nube helados” es una marca inventada.</div>
 </div></div>
<div data-cover="8.35" style="position:absolute;inset:0;background:{CREMA}"></div>
<div class="c d" data-punch="8.5" data-shake="8.5" style="top:380px;font-size:110px;color:{NEGRO}">Mismos colores. Misma letra. <span class="hl">Te reconocen</span>.</div>
<div class="c" data-in="8.8" style="top:850px;font-size:40px;color:{GRIS};line-height:1.4">Logo, paleta y piezas que hablan igual. Branding para negocios.</div>
{cta_block(9.1, NEGRO, GRIS, NEGRO, CREMA, 1060)}
''', NEGRO)

REELS = {  # nombre: (html, duración, segundo de portada)
    'mitos-del-logo': (rA, 15.5, 3.0),
    'links-vs-web': (rB, 13.0, 1.6),
    'preguntas-web': (rC, 17.5, 6.4),
    'antes-despues-marca': (rD, 12.5, 7.2),
}

def make(name):
    html, secs, cover = REELS[name]
    d = OUT / name; fr = d / 'frames'; shutil.rmtree(fr, ignore_errors=True); fr.mkdir(parents=True)
    h = d / 'reel.html'; h.write_text(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(h.resolve().as_uri()); pg.wait_for_timeout(900)
        for i in range(int(secs * FPS)):
            pg.evaluate(f'render({i/FPS})')
            pg.screenshot(path=str(fr / f'{i:04d}.jpg'), type='jpeg', quality=90, clip={'x': 0, 'y': 0, 'width': 1080, 'height': 1920})
        b.close()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', str(fr / '%04d.jpg'),
                    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-crf', '20', '-movflags', '+faststart', str(d / 'video.mp4')], check=True)
    shutil.copy(fr / f'{int(FPS*cover):04d}.jpg', d / f'triweb-{name}-portada.jpg')
    for s in [x/2 for x in range(1, int(secs*2))]:
        shutil.copy(fr / f'{int(s*FPS):04d}.jpg', d / f'check-{s:04.1f}.jpg')
    shutil.rmtree(fr); print('ok', name)

if __name__ == '__main__':
    for n in (sys.argv[1:] or REELS): make(n)
