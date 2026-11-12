"""Semana del 16/11: carrusel comparación (mar), preguntas frecuentes en formato chat (vie), lista de tomas (dom) e historias.
Esquemas de láminas nuevos (rondas con marcador, burbujas de chat, storyboard). Nudo nuevo vía kit.mark_svg."""
import sys, pathlib
sys.path.insert(0, '/home/claude/triweb')
from kit import *
OUT = pathlib.Path('/home/claude/triweb/semana5/out/feed'); OUT.mkdir(parents=True, exist_ok=True)
X = '.o{color:transparent;-webkit-text-stroke:6px currentColor} .k{font-size:30px;font-weight:700;letter-spacing:.12em}'
A = lambda **k: ';'.join(f'{a.replace("_","-")}:{v}' for a, v in k.items())

def sig(dark, i=None, n=None):
    c = GRIS_D if dark else GRIS
    s = (f'<div style="position:absolute;left:96px;bottom:66px;display:flex;align-items:center;gap:12px">{mark_svg(CREMA if dark else NEGRO, 44)}'
         f'<span style="font-size:26px;font-weight:600;color:{c}">@triweb_73</span></div>')
    if i: s += f'<div class="num" style="right:96px;bottom:74px;color:{c}">{i}/{n}</div>'
    return s

# ---------------- MARTES 17 · COMPARACIÓN · Solo Instagram vs. Instagram + web ----------------
R = [('Cuando te buscan en Google', 'Google muestra poco de tu Instagram.', 'Tu web puede aparecer cuando buscan tu rubro y tu barrio.'),
     ('Tus precios y tu catálogo', 'Se pierden entre posts. Hay que preguntar por mensaje.', 'Ordenados, con fotos y precios a la vista.'),
     ('Las reglas del juego', 'Si cambia el algoritmo, cambia tu alcance.', 'Es tu espacio: decidís qué se ve y cómo.'),
     ('La confianza', 'Cualquiera puede abrir una cuenta.', 'Dominio propio y datos claros: se nota que sos un negocio en serio.')]
