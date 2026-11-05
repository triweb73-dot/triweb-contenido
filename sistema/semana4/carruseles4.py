"""Semana del 9/11: carrusel checklist (martes), carrusel quiz (sábado) e historias. Esquemas de láminas nuevos; Nudo nuevo vía mark_svg."""
import sys, pathlib
sys.path.insert(0, '/home/claude/triweb')
from kit import *
OUT = pathlib.Path('/home/claude/triweb/semana4/out/feed'); OUT.mkdir(parents=True, exist_ok=True)

def sig(dark, i=None, n=None):
    c = GRIS_D if dark else GRIS
    s = (f'<div style="position:absolute;left:96px;bottom:66px;display:flex;align-items:center;gap:12px">{mark_svg(CREMA if dark else NEGRO, 44)}'
         f'<span style="font-size:26px;font-weight:600;color:{c}">@triweb_73</span></div>')
    if i: s += f'<div class="num" style="right:96px;bottom:74px;color:{c}">{i}/{n}</div>'
    return s

def box(size, checked=True, dark=False):
    line = CREMA if dark else NEGRO
    tick = (f'<svg viewBox="0 0 100 100" width="{size*.78}" height="{size*.78}"><path d="M18 52 L42 74 L84 26" fill="none" stroke="{NEGRO}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>') if checked else ''
    bg = VERDE if checked else 'transparent'
    return (f'<div style="width:{size}px;height:{size}px;border-radius:{size*.22}px;border:{max(6,size*.06)}px solid {line if not checked else VERDE};background:{bg};'
            f'display:flex;align-items:center;justify-content:center;flex:none">{tick}</div>')

# ---------------- CHECKLIST · martes 10 ----------------
CH = [('Carga rápido en el celular', 'Abrila con datos, no con wifi. Si tarda, mucha gente se va antes de ver la oferta.'),
      ('WhatsApp a un toque', 'El botón se ve sin bajar y abre el chat con un mensaje listo. Probalo vos.'),
      ('La promo, arriba de todo', 'Un banner con el descuento y la fecha de cierre. Que nadie tenga que buscarla.'),
      ('Precios a la vista', 'Mostrá el precio o un "desde". "Consultar precio" frena la compra.'),
      ('Una compra de prueba', 'Hacé un pedido de punta a punta: formulario, pago y mensaje de confirmación.'),
      ('Envíos y cambios claros', 'Plazos, costos y cómo cambiar, en una página fácil de encontrar.')]
N1 = 9
S1 = [('negro', f'''
<div style="position:absolute;left:96px;top:120px" class="k">{''}</div>
<div style="position:absolute;left:96px;top:140px;font-size:30px;font-weight:700;letter-spacing:.12em;color:{VERDE}">CHECKLIST PARA GUARDAR</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:250px;font-size:128px;line-height:1.1">¿Tu web aguanta el <span class="hl">Black Friday</span>?</div>
<div style="position:absolute;left:96px;right:96px;top:800px;font-size:42px;color:{GRIS_D};line-height:1.35">Pasó el CyberMonday. Antes de la próxima fecha fuerte, revisá estas 6 cosas.</div>
<div style="position:absolute;left:96px;top:1030px;display:flex;gap:18px">{box(84)}{box(84)}{box(84)}{box(84, False, True)}{box(84, False, True)}{box(84, False, True)}</div>
{sig(True, 1, N1)}''')]
for i, (t, d) in enumerate(CH):
    S1.append(('crema', f'''
<div style="position:absolute;left:96px;top:120px;font-size:30px;font-weight:700;letter-spacing:.12em;color:{VERDE_TXT}">CHEQUEO {i+1} DE 6</div>
<div style="position:absolute;left:96px;top:250px">{box(230)}</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:560px;font-size:104px">{t}</div>
<div style="position:absolute;left:96px;right:96px;top:{820 if len(t) < 24 else 920}px;font-size:44px;line-height:1.38;color:#3A3833">{d}</div>
<div class="d" style="position:absolute;right:70px;top:120px;font-size:200px;color:#E3DCCB">0{i+1}</div>
{sig(False, i+2, N1)}'''))
rows = ''.join(f'<div style="display:flex;align-items:center;gap:28px;padding:26px 0;border-bottom:2px solid #2A2A2E">{box(64)}<span style="font-size:44px;font-weight:600">{t}</span></div>' for t, _ in CH)
S1.append(('negro', f'''
<div style="position:absolute;left:96px;top:120px;font-size:30px;font-weight:700;letter-spacing:.12em;color:{VERDE}">RESUMEN · GUARDALO</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:200px;font-size:88px">Tu web, lista para vender.</div>
<div style="position:absolute;left:96px;right:96px;top:420px">{rows}</div>
<div style="position:absolute;left:96px;right:96px;top:1130px;font-size:34px;color:{GRIS_D}">Mandáselo a alguien que tenga tienda online.</div>
{sig(True, 8, N1)}'''))
S1.append(('crema', f'''
<div style="position:absolute;left:96px;top:150px">{mark_svg(NEGRO, 150)}</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:380px;font-size:112px">¿Algo no pasó el chequeo?</div>
<div style="position:absolute;left:96px;right:96px;top:690px;font-size:46px;line-height:1.35">Lo revisamos y lo arreglamos. Desarrollo web para negocios que venden.</div>
<div style="position:absolute;left:96px;top:900px"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:42px;padding:26px 50px"><b style="color:{VERDE}">Consultanos</b> · Trabajemos juntos</span></div>
<div style="position:absolute;left:96px;top:1060px;font-size:36px;color:{GRIS}">Planes en triweb.com.ar · link en la bio<br>Seguinos para más</div>
{sig(False, 9, N1)}'''))

