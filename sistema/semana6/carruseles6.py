"""Semana del 23/11: antes/después en ventana de navegador (mar), paleta en 3 pasos (sáb), logo en 16 px (dom) e historias.
Esquemas de láminas nuevos (navegador con marcas numeradas, muestras de color + barra 60-30-10, escalera de tamaños). Nudo nuevo vía kit.mark_svg."""
import sys, pathlib
sys.path.insert(0, '/home/claude/triweb'); sys.path.insert(0, '/home/claude/triweb/semana5')
from kit import *
from carruseles5 import sig, X, story, NOTE
OUT = pathlib.Path('/home/claude/triweb/semana6/out/feed'); OUT.mkdir(parents=True, exist_ok=True)
SURA = '/home/claude/triweb/sura/src/'
OLIVA, TERRA, CREMA_S, NEGRO_S = '#72714D', '#A27850', '#EEE8DA', '#0A0A0A'
P = lambda top, txt, size=46, color=None, extra='': f'<div style="position:absolute;left:96px;right:96px;top:{top}px;font-size:{size}px;line-height:1.35;{f"color:{color};" if color else ""}{extra}">{txt}</div>'
K = lambda top, txt, color: f'<div class="k" style="position:absolute;left:96px;top:{top}px;color:{color}">{txt}</div>'
H = lambda top, txt, size=104, color=None: f'<div class="d" style="position:absolute;left:96px;right:96px;top:{top}px;font-size:{size}px;{f"color:{color};" if color else ""}">{txt}</div>'

# ---------------- MARTES 24 · Web · ANTES / DESPUÉS en ventana de navegador ----------------
def browser(inner, top=330, h=760, dark=False):
    bar = '#2A2A2E' if dark else '#D9D3C5'
    return (f'<div style="position:absolute;left:70px;right:70px;top:{top}px;height:{h}px;border-radius:26px;overflow:hidden;background:{bar};box-shadow:0 30px 60px rgba(0,0,0,.18)">'
            f'<div style="height:58px;display:flex;align-items:center;gap:12px;padding:0 24px">' + ''.join(f'<span style="width:16px;height:16px;border-radius:8px;background:{"#4A4A4E" if dark else "#B8B1A3"}"></span>' for _ in range(3))
            + f'<span style="margin-left:24px;flex:1;height:32px;border-radius:16px;background:{"#1A1A1D" if dark else "#EEE8DA"};font-size:18px;line-height:32px;padding-left:18px;color:#8A8478">tutienda.com.ar</span></div>'
            f'<div style="position:relative;height:{h-58}px">{inner}</div></div>')
def mark(n, x, y, bg, fg):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:64px;height:64px;border-radius:32px;background:{bg};color:{fg};font-size:34px;font-weight:800;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px rgba(255,255,255,.6)">{n}</div>'
ANTES = (f'<div style="position:absolute;inset:0;background:#F4F1EA"></div>'
         f'<div style="position:absolute;left:0;right:0;top:0;height:70px;display:flex;justify-content:space-around;align-items:center;font-size:20px;color:#9A9488;border-bottom:1px solid #DDD">Inicio · Empresa · Productos · Novedades · Contacto</div>'
         f'<div style="position:absolute;left:40px;right:40px;top:100px;height:300px;background:repeating-linear-gradient(45deg,#E2DDD2 0 18px,#D8D2C5 18px 36px);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:26px;color:#9A9488">foto de stock</div>'
         f'<div style="position:absolute;left:40px;right:40px;top:430px;text-align:center;font-family:Georgia,serif;font-size:46px;color:#8A8478">Bienvenidos a nuestra tienda</div>'
         f'<div style="position:absolute;left:80px;right:80px;top:510px;text-align:center;font-size:20px;line-height:1.5;color:#A8A29A">Ofrecemos productos de calidad con la mejor atención. Consulte precios por mensaje privado. Envíos a coordinar.</div>'
         f'<div style="position:absolute;left:0;right:0;top:620px;text-align:center"><span style="font-size:18px;color:#A8A29A;border:1px solid #C8C2B4;padding:8px 18px">Ver más</span></div>'
         + mark(1, 20, 100, NEGRO, CREMA) + mark(2, 830, 420, NEGRO, CREMA) + mark(3, 700, 520, NEGRO, CREMA) + mark(4, 560, 600, NEGRO, CREMA))
