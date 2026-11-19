"""Semana del 23/11: 4 reels nuevos, cada uno con layout, ritmo y música propios.
A confesión de diseñador (tendencia "Sue me": texto tipo sticker sobre imagen con zoom lento) · B quiz A/B con cuenta regresiva
C novedad Edits (dos columnas sí/no con barridos) · D landing en 7 días hábiles (contador gigante con contorno + celular que se arma)."""
import sys, pathlib, subprocess, shutil
sys.path.insert(0, '/home/claude/triweb'); sys.path.insert(0, '/home/claude/triweb/semana4'); sys.path.insert(0, '/home/claude/triweb/semana5')
from kit import *
from reels4 import JS as JS4, CSS as CSS4
from reels5 import JS_EXTRA

OUT = pathlib.Path('/home/claude/triweb/semana6/out'); OUT.mkdir(parents=True, exist_ok=True)
FPS = 30
SURA = '/home/claude/triweb/sura/src/'
JS6 = """<script>
const _r5=render;
render=function(t){_r5(t);
 document.querySelectorAll('[data-count]').forEach(el=>{const [a,b,v0,v1]=el.dataset.count.split(',').map(Number);
   el.textContent=Math.round(v0+(v1-v0)*cl((t-a)/(b-a)));});
 document.querySelectorAll('[data-sticker]').forEach(el=>{const a=+el.dataset.sticker,p=back((t-a)/.28);
   el.style.transform=`rotate(${el.dataset.rot||0}deg) scale(${Math.max(0,p)})`;el.style.opacity=(t>=a?1:0)*out(el,t);});
 document.querySelectorAll('[data-tick]').forEach(el=>{const a=+el.dataset.tick,p=ease((t-a)/.18),b=a+.85;
   el.style.opacity=(t>=a&&t<b+.15)?(t>b?1-(t-b)/.15:1):0;el.style.transform=`scale(${2.2-1.2*p})`;});
};
render(0);
</script>"""
CSS = CSS4 + (' .w{opacity:0} .o{color:transparent;-webkit-text-stroke:5px currentColor} [data-sticker],[data-tick]{opacity:0}'
              ' .stw .w{background:#FFFFFF;color:#0B0B0C;padding:0 .14em;margin:.03em 0;border-radius:.12em} .st{display:inline;background:#FFFFFF;color:#0B0B0C;padding:.08em .28em;border-radius:.18em;line-height:1.42;box-decoration-break:clone;-webkit-box-decoration-break:clone}')

def scene(inner, bg=NEGRO):
    return page(inner + JS4 + JS_EXTRA + JS6, 1080, 1920, '', extra_css=CSS + 'body{background:%s} #frame{background:%s;color:%s}' % (bg, bg, CREMA if bg == NEGRO else NEGRO))

def cta_block(a, fg, mut, pillbg, pillfg, top=1180):
    return (f'<div class="c" data-pop="{a}" style="top:{top}px;display:flex;align-items:center;justify-content:space-between">'
            f'<span class="pill" style="background:{pillbg};color:{pillfg};font-size:40px;padding:24px 44px"><b>Consultanos</b> · Trabajemos juntos</span>{mark_svg(fg, 116)}</div>'
            f'<div class="c" data-in="{a+.1}" style="top:{top+180}px;font-size:32px;color:{mut}">@triweb_73</div>')