# ---------------- QUIZ · sábado 14 ----------------
Q = ['¿Usás siempre los mismos 2 o 3 colores?', '¿Tu logo funciona en un solo color?',
     '¿Tus posts, tu local y tus presupuestos usan la misma letra?', '¿Alguien reconocería un post tuyo sin ver el nombre?',
     '¿Podés decir en una frase qué te hace distinto?']
N2 = 8
def dots(k):
    return '<div style="display:flex;gap:14px">' + ''.join(f'<div style="width:{60 if j == k else 22}px;height:22px;border-radius:11px;background:{VERDE if j == k else (CREMA if j < k else "#2A2A2E")}"></div>' for j in range(5)) + '</div>'
S2 = [('crema', f'''
<div style="position:absolute;left:96px;top:140px;font-size:30px;font-weight:700;letter-spacing:.12em;color:{VERDE_TXT}">QUIZ DE BRANDING · 5 PREGUNTAS</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:240px;font-size:150px;line-height:1.1">¿Tu marca <span class="hl">aprueba</span>?</div>
<div style="position:absolute;left:150px;top:720px;width:420px;height:300px;background:{NEGRO};border-radius:36px;transform:rotate(-6deg);display:flex;align-items:center;justify-content:center" class="d"><span style="font-size:150px;color:{VERDE}">SÍ</span></div>
<div style="position:absolute;left:520px;top:760px;width:420px;height:300px;background:#FFFFFF;border-radius:36px;transform:rotate(5deg);display:flex;align-items:center;justify-content:center;box-shadow:0 20px 40px rgba(0,0,0,.08)" class="d"><span style="font-size:150px;color:{NEGRO}">NO</span></div>
<div style="position:absolute;left:96px;right:96px;top:1120px;font-size:38px;color:{GRIS}">Contá cuántas veces respondés SÍ. Deslizá →</div>
{sig(False, 1, N2)}''')]
for k, q in enumerate(Q):
    S2.append(('negro', f'''
<div style="position:absolute;left:96px;top:130px">{dots(k)}</div>
<div style="position:absolute;right:96px;top:122px;font-size:30px;font-weight:700;color:{GRIS_D}">PREGUNTA {k+1}</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:280px;font-size:{100 if len(q) < 44 else 88}px">{q}</div>
<div style="position:absolute;left:96px;right:96px;top:820px;display:flex;gap:32px">
 <div style="flex:1;height:250px;border-radius:36px;background:{VERDE};color:{NEGRO};display:flex;flex-direction:column;justify-content:center;padding:0 40px"><div class="d" style="font-size:96px">SÍ</div><div style="font-size:30px;font-weight:600">+1 punto</div></div>
 <div style="flex:1;height:250px;border-radius:36px;border:4px solid #3A3A3E;color:{CREMA};display:flex;flex-direction:column;justify-content:center;padding:0 40px"><div class="d" style="font-size:96px">NO</div><div style="font-size:30px;color:{GRIS_D}">0 puntos</div></div></div>
{sig(True, k+2, N2)}'''))
TIERS = [('5', 'Marca sólida.', 'Cuidala: usala siempre igual.'), ('3–4', 'Vas bien.', 'Con un manual de marca simple, cerrás lo que falta.'), ('0–2', 'Hay que ordenar.', 'Tu negocio merece una marca que se recuerde.')]
tiers = ''.join(f'<div style="display:flex;gap:36px;align-items:center;background:{"#FFFFFF" if i else NEGRO};color:{CREMA if i == 0 else NEGRO};border-radius:32px;padding:34px 40px;margin-bottom:26px">'
                f'<div class="d" style="font-size:96px;width:220px;color:{VERDE if i == 0 else NEGRO}">{s}</div><div><div class="d" style="font-size:54px">{h}</div>'
                f'<div style="font-size:32px;margin-top:8px;color:{GRIS_D if i == 0 else GRIS}">{d}</div></div></div>' for i, (s, h, d) in enumerate(TIERS))
