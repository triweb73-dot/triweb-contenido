"""Semana del 30/11: checklist de diciembre en etiquetas de regalo (lun), reel de fin de año en 3 pasos con línea de tiempo (jue),
novedad "editar historias 15 min" con cronómetro gigante (dom) e historias. Esquemas de láminas nuevos. Nudo nuevo vía kit.mark_svg."""
import sys, pathlib
sys.path.insert(0, '/home/claude/triweb'); sys.path.insert(0, '/home/claude/triweb/semana5')
from kit import *
from carruseles5 import sig, X, story, NOTE
OUT = pathlib.Path('/home/claude/triweb/semana7/out/feed'); OUT.mkdir(parents=True, exist_ok=True)
P = lambda top, txt, size=46, color=None, extra='': f'<div style="position:absolute;left:96px;right:96px;top:{top}px;font-size:{size}px;line-height:1.35;{f"color:{color};" if color else ""}{extra}">{txt}</div>'
K = lambda top, txt, color: f'<div class="k" style="position:absolute;left:96px;top:{top}px;color:{color}">{txt}</div>'
H = lambda top, txt, size=104, color=None: f'<div class="d" style="position:absolute;left:96px;right:96px;top:{top}px;font-size:{size}px;{f"color:{color};" if color else ""}">{txt}</div>'
H2 = lambda top, txt, size=88: f'<div class="d" style="position:absolute;left:96px;right:330px;top:{top}px;font-size:{size}px">{txt}</div>'
XX = X + ' .tag{position:absolute;left:96px;right:96px;height:330px;clip-path:polygon(70px 0,100% 0,100% 100%,70px 100%,0 50%);padding:40px 50px 40px 150px}'

# ---------------- LUNES 30/11 · Web · CHECKLIST GUARDABLE en etiquetas de regalo ----------------
def cal():
    cells = ''
    for d in range(1, 32):
        hl = d == 24
        cells += (f'<div style="height:60px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700;'
                  f'{"background:" + VERDE + ";color:" + NEGRO if hl else "background:#1A1A1D;color:" + (GRIS_D if d < 24 else CREMA)}">{d}</div>')
    return (f'<div style="position:absolute;left:96px;right:96px;top:730px;display:grid;grid-template-columns:repeat(7,1fr);gap:12px">'
            f'<div style="grid-column:span 1"></div>{cells}</div>')
def tag(top, n, title, sub, dark=False):
    bg, fg, mu = (NEGRO, CREMA, GRIS_D) if dark else ('#FFFFFF', NEGRO, GRIS)
    return (f'<div class="tag" style="top:{top}px;background:{bg};color:{fg}">'
            f'<div style="position:absolute;left:64px;top:139px;width:52px;height:52px;border-radius:26px;background:{CREMA};border:5px solid {"#2A2A2E" if dark else "#D9D3C5"}"></div>'
            f'<div class="d o" style="position:absolute;right:46px;top:20px;font-size:150px;color:{"#3A3A3E" if dark else "#E2DCCD"};-webkit-text-stroke:4px {"#3A3A3E" if dark else "#D9D3C5"}">{n}</div>'
            f'<div style="position:relative;font-size:50px;font-weight:800;line-height:1.1;max-width:580px">{title}</div>'
            f'<div style="position:relative;font-size:32px;line-height:1.35;color:{mu};margin-top:18px;max-width:580px">{sub}</div></div>')
L = [('Horarios de fiestas, a la vista', 'En tu web y en tu ficha de Google: 24, 25, 31 y 1.'),
     ('Fecha límite para pedidos', '“Pedí hasta el 20/12 y llega para Navidad”, bien arriba.'),
     ('Ideas de regalo primero', 'Tus más vendidos en la primera pantalla, con foto real.'),
     ('Botón de WhatsApp en el celu', 'A un toque y sin buscarlo. Diciembre no espera.'),
     ('Precios actualizados', 'Si dice el precio de marzo, el cliente desconfía.'),
     ('Medios de pago claros', 'Transferencia, tarjeta, cuotas: decilo antes de que pregunten.')]