# ===== A · Lunes 23 · Branding · CONFESIÓN DE DISEÑADOR (tendencia "Sue me") · tango electrónico 116 bpm · 9,5 s =====
rA = scene(f'''
<div style="position:absolute;left:0;right:0;top:880px;height:780px;overflow:hidden">
  <div data-kb="0,6.4,1.0,1.12" style="position:absolute;inset:0;background:url(file://{SURA}logo-negro.png) center/contain no-repeat;transform-origin:50% 50%"></div></div>
<div data-out="6.3" style="position:absolute;left:90px;right:90px;top:300px">
  <div data-sticker=".05" data-rot="-3" style="display:inline-block;background:{CREMA};color:{NEGRO};font-weight:800;font-size:44px;padding:12px 26px;border-radius:14px">confesión de diseñador:</div></div>
<div data-scene="0,3.4" style="position:absolute;inset:0"><div class="d stw" data-words=".35,.11" style="position:absolute;left:90px;right:90px;top:450px;font-size:100px;line-height:1.22">tu logo no tiene que mostrar lo que vendés.</div></div>
<div data-in="3.45" data-out="6.3" style="position:absolute;left:90px;right:90px;top:450px;font-size:62px;font-weight:700;line-height:1.5"><span class="st">Sura es un estudio de arquitectura.</span><br><span class="st">Su logo no tiene una casa:</span><br><span class="st" style="background:{VERDE}">tiene un pájaro sobre una viga.</span></div>
<div data-sticker="4.9" data-rot="4" data-out="6.3" style="position:absolute;left:90px;top:900px;background:{CREMA};color:{NEGRO};font-size:34px;font-weight:700;padding:14px 26px;border-radius:14px">proyecto de branding · TriWeb</div>
<div data-cover="6.35" style="position:absolute;inset:0;background:{CREMA}"></div>
<div class="c d" data-punch="6.5" data-shake="6.5" style="top:430px;font-size:128px;color:{NEGRO}">Una marca que se <span class="hl">recuerda</span>.</div>
<div class="c" data-in="6.8" style="top:830px;font-size:42px;color:{GRIS};line-height:1.4">Símbolo, colores y letra con una idea detrás.<br>Branding para negocios.</div>
{cta_block(7.1, NEGRO, GRIS, NEGRO, CREMA, 1060)}
''', NEGRO)

# ===== B · Miércoles 25 · TRIAL_REEL · Web · QUIZ A/B con cuenta regresiva · drum & bass 172 bpm · 15 s =====
def mock(good):
    if not good:
        return (f'<div style="position:absolute;inset:0;background:#E9E4D8">'
                f'<div style="height:70px;background:#CFC8B8;display:flex;align-items:center;justify-content:space-around;font-size:16px;color:#8A8478">Inicio · Nosotros · Servicios · Galería · Contacto</div>'
                f'<div style="margin:28px;height:250px;border-radius:12px;background:repeating-linear-gradient(45deg,#D7D0C1 0 14px,#CFC8B8 14px 28px);display:flex;align-items:center;justify-content:center;font-size:22px;color:#8A8478">slider</div>'
                f'<div style="text-align:center;font-size:40px;font-weight:700;color:#8A8478;margin-top:10px;font-family:Georgia,serif">Bienvenidos</div>'
                f'<div style="margin:18px 34px;font-size:17px;line-height:1.5;color:#9A9488">Somos una empresa con años de trayectoria comprometida con la calidad y la excelencia en cada uno de nuestros productos...</div>'
                f'<div style="text-align:center;margin-top:16px"><span style="font-size:15px;color:#9A9488;border:1px solid #B8B1A3;padding:6px 14px">Más info</span></div></div>')
    return (f'<div style="position:absolute;inset:0;background:{NEGRO};color:{CREMA}">'
            f'<div style="padding:26px 30px;display:flex;justify-content:space-between;align-items:center;font-size:18px;font-weight:700"><span>Panadería</span><span style="color:{VERDE}">● Abierto</span></div>'
            f'<div class="d" style="margin:14px 30px 0;font-size:50px;line-height:1">Pan de masa madre, recién hecho.</div>'
            f'<div style="margin:16px 30px;font-size:19px;color:{GRIS_D}">Pedí hasta las 18 h y retirá hoy.</div>'
            f'<div style="margin:18px 30px;height:200px;border-radius:16px;background:linear-gradient(135deg,#C9A36A,#8A5A2B)"></div>'
            f'<div style="margin:0 30px;font-size:24px;font-weight:800">Hogaza 1 kg · <span style="color:{VERDE}">$ —</span></div>'
            f'<div style="margin:22px 30px 0;background:{VERDE};color:{NEGRO};border-radius:999px;text-align:center;padding:16px;font-size:22px;font-weight:800">Pedir por WhatsApp</div></div>')

PW, PH = 400, 760
def phone(x, good, letter):
    return (f'<div style="position:absolute;left:{x}px;top:640px;width:{PW+24}px;height:{PH+24}px;border-radius:56px;background:#1E1E21;padding:12px">'
            f'<div style="position:relative;width:{PW}px;height:{PH}px;border-radius:46px;overflow:hidden">{mock(good)}</div></div>'
            f'<div class="d" style="position:absolute;left:{x}px;width:{PW+24}px;top:520px;text-align:center;font-size:100px;color:{CREMA}">{letter}</div>')