DESPUES = (f'<div style="position:absolute;inset:0;background:{NEGRO}"></div>'
           f'<div style="position:absolute;left:0;right:0;top:0;height:64px;background:{VERDE};color:{NEGRO};font-size:24px;font-weight:800;display:flex;align-items:center;justify-content:center;letter-spacing:.04em">BLACK FRIDAY · 20% OFF · HASTA EL DOMINGO 29/11</div>'
           f'<div class="d" style="position:absolute;left:44px;width:470px;top:110px;font-size:62px;color:{CREMA};line-height:1">Mates y bombillas hechos a mano.</div>'
           f'<div style="position:absolute;left:44px;width:450px;top:330px;font-size:24px;line-height:1.4;color:{GRIS_D}">Envío en 48 h a todo el país. Cambios sin vueltas.</div>'
           f'<div style="position:absolute;left:100px;top:440px;font-size:38px;font-weight:800;color:{CREMA}">Mate $ 24.000 <span style="color:{GRIS_D};font-weight:500;text-decoration:line-through;font-size:28px">$ 30.000</span></div>'
           f'<div style="position:absolute;left:100px;top:530px;background:{CREMA};color:{NEGRO};border-radius:999px;padding:18px 36px;font-size:26px;font-weight:800">Comprar por WhatsApp →</div>'
           f'<div style="position:absolute;right:44px;top:110px;width:330px;height:500px;border-radius:20px;background:linear-gradient(160deg,#6B4A2B,#3A2A1A)"></div>'
           f'<div style="position:absolute;right:64px;top:540px;font-size:18px;color:#D9C9B0">foto real del producto</div>'
           + mark(1, 12, 0, CREMA, NEGRO) + mark(2, 470, 100, CREMA, NEGRO) + mark(3, 12, 436, CREMA, NEGRO) + mark(4, 12, 534, CREMA, NEGRO))
N1 = 5
C1 = [('crema', f'''{K(140, 'ANTES / DESPUÉS · BLACK FRIDAY', GRIS)}
{H(230, 'Misma tienda. Mismo producto. <span class="hl">¿Cuál vende?</span>', 112)}
<div style="position:absolute;left:96px;right:96px;top:760px;display:flex;gap:24px">
 <div style="flex:1;height:300px;border-radius:24px;background:#FFFFFF;display:flex;align-items:flex-end;padding:26px;font-size:40px;font-weight:800;color:#8A8478">Antes</div>
 <div style="flex:1;height:300px;border-radius:24px;background:{NEGRO};display:flex;align-items:flex-end;padding:26px;font-size:40px;font-weight:800;color:{CREMA}">Después →</div></div>
{P(1110, 'Deslizá y fijate qué cambió.', 40, GRIS)}{sig(False, 1, N1)}'''),
 ('crema', f'''{K(120, 'ANTES', GRIS)}{H(180, 'Así entra tu cliente.', 72)}{browser(ANTES, 320, 720)}
{P(1080, '<b>1</b> Foto de stock · <b>2</b> “Bienvenidos” · <b>3</b> “Consulte precios” · <b>4</b> Un botón que no dice nada', 32, GRIS)}{sig(False, 2, N1)}'''),
 ('negro', f'''{K(120, 'DESPUÉS', VERDE)}{H(180, 'Así compra.', 72)}{browser(DESPUES, 320, 720, True)}
{P(1080, '<b style="color:{CREMA}">1</b> Promo con fecha de cierre · <b style="color:{CREMA}">2</b> Qué vendés, en una línea · <b style="color:{CREMA}">3</b> Precio a la vista · <b style="color:{CREMA}">4</b> Un botón que dice qué hacer', 32, GRIS_D)}{sig(True, 3, N1)}'''),
 ('crema', f'''{K(120, 'QUÉ CAMBIÓ', VERDE_TXT)}{H(190, '4 cambios. Ninguno es caro.', 92)}''' + ''.join(
    f'<div style="position:absolute;left:96px;right:96px;top:{470+i*170}px;height:150px;display:flex;align-items:center;gap:30px;border-top:3px solid {NEGRO}">'
    f'<span class="d o" style="font-size:110px;width:90px">{i+1}</span><div><div style="font-size:30px;color:{GRIS};text-decoration:line-through">{a}</div><div style="font-size:44px;font-weight:800;margin-top:6px">{b}</div></div></div>'
    for i, (a, b) in enumerate([('Foto de stock', 'Foto real de tu producto'), ('Bienvenidos', 'Qué vendés y por qué a vos'), ('Consulte precios', 'Precio a la vista'), ('Ver más', 'Comprar por WhatsApp →')]))
  + f'''{P(1170, 'Ejemplo ilustrativo.', 28, GRIS)}{sig(False, 4, N1)}'''),
 ('negro', f'''<div style="position:absolute;left:96px;top:150px">{mark_svg(CREMA, 150)}</div>
{H(390, '¿Tu web es la de <span class="hl">antes</span>?', 116)}
{P(700, 'La pasamos a la de después. Una landing page puede estar lista en 7 días hábiles.', 46, GRIS_D)}
<div style="position:absolute;left:96px;top:930px"><span class="pill" style="background:{CREMA};color:{NEGRO};font-size:42px;padding:26px 50px"><b>Consultanos</b> · Trabajemos juntos</span></div>
{P(1090, 'Planes en triweb.com.ar · link en la bio<br>Guardalo · Seguinos para más', 36, GRIS_D)}{sig(True, 5, N1)}'''),
]

