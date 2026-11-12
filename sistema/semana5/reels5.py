"""Semana del 16/11: 4 reels nuevos. Cada uno con layout, ritmo y música propios.
A error+corrección (split screen, barridos, sello con temblor) · B POV estilo app de Notas (texto palabra por palabra)
C detrás de escena Sura (números gigantes con contorno, zoom lento, cortes al beat) · D novedad Instagram (celular con grilla)."""
import sys, pathlib, subprocess, shutil
sys.path.insert(0, '/home/claude/triweb'); sys.path.insert(0, '/home/claude/triweb/semana4')
from kit import *
from reels4 import JS as JS4, CSS as CSS4

OUT = pathlib.Path('/home/claude/triweb/semana5/out'); OUT.mkdir(parents=True, exist_ok=True)
FPS = 30
SURA = '/home/claude/triweb/sura/src/'
JS_EXTRA = """<script>
document.querySelectorAll('[data-words]').forEach(el=>{el.innerHTML=el.innerHTML.split(' ').map(w=>'<span class=w>'+w+'</span>').join(' ');});
const _r4=render;
render=function(t){_r4(t);
 document.querySelectorAll('[data-words]').forEach(el=>{const [a,s]=el.dataset.words.split(',').map(Number);const o=out(el,t);
   el.querySelectorAll('.w').forEach((w,i)=>{const p=ease((t-a-i*s)/.12);w.style.opacity=p*o;w.style.display='inline-block';w.style.transform=`translateY(${(1-p)*18}px)`;});});
 document.querySelectorAll('[data-kb]').forEach(el=>{const [a,b,s0,s1]=el.dataset.kb.split(',').map(Number);el.style.transform=`scale(${s0+(s1-s0)*cl((t-a)/(b-a))})`;});
 document.querySelectorAll('[data-wipe]').forEach(el=>{const a=+el.dataset.wipe,p=ease((t-a)/.3);el.style.clipPath=`inset(0 ${100-p*100}% 0 0)`;el.style.opacity=t>=a?1:0;});
 document.querySelectorAll('[data-strike]').forEach(el=>{const a=+el.dataset.strike;el.style.width=(ease((t-a)/.25)*100)+'%';});
};
render(0);
</script>"""
CSS = CSS4 + ' .w{opacity:0} .o{color:transparent;-webkit-text-stroke:5px currentColor}'

def scene(inner, cls='negro', bg=None):
    return page(inner + JS4 + JS_EXTRA, 1080, 1920, cls, extra_css=CSS + 'body{background:%s}' % (bg or (CREMA if cls == 'crema' else NEGRO)))

def cta(a, txt, sub, dark=True):
    fg, mut = (CREMA, GRIS_D) if dark else (NEGRO, GRIS)
    return (f'<div data-cover="{a}" style="position:absolute;inset:0;background:{NEGRO if dark else CREMA}"></div>'
            f'<div class="c d" data-in="{a+.15}" style="top:420px;font-size:128px;color:{fg}">{txt}</div>'
            f'<div class="c" data-in="{a+.45}" style="top:980px;font-size:42px;color:{mut};line-height:1.4">{sub}</div>'
            f'<div class="c" data-pop="{a+.7}" style="top:1210px;display:flex;align-items:center;justify-content:space-between">'
            f'<span class="pill" style="background:{VERDE};color:{NEGRO};font-size:40px;padding:24px 44px"><b>Consultanos</b> · Trabajemos juntos</span>{mark_svg(fg, 120)}</div>'
            f'<div class="c" data-in="{a+.8}" style="top:1400px;font-size:32px;color:{mut}">@triweb_73</div>')