why = [('Dice qué vende en la primera línea.', 7.2), ('El botón para escribir, a la vista.', 8.5), ('Precio y horario: cero dudas.', 9.8)]
whyB = ''.join(f'<div data-swipe="{a}" data-out="11.6" style="position:absolute;left:96px;right:96px;top:{560+i*240}px;height:200px;background:{CREMA};color:{NEGRO};border-radius:28px;'
               f'display:flex;align-items:center;gap:30px;padding:0 40px"><span class="d o" style="font-size:110px;color:{NEGRO};-webkit-text-stroke:4px {NEGRO}">{i+1}</span>'
               f'<span style="font-size:50px;font-weight:700;line-height:1.2">{t}</span></div>' for i, (t, a) in enumerate(why))
rB = scene(f'''
<div data-scene="0,6.9" style="position:absolute;inset:0">
 <div class="c" data-pop="0" style="top:170px"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:34px">QUIZ · 3 SEGUNDOS</span></div>
 <div class="c d" data-punch=".1" data-shake=".1" style="top:280px;font-size:104px">¿A cuál le escribís?</div>
 <div data-in=".35">{phone(96, False, 'A')}</div>
 <div data-in=".55">{phone(560, True, 'B')}</div>
 <div data-in="1.4" data-out="2.9" style="position:absolute;left:0;right:0;top:1460px;text-align:center;font-size:40px;font-weight:700;color:{GRIS_D}">Comentá A o B antes de que termine.</div>
 <div data-tick="3.0" style="position:absolute;left:0;right:0;top:1440px;text-align:center"><span class="d o" style="font-size:210px;color:{CREMA}">3</span></div>
 <div data-tick="4.0" style="position:absolute;left:0;right:0;top:1440px;text-align:center"><span class="d o" style="font-size:210px;color:{CREMA}">2</span></div>
 <div data-tick="5.0" style="position:absolute;left:0;right:0;top:1440px;text-align:center"><span class="d o" style="font-size:210px;color:{VERDE}">1</span></div>
 <div data-pop="6.0" data-shake="6.0" style="position:absolute;left:548px;top:628px;width:448px;height:808px;border:10px solid {VERDE};border-radius:64px"></div>
 <div data-sticker="6.05" data-rot="-8" style="position:absolute;left:640px;top:1460px;background:{VERDE};color:{NEGRO};font-size:56px;font-weight:900;padding:8px 30px;border-radius:16px;letter-spacing:.06em">GANA B</div>
</div>
<div class="c k" data-in="7.0" data-out="11.6" style="top:430px;color:{VERDE}">POR QUÉ GANA B</div>
{whyB}
<div data-cover="11.65" style="position:absolute;inset:0;background:{NEGRO}"></div>
<div class="c d" data-punch="11.8" style="top:420px;font-size:120px">¿Tu web es <span class="hl" style="white-space:nowrap">la A</span>?</div>
<div class="c" data-in="12.1" style="top:820px;font-size:42px;color:{GRIS_D};line-height:1.4">La pasamos a la B.<br>Diseño web para negocios · triweb.com.ar</div>
{cta_block(12.4, CREMA, GRIS_D, VERDE, NEGRO, 1080)}
<div data-in="12.5" style="position:absolute;left:96px;top:1480px;font-size:26px;color:#5A5650">Ejemplo ilustrativo.</div>
''', NEGRO)

# ===== C · Jueves 26 · Community manager · NOVEDAD: asistente de IA en Edits · dos columnas sí/no · UK garage 132 bpm · 12 s =====
SI = ['Ganchos', 'Guiones', 'Textos', 'Audios']
NO = ['Grabar tu producto', 'Conocer a tu cliente', 'Responder con tu tono', 'Tener constancia']
colC = ''.join(f'<div data-wipe="{4.1+i*.32:.2f}" data-out="9.3" style="position:absolute;left:70px;width:440px;top:{720+i*150}px;height:120px;background:{CREMA};color:{NEGRO};border-radius:22px;display:flex;align-items:center;gap:18px;padding:0 28px;font-size:42px;font-weight:800">'
               f'<span style="width:54px;height:54px;border-radius:50%;background:{VERDE};display:flex;align-items:center;justify-content:center;font-size:34px">✓</span>{t}</div>' for i, t in enumerate(SI))