# ---------------- SÁBADO 28 · Branding · TUTORIAL: la paleta de tu marca en 3 pasos ----------------
def sw(c, w, h, label, hexv, dark_txt):
    fg = NEGRO if dark_txt else CREMA
    return (f'<div style="width:{w}px;height:{h}px;border-radius:28px;background:{c};color:{fg};padding:26px 30px;display:flex;flex-direction:column;justify-content:flex-end;'
            f'{"border:3px solid #CFC8B8;" if c in (CREMA_S,) else ""}"><div style="font-size:36px;font-weight:800">{label}</div><div style="font-size:24px;opacity:.75;margin-top:4px">{hexv}</div></div>')
N2 = 7
C2 = [('negro', f'''{K(140, 'TUTORIAL · 3 PASOS', GRIS_D)}
{H(230, 'La paleta de tu marca, en <span class="hl">3 pasos</span>.', 118)}
<div style="position:absolute;left:96px;right:96px;top:760px;height:380px;display:flex;border-radius:30px;overflow:hidden">
 <div style="flex:6;background:{OLIVA}"></div><div style="flex:3;background:{CREMA_S}"></div><div style="flex:1;background:{TERRA}"></div></div>
{P(1160, 'Ejemplo real: proyecto de branding Sura Arquitectura.', 32, GRIS_D)}{sig(True, 1, N2)}'''),
 ('crema', f'''<div class="d o" style="position:absolute;left:80px;top:90px;font-size:300px;line-height:1;color:{NEGRO}">1</div>
{H(430, 'Elegí un color base.', 96)}
{P(560, 'Uno solo, que diga algo de tu rubro y tu forma de trabajar. No el que está de moda.', 44)}
<div style="position:absolute;left:96px;top:800px;display:flex;gap:40px;align-items:center">
 <div style="width:300px;height:300px;border-radius:150px;background:{OLIVA}"></div>
 <div style="font-size:38px;line-height:1.4;width:520px"><b>Sura: oliva.</b><br>Orgánico, como la palabra que guió su moodboard.</div></div>{sig(False, 2, N2)}'''),
 ('crema', f'''<div class="d o" style="position:absolute;left:80px;top:90px;font-size:300px;line-height:1;color:{NEGRO}">2</div>
{H(430, 'Sumá un acento y dos neutros.', 92)}
{P(650, 'El acento es para lo que querés que se vea primero. Los neutros, para leer tranquilo.', 40)}
<div style="position:absolute;left:96px;top:860px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;width:888px">
 {sw(TERRA, 282, 300, 'Acento', 'terracota', False)}{sw(CREMA_S, 282, 300, 'Neutro', 'crema', True)}{sw(NEGRO_S, 282, 300, 'Neutro', 'negro', False)}</div>{sig(False, 3, N2)}'''),
 ('crema', f'''<div class="d o" style="position:absolute;left:80px;top:90px;font-size:300px;line-height:1;color:{NEGRO}">3</div>
{H(430, 'Repartilos 60-30-10.', 96)}
{P(560, 'Así se ve ordenado, aunque no sepas de diseño.', 42)}''' + ''.join(
    f'<div style="position:absolute;left:96px;top:{720+i*150}px;width:888px;height:110px;display:flex;align-items:center;gap:26px">'
    f'<div style="width:{int(888*p/100*0.72)}px;height:110px;border-radius:20px;background:{c};{"border:3px solid #CFC8B8;" if c == CREMA_S else ""}"></div>'
    f'<div><div class="d" style="font-size:64px">{p}%</div><div style="font-size:28px;color:{GRIS}">{t}</div></div></div>'
    for i, (p, c, t) in enumerate([(60, OLIVA, 'base: fondos, carteles'), (30, CREMA_S, 'neutros: textos, papelería'), (10, TERRA, 'acento: detalles, botones')]))
  + f'{sig(False, 4, N2)}'),
 ('negro', f'''{K(140, 'APLICADO', GRIS_D)}{H(220, 'Así se ve cuando se respeta.', 92)}
<div style="position:absolute;left:96px;right:96px;top:470px;height:620px;border-radius:30px;background:url(file://{SURA}papeleria.png) center/cover"></div>
<div style="position:absolute;left:96px;top:1120px;display:flex;gap:14px">''' + ''.join(f'<span style="width:60px;height:60px;border-radius:30px;background:{c};border:3px solid #3A3A3E"></span>' for c in (OLIVA, CREMA_S, TERRA))
  + f'''<span style="font-size:30px;color:{GRIS_D};line-height:60px;margin-left:10px">Proyecto Sura Arquitectura</span></div>{sig(True, 5, N2)}'''),
 ('crema', f'''{K(140, 'EVITÁ', GRIS)}{H(220, '3 errores con los colores.', 96)}''' + ''.join(
    f'<div style="position:absolute;left:96px;right:96px;top:{500+i*210}px;padding-bottom:30px;border-bottom:3px solid {NEGRO}">'
    f'<div style="font-size:52px;font-weight:800;position:relative;display:inline-block">{a}<div style="position:absolute;left:-6px;right:-6px;top:52%;height:8px;background:{NEGRO}"></div></div>'
    f'<div style="font-size:36px;color:{GRIS};margin-top:12px">{b}</div></div>'
    for i, (a, b) in enumerate([('Usar 8 colores', 'Con 4 alcanza y sobra.'), ('Cambiarlos cada mes', 'La gente te reconoce por repetición.'), ('Elegir solo por gusto', 'Elegí por lo que querés transmitir.')]))
  + f'{sig(False, 6, N2)}'),
 ('negro', f'''<div style="position:absolute;left:96px;top:150px">{mark_svg(CREMA, 150)}</div>
{H(390, '¿Armamos la paleta de <span class="hl">tu marca</span>?', 112)}
{P(800, 'Logo, colores y tipografía con una idea detrás. Branding para negocios.', 46, GRIS_D)}
<div style="position:absolute;left:96px;top:990px"><span class="pill" style="background:{CREMA};color:{NEGRO};font-size:42px;padding:26px 50px"><b>Consultanos</b> · Trabajemos juntos</span></div>
{P(1140, 'Guardalo para cuando armes tu marca · Seguinos para más', 32, GRIS_D)}{sig(True, 7, N2)}'''),
]