# ===== A · Lunes 16 · Web · ERROR COMÚN + CORRECCIÓN · split screen negro/crema · synthwave 100 bpm =====
ERR = [  # (inicio, fin, error_html, mejor_html)
 (2.4, 5.4, f'<div style="font-size:150px;font-weight:800;color:{GRIS_D};line-height:1;position:relative;display:inline-block;letter-spacing:-.03em">Bienvenidos<div data-strike="3.3" style="position:absolute;left:0;top:50%;height:16px;background:{CREMA};width:0"></div></div><div style="font-size:60px;color:{GRIS};margin-top:20px">a nuestra página web</div>',
            f'<div class="d" style="font-size:96px;color:{NEGRO}">Muebles a medida.<br><span class="hl">Entrega en 15 días.</span></div><div style="font-size:36px;color:{GRIS};margin-top:22px">Decí qué hacés en la primera línea.</div>'),
 (5.4, 8.4, ''.join(f'<div style="height:76px;border:3px solid #3A3A3E;border-radius:14px;margin-bottom:16px;padding:0 26px;font-size:34px;line-height:70px;color:#6F6A60">{f}</div>' for f in ['Nombre', 'Apellido', 'Email', 'Teléfono', 'Empresa', 'Asunto']),
            f'<div class="d" style="font-size:92px;color:{NEGRO}">Un botón.<br>Un toque.</div><div style="margin-top:34px"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:44px;padding:26px 46px">Escribinos por WhatsApp →</span></div>'),
 (8.4, 11.4, f'<div style="display:flex;gap:18px">' + ''.join(f'<div style="flex:1;height:440px;border-radius:22px;background:#2A2A2E;display:flex;align-items:center;justify-content:center;font-size:30px;color:#6F6A60;font-weight:700;letter-spacing:.1em">STOCK</div>' for _ in range(3)) + '</div>',
            f'<div class="d" style="font-size:88px;color:{NEGRO}">Fotos reales de <span class="hl">tu trabajo</span>.</div><div style="display:flex;gap:16px;margin-top:30px">'
            + ''.join(f'<div style="flex:1;height:250px;border-radius:18px;background:url(file://{SURA}{f}) center/cover"></div>' for f in ['local.png', 'cartel-obra.png', 'carpeta.png']) + '</div>'),
]
partsA = ''
for k, (a, b, e, m) in enumerate(ERR):
    partsA += (f'<div data-scene="{a},{b}" style="position:absolute;inset:0">'
               f'<div style="position:absolute;left:0;right:0;top:0;height:960px;background:{NEGRO}">'
               f'<div class="c k" style="top:200px;color:{GRIS_D}">ERROR {k+1} DE 3</div>'
               f'<div class="c" data-in="{a+.05}" style="top:330px">{e}</div>'
               f'<div data-pop="{a+.9}" data-shake="{a+.9}" style="position:absolute;right:80px;top:170px;transform-origin:center"><div style="border:7px solid {CREMA};color:{CREMA};border-radius:16px;padding:6px 26px;font-size:54px;font-weight:900;letter-spacing:.1em;transform:rotate(-8deg)">ERROR</div></div></div>'
               f'<div data-wipe="{a+1.4}" style="position:absolute;left:0;right:0;top:960px;height:960px;background:{CREMA}">'
               f'<div class="c k" style="top:70px;color:{VERDE_TXT}">MEJOR ASÍ</div><div class="c" style="top:150px">{m}</div></div></div>')
rA = scene(f'''
<div data-scene="0,2.4" style="position:absolute;inset:0">
<div class="c d" data-punch=".05" data-shake=".05" style="top:560px;font-size:140px">Tu web comete este error.</div>
<div class="c d" data-in=".7" style="top:1040px;font-size:90px;color:{GRIS_D}">Y te cuesta <span class="hl">clientes</span>.</div>
<div class="c k" data-in="1.2" style="top:1320px;color:{GRIS_D}">3 ERRORES · 3 ARREGLOS</div></div>
{partsA}
{cta(11.4, '¿Tu web hace alguno?', 'Los arreglamos con vos.<br>Desarrollo web para negocios · triweb.com.ar')}
''')

# ===== B · Miércoles 18 · TRIAL_REEL · Web · POV estilo app de Notas · palabra por palabra · chiptune 150 bpm =====
ITEMS = ['1. Te busca en Google.', '2. Entra a tu web desde el celu.', '3. Busca el precio.', '4. Si no lo encuentra, se va con otro.']
itemsB = ''.join(f'<div data-words="{2.0 + i*1.45:.2f},.09" data-out="8.3" style="font-size:{68 if i < 3 else 76}px;font-weight:{500 if i < 3 else 800};margin-bottom:58px;line-height:1.25;color:{NEGRO}">{t}</div>' for i, t in enumerate(ITEMS))
rB = scene(f'''
<div style="position:absolute;left:0;right:0;top:0;height:1920px;background:#FBF8F1"></div>
<div data-out="8.3" style="position:absolute;left:70px;right:70px;top:170px;display:flex;justify-content:space-between;font-size:40px;color:{VERDE_TXT};font-weight:600"><span>‹ Notas</span><span>Listo</span></div>
<div data-in="0" data-out="8.3" style="position:absolute;left:96px;right:96px;top:290px;font-size:30px;color:{GRIS}">POV: faltan 9 días para el Black Friday</div>
<div class="d" data-type=".15,1.3" data-out="8.3" data-txt="Lo que hace tu cliente antes de comprarte:" style="position:absolute;left:96px;right:96px;top:360px;font-size:92px;color:{NEGRO};letter-spacing:-.02em;line-height:1.05"></div>
<div data-out="8.3" style="position:absolute;left:96px;right:96px;top:800px">{itemsB}</div>
<div data-pop="6.9" data-shake="6.9" data-out="8.3" style="position:absolute;left:96px;top:1480px"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:40px">Viernes 27/11 · Black Friday</span></div>
<div data-cover="8.3" style="position:absolute;inset:0;background:{NEGRO}"></div>
<div class="c d" data-punch="8.45" style="top:440px;font-size:150px;color:{CREMA}">¿Tu web pasa <span class="hl">los 4</span>?</div>
<div class="c" data-in="8.8" style="top:900px;font-size:42px;color:{GRIS_D};line-height:1.4">Mandáselo a alguien que vende online.</div>
<div class="c" data-pop="9.1" style="top:1120px;display:flex;align-items:center;justify-content:space-between"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:40px;padding:24px 44px"><b>Consultanos</b> · Trabajemos juntos</span>{mark_svg(CREMA, 120)}</div>
<div class="c" data-in="9.2" style="top:1300px;font-size:32px;color:{GRIS_D}">@triweb_73</div>
''', 'crema', '#FBF8F1')