N1 = 6
C1 = [('negro', f'''{K(150, 'CHECKLIST · DICIEMBRE', VERDE)}
{H(220, 'Diciembre vende. ¿Tu web <span class="hl">está lista</span>?', 112)}
<div class="k" style="position:absolute;left:96px;top:680px;color:{GRIS_D};font-size:26px;display:grid;grid-template-columns:repeat(7,1fr);right:96px;text-align:center">{''.join(f'<span>{d}</span>' for d in 'LMMJVSD')}</div>
{cal()}{P(1140, '6 chequeos antes de las fiestas. Guardalo →', 38, GRIS_D)}{sig(True, 1, N1)}'''),
 ('crema', f'''{K(120, 'CHEQUEOS 1 Y 2', VERDE_TXT)}{tag(220, 1, *L[0])}{tag(600, 2, *L[1])}{P(1010, 'Lo primero que busca alguien en diciembre: si estás abierto y si llega a tiempo.', 36, GRIS)}{sig(False, 2, N1)}'''),
 ('crema', f'''{K(120, 'CHEQUEOS 3 Y 4', VERDE_TXT)}{tag(220, 3, *L[2])}{tag(600, 4, *L[3])}{P(1010, 'Quien compra un regalo quiere decidir rápido. Mostrale qué llevar y cómo pedirlo.', 36, GRIS)}{sig(False, 3, N1)}'''),
 ('crema', f'''{K(120, 'CHEQUEOS 5 Y 6', VERDE_TXT)}{tag(220, 5, *L[4], dark=True)}{tag(600, 6, *L[5], dark=True)}{P(1010, 'Menos dudas, menos mensajes de “¿precio?”, más ventas.', 36, GRIS)}{sig(False, 4, N1)}'''),
 ('negro', f'''{K(140, 'GUARDALO Y TACHÁ', GRIS_D)}{H(200, 'Tu lista de diciembre', 92)}''' + ''.join(
    f'<div style="position:absolute;left:96px;right:96px;top:{400+i*112}px;display:flex;align-items:center;gap:28px;font-size:42px;font-weight:700">'
    f'<span style="flex:none;width:62px;height:62px;border-radius:14px;border:5px solid {CREMA if i else VERDE};{"background:" + VERDE if i == 0 else ""};display:flex;align-items:center;justify-content:center;color:{NEGRO};font-size:40px">{"✓" if i == 0 else ""}</span>'
    f'<span style="{"text-decoration:line-through;text-decoration-color:" + VERDE + ";text-decoration-thickness:6px;color:" + GRIS_D if i == 0 else ""}">{t}</span></div>'
    for i, (t, _) in enumerate(L)) + f'''{P(1110, '¿Cuántos tildaste? Contanos en los comentarios.', 38, GRIS_D)}{sig(True, 5, N1)}'''),
 ('crema', f'''<div style="position:absolute;left:96px;top:150px">{mark_svg(NEGRO, 150)}</div>
{H(380, '¿Te faltan <span class="hl">varios</span>? Llegamos a tiempo.', 108)}
{P(740, 'Una landing page está lista en 7 días hábiles (dato de triweb.com.ar al 2/11/2026). Planes en triweb.com.ar, link en la bio.', 42, GRIS)}
<div style="position:absolute;left:96px;top:960px"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:42px;padding:26px 50px"><b style="color:{VERDE}">Consultanos</b> · Trabajemos juntos</span></div>
{P(1110, 'Mandáselo a alguien que vende online · Seguinos para más', 34, GRIS)}{sig(False, 6, N1)}'''),
]