colC += ''.join(f'<div data-wipe="{6.2+i*.32:.2f}" data-out="9.3" style="position:absolute;left:570px;width:440px;top:{720+i*150}px;height:120px;border:4px solid #3A3A3E;color:{CREMA};border-radius:22px;display:flex;align-items:center;gap:18px;padding:0 24px;font-size:34px;font-weight:700;line-height:1.1">'
                f'<span style="flex:none;width:54px;height:54px;border-radius:50%;border:4px solid {GRIS_D};display:flex;align-items:center;justify-content:center;font-size:30px;color:{GRIS_D}">✕</span>{t}</div>' for i, t in enumerate(NO))
rC = scene(f'''
<div data-out="3.7" style="position:absolute;inset:0">
 <div style="position:absolute;left:0;right:0;top:170px;height:84px;border-top:3px solid #2A2A2E;border-bottom:3px solid #2A2A2E;overflow:hidden">
  <div data-marq="180" class="k" style="white-space:nowrap;color:{GRIS_D};font-size:34px;line-height:78px;padding-left:40px">{'NOVEDAD DE INSTAGRAM · EDITS · ' * 8}</div></div>
 <div class="c d" data-words=".15,.09" style="top:420px;font-size:112px">Instagram sumó una IA que te escribe los reels.</div>
 <div class="c" data-in="1.9" style="top:1150px;font-size:44px;color:{GRIS_D};line-height:1.4">Está dentro de <b style="color:{CREMA}">Edits</b>, su app de edición. Mira cómo rinden tus reels y te propone ideas.</div></div>
<div data-cover="3.75" data-out="9.3" style="position:absolute;inset:0;background:#141416"></div>
<div data-in="3.85" data-out="9.3" style="position:absolute;left:70px;width:440px;top:560px" class="k"><span style="color:{VERDE}">TE PROPONE</span></div>
<div data-in="5.9" data-out="9.3" style="position:absolute;left:570px;width:440px;top:560px;color:{GRIS_D}" class="k">NO PUEDE</div>
<div class="c d" data-in="3.85" data-out="9.3" style="top:300px;font-size:76px">Lo que hace y lo que <span class="hl">no</span>.</div>
{colC}
<div data-cover="9.35" style="position:absolute;inset:0;background:{CREMA}"></div>
<div class="c d" data-punch="9.5" data-shake="9.5" style="top:400px;font-size:112px;color:{NEGRO}">La IA ayuda. La estrategia es tuya.</div>
<div class="c" data-in="9.8" style="top:800px;font-size:40px;color:{GRIS};line-height:1.4">O nuestra: community manager para negocios.</div>
{cta_block(10.0, NEGRO, GRIS, NEGRO, CREMA, 1020)}
''', NEGRO)