# ===== C · Jueves 19 · Branding · DETRÁS DE ESCENA (proyecto Sura) · números con contorno, zoom lento, cortes al beat · boom bap 90 bpm =====
BEAT = 60/90
STEPS = [(2.4, 5.1, '01', 'Investigar', 'Referencias, estilo y paleta en un moodboard.', 'moodboard.png'),
         (5.1, 7.8, '02', 'Dibujar', 'Un símbolo con historia: un pájaro sobre una viga.', 'logo-negro.png'),
         (7.8, 10.5, '03', 'Ordenar', 'Colores y letra que se repiten siempre.', 'logo-verde.png')]
partsC = ''
for a, b, n, t, d, img in STEPS:
    sw = ''
    if n == '03':
        sw = '<div style="position:absolute;right:40px;top:40px;display:flex;gap:16px">' + ''.join(
            f'<div data-pop="{a+.6+j*.2:.2f}" style="width:110px;height:110px;border-radius:55px;background:{c};border:4px solid {CREMA}"></div>' for j, c in enumerate(['#4E5532', '#B07A56', '#EDE6D6', '#1E1E1E'])) + '</div>'
    partsC += (f'<div data-scene="{a},{b}" style="position:absolute;inset:0">'
               f'<div style="position:absolute;left:60px;right:60px;top:300px;height:900px;border-radius:40px;overflow:hidden;background:#222">'
               f'<div data-kb="{a},{b},1.0,1.12" style="position:absolute;inset:0;background:url(file://{SURA}{img}) center/cover"></div>{sw}</div>'
               f'<div class="d o" data-punch="{a}" style="position:absolute;left:70px;top:130px;font-size:230px;color:{CREMA}">{n}</div>'
               f'<div class="c d" data-in="{a+.15}" style="top:1250px;font-size:96px">{t}</div>'
               f'<div class="c" data-in="{a+.35}" style="top:1370px;font-size:40px;color:{GRIS_D}">{d}</div></div>')
APPS = ['cartel-obra.png', 'local.png', 'carpeta.png', 'casco.png', 'tubo.png', 'celular.png']
cuts = ''.join(f'<div data-scene="{10.5 + i*BEAT/1.5:.2f},{(10.5 + (i+1)*BEAT/1.5) if i < 5 else 13.4:.2f}" style="position:absolute;left:60px;right:60px;top:300px;height:900px;border-radius:40px;overflow:hidden;background:url(file://{SURA}{f}) center/cover"></div>' for i, f in enumerate(APPS))
rC = scene(f'''
<div data-scene="0,2.4" style="position:absolute;inset:0;background:{CREMA}">
<div class="c k" data-in="0" style="top:300px;color:{VERDE_TXT}">DETRÁS DE ESCENA · BRANDING</div>
<div class="c d" data-punch=".1" data-shake=".1" style="top:400px;font-size:140px;color:{NEGRO}">Un logo no se hace en una tarde.</div>
<div class="c" data-in=".8" style="top:1060px;font-size:44px;color:{GRIS};line-height:1.35">Así trabajamos una marca, paso a paso.<br>Proyecto: Sura Arquitectura.</div></div>
{partsC}
<div data-scene="10.5,13.4" style="position:absolute;inset:0">
<div class="d o" data-punch="10.5" style="position:absolute;left:70px;top:130px;font-size:230px;color:{CREMA}">04</div>
{cuts}
<div class="c d" data-in="10.65" style="top:1250px;font-size:96px">Aplicar</div>
<div class="c" data-in="10.85" style="top:1370px;font-size:40px;color:{GRIS_D}">Obra, local, papelería y redes: todo habla igual.</div></div>
{cta(13.4, 'Tu marca, con proceso.', 'Branding para negocios que quieren que los recuerden.')}
''')