# ---------------- JUEVES 03/12 · Video · TUTORIAL 3 PASOS: tu reel de fin de año con el celu (línea de tiempo) ----------------
def clip(w, label, dark=True, hl=False):
    bg = VERDE if hl else ('#2A2A2E' if dark else '#FFFFFF')
    fg = NEGRO if hl else (CREMA if dark else NEGRO)
    return (f'<div style="flex:none;width:{w}px;height:150px;border-radius:18px;background:{bg};color:{fg};padding:16px 18px;display:flex;flex-direction:column;justify-content:space-between;'
            f'background-image:repeating-linear-gradient(90deg,transparent 0 {w//4-2}px,rgba(127,127,127,.18) {w//4-2}px {w//4}px)">'
            f'<span style="font-size:20px;font-weight:700;opacity:.7">3 s</span><span style="font-size:26px;font-weight:800;line-height:1.1">{label}</span></div>')
def timeline(top, clips, dark=True, playhead=None):
    ruler = ''.join(f'<span style="flex:1;border-left:2px solid {"#3A3A3E" if dark else "#CFC8B8"};height:{20 if k % 5 == 0 else 10}px"></span>' for k in range(30))
    ph = (f'<div style="position:absolute;left:{playhead}px;top:-30px;bottom:-20px;width:6px;background:{VERDE};border-radius:3px">'
          f'<div style="position:absolute;left:-13px;top:0;width:32px;height:32px;border-radius:8px;background:{VERDE}"></div></div>') if playhead is not None else ''
    return (f'<div style="position:absolute;left:70px;right:70px;top:{top}px;border-radius:28px;background:{"#141416" if dark else "#E9E4D8"};padding:30px 28px">'
            f'<div style="display:flex;align-items:flex-end;margin-bottom:18px">{ruler}</div>'
            f'<div style="position:relative;display:flex;gap:10px;overflow:hidden">{"".join(clips)}{ph}</div>'
            f'<div style="margin-top:14px;height:56px;border-radius:12px;background:{"#1E1E21" if dark else "#DDD6C6"};display:flex;align-items:center;padding-left:18px;gap:4px">'
            + ''.join(f'<span style="width:6px;border-radius:3px;height:{10+(k*37 % 34)}px;background:{"#4A4A4E" if dark else "#B8B1A3"}"></span>' for k in range(60)) + '</div></div>')