N1 = 7
C1 = [('negro', f'''
<div class="k" style="position:absolute;left:96px;top:140px;color:{VERDE}">COMPARACIÓN · 4 RONDAS</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:240px;font-size:112px">¿Te alcanza con <span class="hl">Instagram</span>?</div>
<div style="position:absolute;left:96px;right:96px;top:590px;height:150px;border-radius:30px;background:#1E1E21;display:flex;align-items:center;padding:0 44px;font-size:48px;font-weight:700;color:{GRIS_D}">Solo Instagram</div>
<div class="d o" style="position:absolute;left:0;right:0;top:745px;text-align:center;font-size:190px;color:{CREMA};z-index:2">VS</div>
<div style="position:absolute;left:96px;right:96px;top:990px;height:150px;border-radius:30px;background:{CREMA};color:{NEGRO};display:flex;align-items:center;padding:0 44px;font-size:48px;font-weight:800">Instagram + web</div>
{sig(True, 1, N1)}''')]
for i, (t, ig, web) in enumerate(R):
    C1.append(('crema', f'''
<div class="k" style="position:absolute;left:96px;top:120px;color:{VERDE_TXT}">RONDA {i+1}</div>
<div style="position:absolute;right:96px;top:104px;background:{NEGRO};color:{CREMA};border-radius:18px;padding:10px 24px;font-size:34px;font-weight:800">{i} – {i+1}</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:210px;font-size:96px">{t}</div>
<div style="position:absolute;left:96px;right:96px;top:520px;background:#FFFFFF;border-radius:32px;padding:40px 44px">
  <div style="font-size:28px;font-weight:700;letter-spacing:.1em;color:{GRIS}">SOLO INSTAGRAM</div>
  <div style="font-size:46px;line-height:1.3;color:{GRIS};margin-top:14px">{ig}</div></div>
<div style="position:absolute;left:96px;right:96px;top:850px;background:{NEGRO};color:{CREMA};border-radius:32px;padding:40px 44px">
  <div style="font-size:28px;font-weight:700;letter-spacing:.1em;color:{VERDE}">INSTAGRAM + WEB · GANA</div>
  <div style="font-size:50px;line-height:1.28;font-weight:700;margin-top:14px">{web}</div></div>
{sig(False, i+2, N1)}'''))
C1.append(('negro', f'''
<div class="k" style="position:absolute;left:96px;top:140px;color:{GRIS_D}">RESULTADO FINAL</div>
<div style="position:absolute;left:0;right:0;top:250px;display:flex;justify-content:center;align-items:center;gap:40px">
  <div class="d o" style="font-size:330px;color:#3A3A3E">0</div><div class="d" style="font-size:150px;color:{GRIS_D}">–</div><div class="d" style="font-size:330px;color:{VERDE}">4</div></div>
<div class="d" style="position:absolute;left:96px;right:96px;top:830px;font-size:92px">Instagram atrae. <span class="hl">La web cierra.</span></div>
<div style="position:absolute;left:96px;right:96px;top:1080px;font-size:44px;line-height:1.35;color:{GRIS_D}">Lo ideal es tener las dos, trabajando juntas.</div>
{sig(True, 6, N1)}'''))
C1.append(('crema', f'''
<div style="position:absolute;left:96px;top:150px">{mark_svg(NEGRO, 150)}</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:380px;font-size:112px">Sumá tu web a tu Instagram.</div>
<div style="position:absolute;left:96px;right:96px;top:690px;font-size:46px;line-height:1.35">Una landing page puede estar lista en 7 días hábiles.</div>
<div style="position:absolute;left:96px;top:900px"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:42px;padding:26px 50px"><b style="color:{VERDE}">Consultanos</b> · Trabajemos juntos</span></div>
<div style="position:absolute;left:96px;top:1060px;font-size:36px;color:{GRIS};line-height:1.45">Planes en triweb.com.ar · link en la bio<br>Guardalo · Seguinos para más</div>
{sig(False, 7, N1)}'''))

# ---------------- VIERNES 20 · PREGUNTAS FRECUENTES en chat ----------------
FAQ = [('¿Cuánto sale una web?', 'Depende de lo que necesites. Un rediseño arranca <b>desde $197.000</b>. Todos los planes están en triweb.com.ar.', 'Precio publicado en triweb.com.ar al 2/11/2026.'),
       ('¿Y cuánto tarda?', 'Una landing page está lista en <b>7 días hábiles</b>.', 'Una landing es una web de una sola página, pensada para que te escriban.'),
       ('Ya tengo Instagram. ¿Para qué quiero web?', 'Instagram te hace conocer. La web hace que te encuentren en Google y ordena precios y servicios para que te escriban.', ''),
       ('¿Por dónde arranco?', 'Contanos qué hacés y qué necesitás. Te asesoramos gratis y te decimos qué plan te conviene.', '')]
N2 = 6
def bubble_in(t, top):
    return f'<div style="position:absolute;left:96px;right:240px;top:{top}px;background:#FFFFFF;border-radius:44px 44px 44px 10px;padding:38px 44px;font-size:52px;font-weight:600;line-height:1.25;color:{NEGRO}">{t}</div>'
def bubble_out(t, top):
    return (f'<div style="position:absolute;left:200px;right:96px;top:{top}px;background:{NEGRO};color:{CREMA};border-radius:44px 44px 10px 44px;padding:38px 44px;font-size:46px;line-height:1.35">{t}</div>'
            f'<div style="position:absolute;right:96px;top:{top-90}px;display:flex;align-items:center;gap:12px;font-size:26px;font-weight:700;color:{GRIS}">TriWeb {mark_svg(NEGRO, 56)}</div>')