# ---------------- DOMINGO 29 · Branding · ERROR + CORRECCIÓN: tu logo en 16 px ----------------
def emblem(size):
    """Emblema recargado de ejemplo (inventado): anillo con texto, rayos finos y dibujo con detalle."""
    rays = ''.join(f'<line x1="100" y1="100" x2="{100+70*__import__("math").cos(k*0.2618):.1f}" y2="{100+70*__import__("math").sin(k*0.2618):.1f}" stroke="#8A8478" stroke-width=".6"/>' for k in range(24))
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 200 200"><circle cx="100" cy="100" r="96" fill="none" stroke="#5A5650" stroke-width="2"/>'
            f'<circle cx="100" cy="100" r="88" fill="none" stroke="#5A5650" stroke-width=".8"/><circle cx="100" cy="100" r="66" fill="#E9E4D8" stroke="#5A5650" stroke-width="1"/>{rays}'
            f'<defs><path id="ring" d="M100,100 m-77,0 a77,77 0 1,1 154,0 a77,77 0 1,1 -154,0"/></defs>'
            f'<text font-size="9" fill="#5A5650" letter-spacing="2" font-family="Georgia"><textPath href="#ring">CALIDAD · TRADICIÓN · SERVICIO · EXCELENCIA · DESDE SIEMPRE ·</textPath></text>'
            f'<path d="M70 120 Q100 60 130 120 Z" fill="#B8B1A3" stroke="#5A5650" stroke-width=".8"/><circle cx="100" cy="95" r="10" fill="#8A8478"/>'
            f'<text x="100" y="140" text-anchor="middle" font-size="11" font-family="Georgia" fill="#5A5650">Mi Empresa S.A.</text></svg>')