TOMAS = ['Tu local abriendo', 'Tu producto estrella', 'Tus manos trabajando', 'Un pedido saliendo', 'El brindis del equipo (de espaldas vale)']
N2 = 6
C2 = [('negro', f'''{K(150, 'TUTORIAL · 3 PASOS · CON EL CELU', VERDE)}
{H(220, 'Tu reel de <span class="hl">fin de año</span>, en 3 pasos.', 116)}
{timeline(760, [clip(200, 'Local'), clip(200, 'Producto', hl=True), clip(200, 'Manos'), clip(200, 'Pedido'), clip(200, 'Brindis')], True, 205)}
{P(1150, 'Sin cámara, sin programa y sin mostrar la cara.', 38, GRIS_D)}{sig(True, 1, N2)}'''),
 ('crema', f'''<div class="d o" style="position:absolute;right:70px;top:60px;font-size:300px;line-height:1;color:{NEGRO};-webkit-text-stroke:5px {NEGRO}">1</div>
{K(140, 'PASO 1', VERDE_TXT)}{H2(200, 'Grabá 5 tomas de 3 segundos.')}''' + ''.join(
    f'<div style="position:absolute;left:96px;right:96px;top:{560+i*96}px;display:flex;align-items:center;gap:24px;font-size:40px;font-weight:700">'
    f'<span style="flex:none;width:56px;height:56px;border-radius:12px;background:{NEGRO};color:{CREMA};display:flex;align-items:center;justify-content:center;font-size:30px">{i+1}</span>{t}</div>'
    for i, t in enumerate(TOMAS)) + f'''{P(1070, 'Celu en vertical, con luz de ventana y la lente limpia.', 36, GRIS)}{sig(False, 2, N2)}'''),
 ('negro', f'''<div class="d o" style="position:absolute;right:70px;top:60px;font-size:300px;line-height:1;color:{CREMA};-webkit-text-stroke:5px {CREMA}">2</div>
{K(140, 'PASO 2', VERDE)}{H2(200, 'Arrancá con la toma <span class="hl">más linda</span>.')}
{timeline(560, [clip(220, 'Producto', hl=True), clip(180, 'Local'), clip(180, 'Manos'), clip(180, 'Pedido'), clip(180, 'Brindis')], True, 12)}
<div style="position:absolute;left:96px;top:930px;display:flex;align-items:center;gap:20px;font-size:36px;font-weight:700;color:{VERDE}">← la movés al principio</div>
{P(1030, 'Los primeros 2 segundos deciden si te miran. Cortá cada toma justo cuando pasa algo.', 38, GRIS_D)}{sig(True, 3, N2)}'''),
 ('crema', f'''<div class="d o" style="position:absolute;right:70px;top:60px;font-size:300px;line-height:1;color:{NEGRO};-webkit-text-stroke:5px {NEGRO}">3</div>
{K(140, 'PASO 3', VERDE_TXT)}{H2(200, 'Texto grande y música de Instagram.')}
<div style="position:absolute;left:96px;top:540px;width:330px;height:590px;border-radius:44px;background:{NEGRO};padding:12px">
 <div style="position:relative;width:100%;height:100%;border-radius:34px;overflow:hidden;background:linear-gradient(160deg,#6B4A2B,#2A1E14)">
  <div class="d" style="position:absolute;left:24px;right:24px;top:150px;font-size:44px;color:{CREMA};line-height:1.05">Gracias por este <span class="hl">2026</span>.</div>
  <div style="position:absolute;left:24px;right:24px;top:330px;font-size:22px;color:{CREMA};opacity:.8">Nos vemos en enero con novedades.</div>
  <div style="position:absolute;left:20px;bottom:24px;font-size:18px;color:{CREMA};opacity:.8">♪ audio de la biblioteca</div></div></div>
<div style="position:absolute;left:480px;right:96px;top:560px;font-size:36px;line-height:1.4">
 <b>Una frase, no un párrafo.</b><br><span style="color:{GRIS}">Que se lea sin sonido.</span><br><br>
 <b>Música desde la app.</b><br><span style="color:{GRIS}">Elegila en la biblioteca de Instagram: así no te silencian el video.</span><br><br>
 <b>Cerrá con qué viene.</b><br><span style="color:{GRIS}">Horarios de enero, una novedad, una promo.</span></div>
{sig(False, 4, N2)}'''),
 ('negro', f'''{K(140, 'EVITÁ', GRIS_D)}{H(200, 'Lo que hace que lo pasen de largo', 88)}''' + ''.join(
    f'<div style="position:absolute;left:96px;right:96px;top:{560+i*130}px;font-size:46px;font-weight:700;color:{GRIS_D}">'
    f'<span style="text-decoration:line-through;text-decoration-color:{CREMA};text-decoration-thickness:6px">{t}</span></div>'
    for i, t in enumerate(['Arrancar con el logo', 'Videos horizontales', 'Tomas de 10 segundos', 'Música subida desde otra app'])) + f'''
{P(1110, 'Guardalo para grabar esta semana.', 38, VERDE)}{sig(True, 5, N2)}'''),
 ('crema', f'''<div style="position:absolute;left:96px;top:150px">{mark_svg(NEGRO, 150)}</div>
{H(380, '¿Grabaste y no sabés <span class="hl">editar</span>?', 112)}
{P(720, 'Mandanos tus tomas y las convertimos en reels con tu marca. Edición de video para negocios.', 44, GRIS)}
<div style="position:absolute;left:96px;top:960px"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:42px;padding:26px 50px"><b style="color:{VERDE}">Consultanos</b> · Trabajemos juntos</span></div>
{P(1110, 'Mandáselo a alguien con negocio · Seguinos para más', 34, GRIS)}{sig(False, 6, N2)}'''),
]