C2 = [('crema', f'''
<div class="k" style="position:absolute;left:96px;top:140px;color:{VERDE_TXT}">LO QUE MÁS NOS PREGUNTAN POR MENSAJE</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:250px;font-size:140px">¿Cuánto sale una <span class="hl">web</span>?</div>
<div style="position:absolute;left:96px;top:760px;background:#FFFFFF;border-radius:40px 40px 40px 10px;padding:30px 40px;font-size:42px;color:{NEGRO}">Hola! Una consulta…</div>
<div style="position:absolute;left:96px;top:900px;background:#FFFFFF;border-radius:40px 40px 40px 10px;padding:30px 40px;font-size:42px;color:{NEGRO}">¿y cuánto tarda?</div>
<div style="position:absolute;left:96px;top:1040px;display:flex;gap:12px;background:#FFFFFF;border-radius:40px;padding:30px 40px">{''.join(f'<div style="width:20px;height:20px;border-radius:10px;background:{GRIS}"></div>' for _ in range(3))}</div>
<div style="position:absolute;right:96px;top:1060px;font-size:34px;color:{GRIS}">4 respuestas · deslizá →</div>
{sig(False, 1, N2)}''')]
for i, (q, a, n) in enumerate(FAQ):
    C2.append(('crema', f'''
<div class="k" style="position:absolute;left:96px;top:120px;color:{VERDE_TXT}">PREGUNTA {i+1} DE 4</div>
{bubble_in(q, 230)}
{bubble_out(a, 640 if len(q) < 30 else 720)}
{f'<div style="position:absolute;left:200px;right:96px;top:1120px;font-size:30px;color:{GRIS};text-align:right">{n}</div>' if n else ''}
{sig(False, i+2, N2)}'''))
C2.append(('negro', f'''
<div class="d" style="position:absolute;left:96px;right:96px;top:200px;font-size:116px">¿Te quedó alguna pregunta?</div>
<div style="position:absolute;left:96px;right:96px;top:560px;font-size:46px;line-height:1.35;color:{GRIS_D}">Escribinos por mensaje o por WhatsApp. Planes y precios en triweb.com.ar (link en la bio).</div>
<div style="position:absolute;left:96px;right:96px;top:860px;height:130px;border-radius:65px;border:4px solid #3A3A3E;display:flex;align-items:center;justify-content:space-between;padding:0 14px 0 44px">
  <span style="font-size:40px;color:{GRIS_D}">Mensaje…</span>
  <span style="width:100px;height:100px;border-radius:50px;background:{VERDE};color:{NEGRO};display:flex;align-items:center;justify-content:center;font-size:52px;font-weight:800">↑</span></div>
<div style="position:absolute;left:96px;top:1040px"><span class="pill" style="background:{CREMA};color:{NEGRO};font-size:40px;padding:24px 44px"><b>Consultanos</b> · Trabajemos juntos</span></div>
<div style="position:absolute;left:96px;top:1170px;font-size:34px;color:{GRIS_D}">Guardalo · Seguinos para más</div>
{sig(True, 6, N2)}'''))

# ---------------- DOMINGO 22 · CHECKLIST DE TOMAS (edición de video) ----------------
def frame(w, h, n, txt, dark=False, fs=36):
    bd = '#3A3A3E' if dark else NEGRO
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border:5px solid {bd};border-radius:28px;padding:26px;display:flex;flex-direction:column;justify-content:flex-end;flex:none">'
            f'<div style="position:absolute;left:24px;top:22px;display:flex;align-items:center;gap:10px;font-size:22px;font-weight:700;color:{GRIS}"><span style="width:18px;height:18px;border-radius:9px;background:{VERDE}"></span>REC</div>'
            f'<div class="d" style="position:absolute;right:22px;top:12px;font-size:64px;color:{"#3A3A3E" if dark else "#D9D3C5"}">{n:02d}</div>'
            f'<div style="font-size:{fs}px;font-weight:700;line-height:1.2;color:{CREMA if dark else NEGRO}">{txt}</div></div>')