S2.append(('crema', f'''
<div style="position:absolute;left:96px;top:130px;font-size:30px;font-weight:700;letter-spacing:.12em;color:{VERDE_TXT}">TU RESULTADO</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:200px;font-size:96px">¿Cuántos SÍ sumaste?</div>
<div style="position:absolute;left:96px;right:96px;top:440px">{tiers}</div>
<div style="position:absolute;left:96px;right:96px;top:1150px;font-size:34px;color:{GRIS}">Contanos tu puntaje en los comentarios.</div>
{sig(False, 7, N2)}'''))
S2.append(('verdebg', f'''
<div style="position:absolute;left:0;right:0;top:170px;display:flex;justify-content:center">{mark_svg(NEGRO, 260, seed=CREMA)}</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:520px;font-size:104px;text-align:center">Branding para negocios que quieren que los recuerden.</div>
<div style="position:absolute;left:0;right:0;top:960px;text-align:center"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:42px;padding:26px 50px"><b>Consultanos</b> · Trabajemos juntos</span></div>
<div style="position:absolute;left:0;right:0;top:1110px;text-align:center;font-size:34px;font-weight:600">Guardalo · Seguinos para más · @triweb_73</div>'''))

# ---------------- HISTORIAS (1080×1920, contenido fuera de los 340 px inferiores) ----------------
def story(inner, cls):
    return page(inner + f'<div style="position:absolute;left:96px;top:120px;display:flex;align-items:center;gap:14px">{mark_svg(CREMA if cls == "negro" else NEGRO, 60)}'
                f'<span style="font-size:30px;font-weight:600;color:{GRIS_D if cls == "negro" else GRIS}">@triweb_73</span></div>', 1080, 1920, cls)