# ---------------- DOMINGO 06/12 · Community manager · DATO / NOVEDAD: editar historias hasta 15 minutos después ----------------
def story_mock(left, top, w=380, h=680, edited=True):
    return (f'<div style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px;border-radius:44px;background:#1E1E21;padding:12px">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:34px;overflow:hidden;background:linear-gradient(170deg,#3A3A3E,#141416)">'
            f'<div style="position:absolute;left:18px;right:18px;top:16px;height:6px;border-radius:3px;background:rgba(242,236,221,.35)"><div style="width:40%;height:100%;background:{CREMA};border-radius:3px"></div></div>'
            f'<div style="position:absolute;left:18px;top:36px;display:flex;align-items:center;gap:10px"><span style="width:40px;height:40px;border-radius:20px;background:{CREMA};display:flex;align-items:center;justify-content:center">{mark_svg(NEGRO, 30)}</span><span style="font-size:18px;color:{CREMA};font-weight:700">tunegocio</span></div>'
            + (f'<div style="position:absolute;right:18px;top:42px;font-size:18px;font-weight:700;color:{NEGRO};background:{VERDE};padding:4px 12px;border-radius:8px">Editada</div>' if edited else '')
            + f'<div style="position:absolute;left:30px;right:30px;top:250px;text-align:center"><span style="background:{CREMA};color:{NEGRO};font-size:27px;font-weight:800;padding:6px 12px;border-radius:10px;line-height:1.7;white-space:nowrap">Abrimos el 24<br>hasta las <s style="color:#A8A29A">20 h</s> 14 h</span></div>'
            f'</div></div>')
N3 = 5
C3 = [('negro', f'''{K(150, 'NOVEDAD DE INSTAGRAM · NOV 2026', VERDE)}
<div class="d o" style="position:absolute;left:80px;top:230px;font-size:330px;line-height:1;color:{CREMA};-webkit-text-stroke:5px {CREMA}">15:00</div>
{H(640, 'Minutos para <span class="hl">arreglar</span> tu historia.', 104)}
{P(1000, 'Ya podés editar una historia publicada sin perder vistas ni respuestas.', 42, GRIS_D)}{sig(True, 1, N3)}'''),
 ('crema', f'''{K(140, 'QUÉ PODÉS CAMBIAR', VERDE_TXT)}{H(200, 'Hasta 15 minutos después de publicarla:', 76)}
{story_mock(600, 430)}''' + ''.join(
    f'<div style="position:absolute;left:96px;width:460px;top:{450+i*120}px;display:flex;align-items:center;gap:22px;font-size:44px;font-weight:800">'
    f'<span style="flex:none;width:58px;height:58px;border-radius:29px;background:{VERDE};display:flex;align-items:center;justify-content:center;font-size:32px">✓</span>{t}</div>'
    for i, t in enumerate(['Texto', 'Música', 'Stickers', 'Dibujos'])) + f'''
<div style="position:absolute;left:96px;width:460px;top:950px;display:flex;align-items:center;gap:22px;font-size:38px;font-weight:700;color:{GRIS}">
 <span style="flex:none;width:58px;height:58px;border-radius:29px;border:4px solid {GRIS};display:flex;align-items:center;justify-content:center;font-size:30px">✕</span>La foto o el video</div>
{sig(False, 2, N3)}'''),
 ('negro', f'''{K(140, 'CÓMO SE HACE', GRIS_D)}{H(200, 'Tres toques', 100)}''' + ''.join(
    f'<div style="position:absolute;left:96px;right:96px;top:{440+i*200}px;display:flex;gap:34px;align-items:center">'
    f'<span class="d o" style="flex:none;width:120px;font-size:150px;line-height:1;color:{VERDE if i == 2 else CREMA};-webkit-text-stroke:4px {VERDE if i == 2 else CREMA}">{i+1}</span>'
    f'<span style="font-size:46px;font-weight:700;line-height:1.2">{t}</span></div>'
    for i, t in enumerate(['Abrí tu historia.', 'Tocá los tres puntos, abajo a la derecha.', '“Editar historia”. Va a decir “Editada”.'])) + f'''
{P(1090, 'Se está habilitando de a poco: si no lo ves, actualizá la app.', 34, GRIS_D)}{sig(True, 3, N3)}'''),
 ('crema', f'''{K(140, 'CÓMO APROVECHARLO EN TU NEGOCIO', VERDE_TXT)}{H(200, 'Corregí, no rehagas.', 104)}''' + ''.join(
    f'<div style="position:absolute;left:96px;right:96px;top:{470+i*190}px;background:#FFFFFF;border-radius:28px;padding:30px 36px">'
    f'<div style="font-size:42px;font-weight:800">{a}</div><div style="font-size:32px;color:{GRIS};margin-top:8px">{b}</div></div>'
    for i, (a, b) in enumerate([('El precio o el horario mal escrito', 'Lo arreglás y la historia sigue sumando vistas.'),
                                ('El sticker que te olvidaste', 'Sumá el link o la encuesta después.'),
                                ('Revisá antes de los 15 minutos', 'Pasado ese tiempo, hay que borrarla y subirla de nuevo.')])) + f'''{sig(False, 4, N3)}'''),
 ('negro', f'''<div style="position:absolute;left:96px;top:150px">{mark_svg(CREMA, 150)}</div>
{H(380, 'Tus historias, <span class="hl">todos los días</span>.', 112)}
{P(720, 'Las pensamos, las diseñamos y las publicamos por vos. Community manager para negocios.', 44, GRIS_D)}
<div style="position:absolute;left:96px;top:960px"><span class="pill" style="background:{CREMA};color:{NEGRO};font-size:42px;padding:26px 50px"><b>Consultanos</b> · Trabajemos juntos</span></div>
{P(1110, 'Guardalo y mandáselo a quien sube tus historias · Seguinos para más', 34, GRIS_D)}{sig(True, 5, N3)}'''),
]