def ladder(fn, sizes, fg):
    return ('<div style="position:absolute;left:96px;right:96px;top:470px;display:flex;align-items:flex-end;gap:46px">'
            + ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:20px">{fn(s)}<span style="font-size:28px;font-weight:700;color:{fg}">{s} px</span></div>' for s in sizes) + '</div>')
N3 = 6
C3 = [('crema', f'''{K(140, 'ERROR COMÚN · BRANDING', GRIS)}
<div style="position:absolute;left:70px;top:210px;display:flex;align-items:baseline;gap:20px"><span class="d o" style="font-size:440px;line-height:1;color:{NEGRO}">16</span><span class="d" style="font-size:120px;color:{GRIS}">px</span></div>
{H(740, 'Si tu logo no se lee acá, <span class="hl">no se lee</span>.', 104)}
{P(1090, 'Es el tamaño de la pestaña del navegador.', 40, GRIS)}{sig(False, 1, N3)}'''),
 ('crema', f'''{K(140, 'ERROR', GRIS)}{H(220, 'Mucho detalle.', 96)}{ladder(emblem, (360, 120, 40, 16), GRIS)}
{P(960, 'En grande se ve lindo. En el perfil de Instagram ya es una mancha, y en 16 px no se distingue nada.', 42)}
{P(1180, 'Ejemplo ilustrativo.', 28, GRIS)}{sig(False, 2, N3)}'''),
 ('negro', f'''{K(140, 'MEJOR ASÍ', VERDE)}{H(220, 'Formas simples.', 96)}{ladder(lambda s: mark_svg(CREMA, s), (360, 120, 40, 16), GRIS_D)}
{P(960, 'Pocas formas, buen contraste y un solo punto de color. Nuestro Nudo se reconoce en cualquier tamaño.', 42, GRIS_D)}{sig(True, 3, N3)}'''),
 ('crema', f'''{K(140, 'DÓNDE SE VE CHICO', GRIS)}{H(220, 'Tu logo vive en miniatura.', 96)}
<div style="position:absolute;left:96px;right:96px;top:480px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
 <div style="height:300px;border-radius:28px;background:#FFFFFF;padding:30px;display:flex;flex-direction:column;justify-content:space-between"><div style="width:130px;height:130px;border-radius:65px;background:{NEGRO};display:flex;align-items:center;justify-content:center">{mark_svg(CREMA, 90)}</div><b style="font-size:34px">Foto de perfil</b></div>
 <div style="height:300px;border-radius:28px;background:#FFFFFF;padding:30px;display:flex;flex-direction:column;justify-content:space-between"><div style="display:flex;align-items:center;gap:12px;background:#EEE8DA;border-radius:14px 14px 0 0;padding:14px 18px;width:330px">{mark_svg(NEGRO, 32)}<span style="font-size:24px;color:{GRIS}">Tu negocio</span></div><b style="font-size:34px">Pestaña del navegador</b></div>
 <div style="height:300px;border-radius:28px;background:#FFFFFF;padding:30px;display:flex;flex-direction:column;justify-content:space-between"><div style="width:330px;height:150px;border-radius:14px;background:#2A2A2E;position:relative"><div style="position:absolute;right:14px;bottom:12px;opacity:.85">{mark_svg(CREMA, 44)}</div></div><b style="font-size:34px">Sello en tus videos</b></div>
 <div style="height:300px;border-radius:28px;background:#FFFFFF;padding:30px;display:flex;flex-direction:column;justify-content:space-between"><div style="width:130px;height:130px;border-radius:65px;border:5px dashed {NEGRO};display:flex;align-items:center;justify-content:center">{mark_svg(NEGRO, 80, seed=NEGRO)}</div><b style="font-size:34px">Sello, bordado o etiqueta</b></div>
</div>{sig(False, 4, N3)}'''),
 ('crema', f'''{K(140, 'LA PRUEBA DE 1 MINUTO', VERDE_TXT)}{H(220, 'Hacela hoy con tu logo.', 96)}''' + ''.join(
    f'<div style="position:absolute;left:96px;right:96px;top:{480+i*210}px;display:flex;gap:34px;align-items:center">'
    f'<div style="flex:none;width:110px;height:110px;border-radius:24px;border:5px solid {NEGRO};display:flex;align-items:center;justify-content:center;font-size:56px;font-weight:900">✓</div>'
    f'<div><div style="font-size:46px;font-weight:800">{a}</div><div style="font-size:34px;color:{GRIS};margin-top:6px">{b}</div></div></div>'
    for i, (a, b) in enumerate([('Achicalo a 1 cm', '¿Se sigue entendiendo qué es?'), ('Pasalo a blanco y negro', '¿Funciona sin colores?'), ('Miralo 3 segundos de lejos', '¿Lo podrías dibujar de memoria?')]))
  + f'{P(1130, "Si fallaste en alguna, tu logo necesita una versión simple.", 32, GRIS)}{sig(False, 5, N3)}'),
 ('negro', f'''<div style="position:absolute;left:96px;top:150px">{mark_svg(CREMA, 150)}</div>
{H(390, 'Un logo que se lea <span class="hl">en todos lados</span>.', 112)}
{P(720, 'Diseñamos tu logo y sus versiones: grande, chica y en un color. Branding para negocios.', 46, GRIS_D)}
<div style="position:absolute;left:96px;top:950px"><span class="pill" style="background:{CREMA};color:{NEGRO};font-size:42px;padding:26px 50px"><b>Consultanos</b> · Trabajemos juntos</span></div>
{P(1110, 'Mandáselo a alguien que está por hacer su logo · Seguinos para más', 36, GRIS_D)}{sig(True, 6, N3)}'''),
]

# ---------------- HISTORIAS (1 por día, 13:00) + 2 con sticker para subir a mano ----------------
ST = {
 'lun-confesion': ('negro', f'''<div style="position:absolute;left:96px;top:420px;background:{CREMA};color:{NEGRO};font-weight:800;font-size:44px;padding:12px 26px;border-radius:14px;transform:rotate(-3deg)">confesión de diseñador:</div>
   {H(560, '“Tu logo no tiene que mostrar lo que vendés.”', 108)}{NOTE(GRIS_D, 'Te contamos por qué en el reel de hoy ↑')}'''),
 'mar-navegador': ('crema', f'''{browser('<div style="position:absolute;inset:0;background:#F4F1EA"></div><div style="position:absolute;left:0;right:0;top:220px;text-align:center;font-family:Georgia,serif;font-size:56px;color:#8A8478">Bienvenidos</div>', 380, 560)}
   {H(1010, 'Tu web el Black Friday: <span class="hl">¿antes o después?</span>', 92)}{NOTE(GRIS)}'''),
 'mie-quiz': ('negro', f'''<div style="position:absolute;left:96px;right:96px;top:420px;display:flex;gap:30px">
   <div class="d" style="flex:1;height:420px;border-radius:40px;background:#1E1E21;display:flex;align-items:center;justify-content:center;font-size:240px;color:{GRIS_D}">A</div>
   <div class="d" style="flex:1;height:420px;border-radius:40px;background:{CREMA};color:{NEGRO};display:flex;align-items:center;justify-content:center;font-size:240px">B</div></div>
   {H(930, '¿A cuál le escribís? Tenés 3 segundos.', 100)}{NOTE(GRIS_D, 'Jugá en el reel de hoy ↑')}'''),
 'jue-ia': ('negro', f'''<div style="position:absolute;left:0;right:0;top:400px;height:90px;border-top:3px solid #2A2A2E;border-bottom:3px solid #2A2A2E;overflow:hidden" class="k"><div style="white-space:nowrap;color:{GRIS_D};font-size:34px;line-height:84px;padding-left:40px">NOVEDAD · EDITS · NOVEDAD · EDITS · NOVEDAD · EDITS · NOVEDAD</div></div>
   {H(600, 'Instagram sumó una IA que te escribe los reels.', 110)}{P(1100, '¿Te sirve? Lo que hace y lo que no.', 44, GRIS_D)}{NOTE(GRIS_D)}'''),
 'vie-contador': ('negro', f'''{K(420, 'HOY · BLACK FRIDAY', GRIS_D)}<div style="position:absolute;left:70px;top:470px;display:flex;align-items:baseline;gap:30px"><span class="d o" style="font-size:520px;line-height:1;color:{CREMA}">7</span><span class="d" style="font-size:100px;line-height:1">días<br>hábiles</span></div>
   {H(1060, 'Lo que tarda tu landing page.', 96)}{NOTE(GRIS_D, 'Te mostramos cómo en el reel de hoy ↑')}'''),
 'sab-paleta': ('crema', f'''<div style="position:absolute;left:96px;right:96px;top:400px;height:560px;display:flex;flex-direction:column;border-radius:40px;overflow:hidden">
   <div style="flex:6;background:{OLIVA}"></div><div style="flex:3;background:{CREMA_S};border-left:3px solid #CFC8B8;border-right:3px solid #CFC8B8"></div><div style="flex:1;background:{TERRA}"></div></div>
   {H(1030, 'La paleta de tu marca en 3 pasos.', 100)}{NOTE(GRIS)}'''),
 'dom-16px': ('crema', f'''<div style="position:absolute;left:96px;top:420px;display:flex;align-items:flex-end;gap:50px">{emblem(300)}<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{emblem(16)}<span style="font-size:26px;font-weight:700;color:{GRIS}">16 px</span></div></div>
   {H(860, '¿Tu logo sobrevive en chiquito?', 104)}{P(1120, 'Hacé la prueba de 1 minuto en el post de hoy.', 42, GRIS)}{NOTE(GRIS)}'''),
 'sticker-encuesta-black-friday': ('negro', f'''{H(420, '¿Vendés algo este Black Friday?', 120)}
   {P(780, 'Votá ↓ (sí / no / todavía no sé)', 40, GRIS_D)}
   <div style="position:absolute;left:140px;right:140px;top:960px;height:320px;border:4px dashed #3A3A3E;border-radius:40px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#4A4A4E">sticker de encuesta</div>'''),
 'sticker-pregunta-tu-logo': ('crema', f'''{H(420, '¿Qué le cambiarías a tu <span class="hl">logo</span>?', 116)}
   {P(830, 'Contanos y te damos una idea en historias ↓', 40, GRIS)}
   <div style="position:absolute;left:140px;right:140px;top:1000px;height:300px;border:4px dashed #CFC8B8;border-radius:40px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#B5AE9E">sticker de pregunta</div>'''),
}

if __name__ == '__main__':
    pairs = []
    for name, slides in (('antes-despues-black-friday', C1), ('paleta-3-pasos', C2), ('logo-16-px', C3)):
        for i, (cls, inner) in enumerate(slides, 1):
            h = OUT / f'{name}-{i}.html'; h.write_text(page(inner, cls=cls, extra_css=X)); pairs.append((h, OUT / f'triweb-{name}-{i:02d}.png'))
    for name, (cls, inner) in ST.items():
        h = OUT / f'h-{name}.html'; h.write_text(story(inner, cls)); pairs.append((h, OUT / f'triweb-historia-{name}.png'))
    render(pairs); print('ok', len(pairs))