# ===== D · Viernes 27 · Web · PROMO (Black Friday) · LANDING EN 7 DÍAS HÁBILES · contador gigante + celular que se arma · nu-disco 120 bpm · 16 s =====
BEAT = 0.5
stages = [  # (t, etiqueta, contenido del celular)
 (3.0, 'La idea', f'<div style="position:absolute;inset:26px;border:3px dashed #8A8478;border-radius:18px"></div>'
                   + ''.join(f'<div style="position:absolute;left:50px;right:{50+k*60}px;top:{90+k*70}px;height:24px;border-radius:12px;background:#CFC8B8"></div>' for k in range(4))),
 (5.0, 'El diseño', f'<div style="position:absolute;inset:0;background:{CREMA}"></div><div class="d" style="position:absolute;left:34px;right:34px;top:70px;font-size:46px;color:{NEGRO};line-height:1">Tu negocio, en una frase clara.</div>'
                   f'<div style="position:absolute;left:34px;right:34px;top:260px;height:230px;border-radius:16px;background:#D9D3C5"></div>'
                   f'<div style="position:absolute;left:34px;right:34px;top:520px;height:64px;border-radius:999px;background:#BFB8A8"></div>'),
 (7.0, 'Online', f'<div style="position:absolute;inset:0;background:{NEGRO}"></div><div class="d" style="position:absolute;left:34px;right:34px;top:70px;font-size:46px;color:{CREMA};line-height:1">Tu negocio, en una frase clara.</div>'
                f'<div style="position:absolute;left:34px;right:34px;top:260px;height:230px;border-radius:16px;background:linear-gradient(135deg,#2E2E33,#555)"></div>'
                f'<div style="position:absolute;left:34px;right:34px;top:520px;height:64px;border-radius:999px;background:{VERDE};color:{NEGRO};font-size:22px;font-weight:800;display:flex;align-items:center;justify-content:center">Escribinos</div>'),
]
phD = ''.join(f'<div data-wipe="{a}" data-out="9.4" style="position:absolute;inset:0">{h}</div>' for a, _, h in stages)
labD = ''.join(f'<div data-pop="{a}" data-shake="{a}" data-out="{(stages[i+1][0] if i < 2 else 9.4)}" style="position:absolute;left:96px;top:1500px"><span class="pill" style="background:{VERDE if i == 2 else CREMA};color:{NEGRO};font-size:40px">{lab}</span></div>' for i, (a, lab, _) in enumerate(stages))
rD = scene(f'''
<div data-scene="0,2.9" style="position:absolute;inset:0">
 <div class="c k" data-in="0" style="top:300px;color:{GRIS_D}">VIERNES 27/11 · BLACK FRIDAY</div>
 <div class="c d" data-punch=".15" data-shake=".15" style="top:420px;font-size:140px">Hoy todos venden.</div>
 <div class="c d" data-punch="1.2" data-shake="1.2" style="top:800px;font-size:140px;color:{GRIS_D}">¿Tu web llega al <span class="hl">próximo</span>?</div></div>
<div data-scene="2.9,9.5" style="position:absolute;inset:0">
 <div class="c k" style="top:200px;color:{GRIS_D}">TU LANDING PAGE, LISTA EN</div>
 <div style="position:absolute;left:70px;top:260px;width:480px;text-align:left"><span class="d o" data-count="3.0,8.0,1,7" style="font-size:520px;line-height:1;color:{CREMA}">1</span></div>
 <div class="d" style="position:absolute;left:96px;top:830px;font-size:84px;line-height:1">días<br>hábiles</div>
 <div style="position:absolute;left:96px;top:1080px;width:420px;height:16px;border-radius:8px;background:#2A2A2E;overflow:hidden"><div data-wk="3.0,0;8.0,100" style="height:100%;background:{VERDE}"></div></div>
 <div style="position:absolute;left:600px;top:300px;width:404px;height:784px;border-radius:56px;background:#1E1E21;padding:12px">
  <div style="position:relative;width:380px;height:760px;border-radius:46px;overflow:hidden;background:#E9E4D8">{phD}</div></div>
 {labD}
</div>
<div data-scene="9.5,16" style="position:absolute;inset:0;background:{CREMA}">
 <div class="c k" data-in="9.55" style="top:260px;color:{VERDE_TXT}">PLANES EN TRIWEB.COM.AR</div>
 <div data-in="9.7" style="position:absolute;left:96px;right:96px;top:350px;border-top:4px solid {NEGRO}">
  <div style="display:flex;justify-content:space-between;align-items:baseline;padding:40px 0;border-bottom:2px solid #CFC8B8"><span style="font-size:48px;font-weight:700;color:{NEGRO}">Landing page</span><span class="d" style="font-size:72px;color:{NEGRO}">7 días hábiles</span></div>
  <div style="display:flex;justify-content:space-between;align-items:baseline;padding:40px 0;border-bottom:2px solid #CFC8B8"><span style="font-size:48px;font-weight:700;color:{NEGRO}">Rediseño</span><span class="d" style="font-size:72px;color:{NEGRO}">desde $197.000</span></div></div>
 <div class="c" data-in="10.3" style="top:830px;font-size:30px;color:{GRIS}">Precio publicado en triweb.com.ar al 2/11/2026.</div>
 <div class="c d" data-in="10.9" style="top:960px;font-size:84px;color:{NEGRO}">El próximo Black Friday, <span class="hl">con web</span>.</div>
 {cta_block(11.6, NEGRO, GRIS, NEGRO, CREMA, 1220)}
</div>
''', NEGRO)

REELS = {  # nombre: (html, duración, segundo de portada)
    'confesion-logo-sura': (rA, 9.5, 2.2),
    'quiz-a-o-b-web': (rB, 15.0, 1.3),
    'novedad-ia-edits': (rC, 12.0, 2.6),
    'landing-7-dias-black-friday': (rD, 16.0, 8.5),
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