# ---------------- HISTORIAS (1 por día, 13:00) + 2 con sticker para subir a mano ----------------
ST = {
 'lun-etiqueta': ('crema', f'''{tag(420, 1, 'Horarios de fiestas, a la vista', 'En tu web y en tu ficha de Google.')}
   {H(860, '¿Tu web sabe que es diciembre?', 104)}{NOTE(GRIS, '6 chequeos en el post de hoy ↑')}'''),
 'mar-mito': ('negro', f'''<div style="position:absolute;left:150px;right:150px;top:380px;height:560px;border-radius:44px;background:{CREMA};color:{NEGRO};padding:60px;transform:rotate(-4deg)">
   <div class="k" style="color:{GRIS}">MITO</div><div class="d" style="margin-top:30px;font-size:84px">“Más colores, más llamativo.”</div></div>
   {H(1040, '¿Verdad o mito?', 110)}{NOTE(GRIS_D, 'La respuesta, en el reel de hoy ↑')}'''),
 'mie-vs': ('negro', f'''<div style="position:absolute;left:96px;right:96px;top:420px;display:flex;align-items:center;gap:30px">
   <div style="flex:1;height:420px;border-radius:40px;background:#1E1E21;padding:40px;display:flex;flex-direction:column;gap:18px">''' + ''.join(f'<div style="height:60px;border-radius:30px;border:3px solid #3A3A3E"></div>' for _ in range(4)) + f'''</div>
   <span class="d" style="font-size:80px;color:{VERDE}">vs</span>
   <div style="flex:1;height:420px;border-radius:40px;background:{CREMA};padding:30px"><div class="d" style="font-size:40px;color:{NEGRO}">tunegocio<br>.com.ar</div><div style="margin-top:30px;height:150px;border-radius:20px;background:#D9D3C5"></div></div></div>
   {H(940, '¿Página de links o tu web?', 104)}{NOTE(GRIS_D, 'Las comparamos en el reel de hoy ↑')}'''),
 'jue-timeline': ('negro', f'''{timeline(420, [clip(180, 'Local'), clip(180, 'Producto', hl=True), clip(180, 'Manos'), clip(180, 'Brindis')], True, 200)}
   {H(860, 'Tu reel de fin de año, sin saber editar.', 100)}{NOTE(GRIS_D, '3 pasos en el post de hoy ↑')}'''),
 'vie-faq': ('crema', f'''<div style="position:absolute;left:96px;right:96px;top:420px;background:#FFFFFF;border-radius:30px;padding:36px 40px;display:flex;justify-content:space-between;align-items:center;font-size:44px;font-weight:800">¿Cuánto tarda mi web?<span style="color:{VERDE_TXT};font-size:60px">+</span></div>
   <div style="position:absolute;left:96px;right:96px;top:590px;background:#FFFFFF;border-radius:30px;padding:36px 40px;display:flex;justify-content:space-between;align-items:center;font-size:44px;font-weight:800">¿Y si ya tengo una?<span style="color:{VERDE_TXT};font-size:60px">+</span></div>
   {H(860, 'Lo que más nos preguntan, respondido.', 100)}{NOTE(GRIS, 'En el reel de hoy ↑')}'''),
 'sab-grilla': ('negro', f'''<div style="position:absolute;left:96px;right:96px;top:380px;display:grid;grid-template-columns:1fr 1fr;gap:20px">''' + ''.join(
    f'<div style="height:250px;border-radius:26px;background:{c};display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:800;color:{f};font-family:{ff}">Helados</div>'
    for c, f, ff in [('#E84A8A', '#FFF', 'Georgia,serif'), ('#3A7BD5', '#FFEB3B', 'Impact,sans-serif'), ('#F2C94C', '#7B3F00', 'cursive'), ('#FFFFFF', '#2E7D32', 'Courier New,monospace')]) + f'''</div>
   {H(960, '4 piezas, 4 marcas distintas. ¿Te pasa?', 100)}{NOTE(GRIS_D, 'El después, en el reel de hoy ↑')}'''),
 'dom-15': ('negro', f'''<div class="d o" style="position:absolute;left:80px;top:400px;font-size:300px;line-height:1;color:{CREMA};-webkit-text-stroke:5px {CREMA}">15:00</div>
   {H(800, 'Ahora podés editar tu historia después de subirla.', 96)}{NOTE(GRIS_D, 'Cómo, en el post de hoy ↑')}'''),
 'sticker-encuesta-diciembre': ('negro', f'''{H(420, '¿Tu web está lista para diciembre?', 116)}
   {P(880, 'Votá ↓ (sí / más o menos / no tengo web)', 40, GRIS_D)}
   <div style="position:absolute;left:140px;right:140px;top:1000px;height:300px;border:4px dashed #3A3A3E;border-radius:40px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#4A4A4E">sticker de encuesta</div>'''),
 'sticker-pregunta-web': ('crema', f'''{H(420, '¿Qué te gustaría preguntarle a una <span class="hl">agencia</span>?', 96)}
   {P(860, 'Mandá tu duda y te respondemos en historias ↓', 40, GRIS)}
   <div style="position:absolute;left:140px;right:140px;top:1020px;height:280px;border:4px dashed #CFC8B8;border-radius:40px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#B5AE9E">sticker de pregunta</div>'''),
}

if __name__ == '__main__':
    pairs = []
    for name, slides in (('checklist-diciembre', C1), ('reel-fin-de-ano-3-pasos', C2), ('editar-historias-15-min', C3)):
        for i, (cls, inner) in enumerate(slides, 1):
            h = OUT / f'{name}-{i}.html'; h.write_text(page(inner, cls=cls, extra_css=XX)); pairs.append((h, OUT / f'triweb-{name}-{i:02d}.png'))
    for name, (cls, inner) in ST.items():
        h = OUT / f'h-{name}.html'; h.write_text(story(inner, cls).replace('</style>', XX + '</style>', 1)); pairs.append((h, OUT / f'triweb-historia-{name}.png'))
    render(pairs); print('ok', len(pairs))