NOTE = lambda c: f'<div style="position:absolute;left:96px;right:96px;top:1420px;font-size:38px;color:{c}">Nuevo post en el perfil ↑</div>'
ST = {
 'lun-mitos': ('negro', f'''<div class="d" style="position:absolute;left:96px;right:96px;top:420px;font-size:150px;color:{GRIS}"><span style="text-decoration:line-through;text-decoration-color:{VERDE};text-decoration-thickness:16px">"Una web es carísima."</span></div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:1000px;font-size:90px">3 mitos que te frenan de tener web.</div>{NOTE(GRIS_D)}'''),
 'mar-checklist': ('crema', f'''<div style="position:absolute;left:96px;top:420px">{box(300)}</div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:820px;font-size:110px">6 chequeos antes del Black Friday.</div>
   <div style="position:absolute;left:96px;right:96px;top:1220px;font-size:42px;color:{GRIS}">Guardalo para tu web.</div>{NOTE(GRIS)}'''),
 'mie-antes-despues': ('crema', f'''<div style="position:absolute;left:0;top:380px;width:540px;height:900px;background:#D9D3C5"></div><div style="position:absolute;left:540px;top:380px;width:540px;height:900px;background:{NEGRO}"></div>
   <div class="d" style="position:absolute;left:60px;top:780px;font-size:96px;color:{GRIS}">Antes</div><div class="d" style="position:absolute;left:600px;top:780px;font-size:96px;color:{VERDE}">Después</div>
   <div style="position:absolute;left:534px;top:380px;width:12px;height:900px;background:{VERDE}"></div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:1330px;font-size:64px">Misma web, ¿cuál te escribe?</div>'''),
 'jue-dalinger': ('crema', f'''<div style="position:absolute;left:96px;top:420px;font-size:32px;font-weight:700;letter-spacing:.12em;color:{VERDE_TXT}">CASO REAL · DALINGER AUTOMOTORES</div>
   <div class="d" style="position:absolute;left:96px;top:520px;font-size:260px">+1.500</div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:820px;font-size:90px">seguidores en el primer año.</div>
   <div style="position:absolute;left:96px;right:96px;top:1100px;font-size:40px;color:{GRIS}">Mirá cómo lo hicimos en el carrusel de hoy.</div>{NOTE(GRIS)}'''),
 'vie-novedad': ('negro', f'''<div style="position:absolute;left:0;right:0;top:400px;height:100px;background:{VERDE};color:{NEGRO};font-size:44px;font-weight:800;letter-spacing:.12em;line-height:100px;padding-left:96px">NOVEDAD INSTAGRAM</div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:640px;font-size:116px">Lo original llega a más gente.</div>
   <div style="position:absolute;left:96px;right:96px;top:1120px;font-size:44px;color:{GRIS_D}">3 cosas para hacer en tu negocio.</div>{NOTE(GRIS_D)}'''),
 'sab-quiz': ('negro', f'''<div class="d" style="position:absolute;left:96px;right:96px;top:420px;font-size:120px">¿Tu marca aprueba?</div>
   <div style="position:absolute;left:96px;right:96px;top:800px;display:flex;gap:30px"><div class="d" style="flex:1;height:300px;border-radius:40px;background:{VERDE};color:{NEGRO};font-size:140px;display:flex;align-items:center;justify-content:center">SÍ</div>
   <div class="d" style="flex:1;height:300px;border-radius:40px;border:5px solid #3A3A3E;font-size:140px;display:flex;align-items:center;justify-content:center">NO</div></div>
   <div style="position:absolute;left:96px;right:96px;top:1200px;font-size:44px;color:{GRIS_D}">Quiz de 5 preguntas en el feed.</div>'''),
 'dom-google': ('crema', f'''<div class="d" style="position:absolute;left:96px;right:96px;top:420px;font-size:110px">¿Te encuentran en Google?</div>
   <div style="position:absolute;left:96px;right:96px;top:820px;height:140px;background:#FFFFFF;border-radius:70px;display:flex;align-items:center;padding:0 50px;font-size:46px;gap:26px"><div style="width:46px;height:46px;border:7px solid {GRIS};border-radius:50%"></div>tu rubro + tu barrio</div>
   <div style="position:absolute;left:96px;right:96px;top:1060px;font-size:44px;color:{GRIS}">3 pasos para aparecer, en el reel de hoy.</div>{NOTE(GRIS)}'''),
 # para subir a mano con sticker (dejan lugar libre al centro-abajo)
 'sticker-encuesta-web': ('negro', f'''<div class="d" style="position:absolute;left:96px;right:96px;top:420px;font-size:116px">¿Tu web carga rápido en el celular?</div>
   <div style="position:absolute;left:96px;right:96px;top:860px;font-size:40px;color:{GRIS_D}">Abrila ahora con datos y votá ↓</div>
   <div style="position:absolute;left:140px;right:140px;top:1040px;height:300px;border:4px dashed #3A3A3E;border-radius:40px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#4A4A4E">sticker de encuesta</div>'''),
 'sticker-pregunta-marca': ('crema', f'''<div class="d" style="position:absolute;left:96px;right:96px;top:420px;font-size:116px">Preguntanos lo que quieras sobre tu <span class="hl">marca</span>.</div>
   <div style="position:absolute;left:96px;right:96px;top:900px;font-size:40px;color:{GRIS}">Respondemos en historias ↓</div>
   <div style="position:absolute;left:140px;right:140px;top:1040px;height:300px;border:4px dashed #CFC8B8;border-radius:40px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#B5AE9E">sticker de pregunta</div>'''),
}

if __name__ == '__main__':
    pairs = []
    for name, slides in (('checklist-black-friday', S1), ('quiz-marca', S2)):
        for i, (cls, inner) in enumerate(slides, 1):
            h = OUT / f'{name}-{i}.html'; h.write_text(page(inner, cls=cls)); pairs.append((h, OUT / f'triweb-{name}-{i:02d}.png'))
    for name, (cls, inner) in ST.items():
        h = OUT / f'h-{name}.html'; h.write_text(story(inner, cls)); pairs.append((h, OUT / f'triweb-historia-{name}.png'))
    render(pairs); print('ok', len(pairs))