# ===== D · Sábado 21 · Community manager · NOVEDAD INSTAGRAM · celular con grilla y zoom · afro house 118 bpm =====
def tile(i):
    c = [NEGRO, '#D9D3C5', '#2A2A2E', '#C9C3B5', NEGRO, '#E3DCCB', '#3A3A3E', '#D9D3C5'][i % 8]
    return f'<div style="background:{c};aspect-ratio:4/5"></div>'
grid = ''.join(tile(i) for i in range(8))
phone = (f'<div data-in="2.6" data-out="7.2" style="position:absolute;left:250px;top:560px;width:580px;height:1000px;border-radius:70px;background:{NEGRO};padding:22px;overflow:hidden">'
         f'<div style="width:100%;height:100%;border-radius:50px;background:#FBF8F1;overflow:hidden;position:relative"><div data-zk="2.6,1;4.4,1;5.0,1.18;6.6,1.18;7.0,1" style="transform-origin:0% 30%">'
         f'<div style="display:flex;align-items:center;gap:20px;padding:56px 30px 20px"><div style="width:110px;height:110px;border-radius:55px;background:{CREMA};display:flex;align-items:center;justify-content:center;border:3px solid {NEGRO}">{mark_svg(NEGRO, 76)}</div>'
         f'<div><div style="font-size:28px;font-weight:700;color:{NEGRO}">tu_negocio</div><div style="font-size:20px;color:{GRIS}">Publicaciones · Seguidores</div></div></div>'
         f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;margin-top:20px;position:relative">'
         f'<div data-pop="4.4" data-shake="4.4" style="aspect-ratio:4/5;background:{VERDE};display:flex;flex-direction:column;justify-content:flex-end;padding:10px;font-size:17px;font-weight:700;color:{NEGRO}">@tucliente<br>te etiquetó</div>{grid}</div></div></div></div>')
TIPS = ['Pedí que te etiqueten.', 'Sumá las mejores a tu grilla.', 'Agradecé en historias.']
tipsD = ''.join(f'<div data-scene="{7.2 + i*1.0:.1f},{7.2 + (i+1)*1.0:.1f}" style="position:absolute;inset:0;background:{NEGRO}"><div class="d o" data-punch="{7.2 + i*1.0:.1f}" style="position:absolute;left:96px;top:300px;font-size:300px;color:{CREMA}">{i+1}</div>'
                f'<div class="c d" data-words="{7.3 + i*1.0:.1f},.07" style="top:720px;font-size:120px">{t}</div></div>' for i, t in enumerate(TIPS))
rD = scene(f'''
<div data-scene="0,2.6" style="position:absolute;inset:0">
<div class="c" data-pop="0" style="top:300px"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:34px">NOVEDAD DE INSTAGRAM</span></div>
<div class="c d" data-words=".15,.08" style="top:440px;font-size:116px">Los posts donde te etiquetan ahora pueden ir a tu perfil.</div>
<div class="c" data-in="1.6" style="top:1250px;font-size:38px;color:{GRIS_D}">Se está habilitando de a poco.</div></div>
<div data-cover="2.5" data-out="7.15" style="position:absolute;inset:0;background:{CREMA}"></div>
<div class="c d" data-in="2.7" data-out="7.1" style="top:250px;font-size:76px;color:{NEGRO}">Lo que publican tus clientes, <span class="hl">en tu grilla</span>.</div>
{phone}
{tipsD}
{cta(10.2, 'Tu Instagram, al día.', 'Community manager para negocios: planificamos, publicamos y respondemos.')}
''')

REELS = {  # nombre: (html, duración, segundo de portada)
    'error-web-3-segundos': (rA, 14.0, 1.5),
    'pov-black-friday-notas': (rB, 10.5, 1.9),
    'detras-marca-sura': (rC, 16.0, 1.6),
    'novedad-grilla-etiquetas': (rD, 12.6, 2.0),
}

def make(name):
    html, secs, cover = REELS[name]
    d = OUT / name; fr = d / 'frames'; shutil.rmtree(fr, ignore_errors=True); fr.mkdir(parents=True)
    h = d / 'reel.html'; h.write_text(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(h.resolve().as_uri()); pg.wait_for_timeout(800)
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