T = ['Tu producto girando sobre la mesa', 'Tus manos armando o preparando', 'El antes y el después', 'Un detalle bien de cerca',
     'Abrir la puerta del local', 'Armar un pedido', 'Tu producto en uso',
     'El precio, con texto en pantalla', 'La respuesta a una pregunta frecuente', 'El cierre del día']
N3 = 6
small = ''.join(f'<div style="width:150px;height:266px;border:4px solid #3A3A3E;border-radius:20px;position:relative"><span style="position:absolute;left:16px;top:16px;width:16px;height:16px;border-radius:8px;background:{VERDE if k == 0 else "#3A3A3E"}"></span></div>' for k in range(5))
C3 = [('negro', f'''
<div class="k" style="position:absolute;left:96px;top:140px;color:{VERDE}">LISTA DE TOMAS · GUARDALA</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:240px;font-size:122px">Finde largo: <span class="hl">10 videos</span> en 1 hora.</div>
<div style="position:absolute;left:96px;right:96px;top:700px;font-size:44px;line-height:1.35;color:{GRIS_D}">Tu celular, tu producto y esta lista. Contenido para todo el mes.</div>
<div style="position:absolute;left:96px;top:900px;display:flex;gap:22px">{small}</div>
{sig(True, 1, N3)}'''),
 ('crema', f'''
<div class="k" style="position:absolute;left:96px;top:120px;color:{VERDE_TXT}">TOMAS 1 A 4 · EL PRODUCTO</div>
<div style="position:absolute;left:96px;top:200px;display:grid;grid-template-columns:428px 428px;gap:32px">{''.join(frame(428, 470, k+1, T[k]) for k in range(4))}</div>
{sig(False, 2, N3)}'''),
 ('crema', f'''
<div class="k" style="position:absolute;left:96px;top:120px;color:{VERDE_TXT}">TOMAS 5 A 7 · EL DÍA A DÍA</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:190px;font-size:84px">Mostrá cómo trabajás.</div>
<div style="position:absolute;left:96px;top:420px;display:flex;gap:26px">{''.join(frame(278, 494, k+1, T[k], fs=34) for k in range(4, 7))}</div>
<div style="position:absolute;left:96px;right:96px;top:980px;font-size:40px;line-height:1.35;color:{GRIS}">Es lo que la gente más mira: el proceso real, sin producción.</div>
{sig(False, 3, N3)}'''),
 ('crema', f'''
<div class="k" style="position:absolute;left:96px;top:120px;color:{VERDE_TXT}">TOMAS 8 A 10 · LAS QUE VENDEN</div>
<div style="position:absolute;left:96px;right:96px;top:200px">{''.join(
    f'<div style="display:flex;gap:34px;align-items:center;padding:36px 0;border-bottom:3px solid #D9D3C5"><div class="d o" style="font-size:150px;width:260px;flex:none;color:{NEGRO}">{k+1:02d}</div><div style="font-size:52px;font-weight:700;line-height:1.2">{T[k]}</div></div>' for k in range(7, 10))}</div>
<div style="position:absolute;left:96px;right:96px;top:1010px;font-size:40px;line-height:1.35;color:{GRIS}">Grabalas sin hablar: el texto se suma en la edición.</div>
{sig(False, 4, N3)}'''),
 ('negro', f'''
<div class="k" style="position:absolute;left:96px;top:140px;color:{GRIS_D}">ANTES DE GRABAR</div>
<div style="position:absolute;left:96px;right:96px;top:230px">{''.join(
    f'<div style="display:flex;gap:30px;align-items:baseline;margin-bottom:58px"><span class="d" style="font-size:64px;color:{VERDE if k == 0 else CREMA}">→</span><div><div class="d" style="font-size:66px">{h}</div><div style="font-size:38px;color:{GRIS_D};margin-top:10px">{d}</div></div></div>'
    for k, (h, d) in enumerate([('Luz de ventana', 'De frente o de costado, nunca a contraluz.'), ('Celular vertical', 'Y limpiá el lente con la remera.'), ('5 a 8 segundos', 'Por toma. Después se corta.'), ('Grabá de más', 'Dos o tres versiones de cada una.')]))}</div>
{sig(True, 5, N3)}'''),
 ('crema', f'''
<div style="position:absolute;left:96px;top:150px">{mark_svg(NEGRO, 150)}</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:380px;font-size:112px">¿Grabaste y no sabés editar?</div>
<div style="position:absolute;left:96px;right:96px;top:690px;font-size:46px;line-height:1.35">Mandanos las tomas: las convertimos en reels con tu marca.</div>
<div style="position:absolute;left:96px;top:900px"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:42px;padding:26px 50px"><b style="color:{VERDE}">Consultanos</b> · Trabajemos juntos</span></div>
<div style="position:absolute;left:96px;top:1060px;font-size:36px;color:{GRIS};line-height:1.45">Guardalo para el finde · Seguinos para más</div>
{sig(False, 6, N3)}''')]

# ---------------- HISTORIAS (1080×1920; nada importante en los 340 px inferiores) ----------------
def story(inner, cls):
    return page(inner + f'<div style="position:absolute;left:96px;top:120px;display:flex;align-items:center;gap:14px">{mark_svg(CREMA if cls == "negro" else NEGRO, 60)}'
                f'<span style="font-size:30px;font-weight:600;color:{GRIS_D if cls == "negro" else GRIS}">@triweb_73</span></div>', 1080, 1920, cls, extra_css=X)
NOTE = lambda c, t='Nuevo post en el perfil ↑': f'<div style="position:absolute;left:96px;right:96px;top:1440px;font-size:38px;color:{c}">{t}</div>'
ST = {
 'lun-error': ('negro', f'''<div style="position:absolute;left:0;right:0;top:330px;height:520px;background:#1E1E21"></div>
   <div class="d" style="position:absolute;left:96px;top:460px;font-size:150px;color:{GRIS_D};text-decoration:line-through;text-decoration-color:{CREMA};text-decoration-thickness:14px">Bienvenidos</div>
   <div style="position:absolute;left:0;right:0;top:850px;height:520px;background:{CREMA}"></div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:940px;font-size:96px;color:{NEGRO}">Decí qué hacés en la primera línea.</div>{NOTE(GRIS_D, '3 errores de tu web, en el reel de hoy ↑')}'''),
 'mar-vs': ('crema', f'''<div class="d" style="position:absolute;left:96px;right:96px;top:400px;font-size:104px">Solo Instagram</div>
   <div class="d o" style="position:absolute;left:96px;top:560px;font-size:300px;color:{NEGRO}">VS</div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:900px;font-size:104px"><span class="hl">Instagram + web</span></div>
   <div style="position:absolute;left:96px;right:96px;top:1120px;font-size:44px;color:{GRIS}">4 rondas. Adiviná quién gana.</div>{NOTE(GRIS)}'''),
 'mie-notas': ('crema', f'''<div style="position:absolute;inset:0;background:#FBF8F1"></div>
   <div style="position:absolute;left:96px;right:96px;top:330px;font-size:40px;color:{VERDE_TXT};font-weight:600">‹ Notas</div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:440px;font-size:110px;color:{NEGRO}">Faltan 9 días para el Black Friday.</div>
   <div style="position:absolute;left:96px;right:96px;top:870px;font-size:56px;line-height:1.6;color:{NEGRO}">1. Te busca en Google.<br>2. Entra a tu web.<br>3. …</div>{NOTE(GRIS, 'Seguí la lista en el reel ↑')}'''),
 'jue-proceso': ('negro', f'''<div class="d o" style="position:absolute;left:80px;top:360px;font-size:330px;color:{CREMA}">01</div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:740px;font-size:110px">De un moodboard a una marca.</div>
   <div style="position:absolute;left:96px;right:96px;top:1080px;font-size:44px;color:{GRIS_D}">El proceso completo, detrás de escena.</div>{NOTE(GRIS_D)}'''),
 'vie-chat': ('crema', f'''<div style="position:absolute;left:96px;right:200px;top:420px;background:#FFFFFF;border-radius:44px 44px 44px 10px;padding:40px 46px;font-size:64px;font-weight:700">¿Cuánto sale una web?</div>
   <div style="position:absolute;left:300px;right:96px;top:700px;background:{NEGRO};color:{CREMA};border-radius:44px 44px 10px 44px;padding:40px 46px;font-size:48px;line-height:1.35">Te respondemos esta y 3 preguntas más en el post de hoy.</div>{NOTE(GRIS)}'''),
 'sab-grilla': ('negro', f'''<div style="position:absolute;left:96px;right:96px;top:380px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px">
   <div style="aspect-ratio:4/5;background:{VERDE};color:{NEGRO};font-size:30px;font-weight:800;padding:20px;display:flex;align-items:flex-end">@tucliente te etiquetó</div>{''.join(f'<div style="aspect-ratio:4/5;background:{c}"></div>' for c in ["#2A2A2E", "#3A3A3E", "#3A3A3E", "#2A2A2E", "#1E1E21"])}</div>
   <div class="d" style="position:absolute;left:96px;right:96px;top:1190px;font-size:96px">Novedad de Instagram.</div>{NOTE(GRIS_D, 'Te la contamos en el reel ↑')}'''),
 'dom-tomas': ('crema', f'''<div style="position:absolute;left:96px;top:330px;width:420px;height:746px;border:6px solid {NEGRO};border-radius:40px">
   <div style="position:absolute;left:30px;top:30px;display:flex;align-items:center;gap:12px;font-size:30px;font-weight:700;color:{GRIS}"><span style="width:24px;height:24px;border-radius:12px;background:{VERDE}"></span>REC</div></div>
   <div class="d" style="position:absolute;left:580px;right:96px;top:420px;font-size:92px">10 videos en 1 hora.</div>
   <div style="position:absolute;left:580px;right:96px;top:800px;font-size:40px;color:{GRIS};line-height:1.35">La lista de tomas para el finde largo.</div>{NOTE(GRIS)}'''),
 # para subir a mano con sticker (lugar libre al centro-abajo)
 'sticker-encuesta-tenes-web': ('negro', f'''<div class="d" style="position:absolute;left:96px;right:96px;top:420px;font-size:124px">¿Tu negocio tiene web?</div>
   <div style="position:absolute;left:96px;right:96px;top:780px;font-size:40px;color:{GRIS_D}">Votá ↓ (sí / no / en eso estoy)</div>
   <div style="position:absolute;left:140px;right:140px;top:960px;height:320px;border:4px dashed #3A3A3E;border-radius:40px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#4A4A4E">sticker de encuesta</div>'''),
 'sticker-pregunta-que-te-frena': ('crema', f'''<div class="d" style="position:absolute;left:96px;right:96px;top:420px;font-size:116px">¿Qué te frena para tener tu <span class="hl">web</span>?</div>
   <div style="position:absolute;left:96px;right:96px;top:900px;font-size:40px;color:{GRIS}">Respondemos en historias ↓</div>
   <div style="position:absolute;left:140px;right:140px;top:1040px;height:300px;border:4px dashed #CFC8B8;border-radius:40px;display:flex;align-items:center;justify-content:center;font-size:30px;color:#B5AE9E">sticker de pregunta</div>'''),
}

if __name__ == '__main__':
    pairs = []
    for name, slides in (('ig-vs-web', C1), ('faq-chat-web', C2), ('lista-tomas-finde', C3)):
        for i, (cls, inner) in enumerate(slides, 1):
            h = OUT / f'{name}-{i}.html'; h.write_text(page(inner, cls=cls, extra_css=X)); pairs.append((h, OUT / f'triweb-{name}-{i:02d}.png'))
    for name, (cls, inner) in ST.items():
        h = OUT / f'h-{name}.html'; h.write_text(story(inner, cls)); pairs.append((h, OUT / f'triweb-historia-{name}.png'))
    render(pairs); print('ok', len(pairs))
