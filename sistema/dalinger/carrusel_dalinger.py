"""Carrusel caso real Dalinger Automotores (community manager), con capturas reales del perfil."""
import sys, pathlib
sys.path.insert(0, '/home/claude/triweb')
from kit import *
D = 'file:///home/claude/triweb/dalinger/'
OUT = pathlib.Path('/home/claude/triweb/dalinger/out'); OUT.mkdir(exist_ok=True)
N = 7
def foot(i, dark=True):
    c = GRIS_D if dark else GRIS
    return (f'<div style="position:absolute;left:96px;bottom:70px;display:flex;align-items:center;gap:12px">{mark_svg(CREMA if dark else NEGRO, 44)}'
            f'<span style="font-size:26px;font-weight:600;color:{c}">@triweb_73</span></div>'
            f'<div class="num" style="right:96px;bottom:78px;color:{c}">{i}/{N}</div>')
def kick(t, col=VERDE): return f'<div style="font-size:28px;font-weight:700;letter-spacing:.1em;color:{col}">{t}</div>'
def shot(src, w, extra=''):
    return f'<img src="{D}{src}" style="width:{w}px;border-radius:28px;display:block;box-shadow:0 30px 60px rgba(0,0,0,.35);{extra}">'
S = []
# 1 portada
S.append(('negro', f'''<div style="position:absolute;left:96px;right:96px;top:110px">{kick('CASO REAL · COMMUNITY MANAGER')}
<div class="d" style="font-size:92px;margin-top:26px">Así se ve un Instagram que <span class="hl">vende autos</span>.</div></div>
<div style="position:absolute;left:170px;top:520px;display:flex;flex-direction:column;gap:14px">{shot('fila-a.png', 740)}{shot('fila-b.png', 740)}</div>
{foot(1)}'''))
# 2 números
S.append(('crema', f'''<div style="position:absolute;left:96px;right:96px;top:130px">{kick('DALINGER AUTOMOTORES', VERDE_TXT)}
<div class="d" style="font-size:210px;margin-top:20px">+1.500</div>
<div class="d" style="font-size:64px;margin-top:6px">seguidores en el primer año.</div>
<div style="display:flex;gap:28px;margin-top:70px">
 <div style="flex:1;background:{NEGRO};color:{CREMA};border-radius:28px;padding:36px"><div class="d" style="font-size:84px">4.461</div><div style="font-size:30px;color:{GRIS_D};margin-top:10px">seguidores hoy</div></div>
 <div style="flex:1;background:{NEGRO};color:{CREMA};border-radius:28px;padding:36px"><div class="d" style="font-size:84px">275 mil</div><div style="font-size:30px;color:{GRIS_D};margin-top:10px">visualizaciones en los últimos 30 días</div></div>
</div></div>{foot(2, False)}'''))
# 3 plantilla por auto
S.append(('negro', f'''<div style="position:absolute;left:96px;right:96px;top:110px">{kick('QUÉ HICIMOS · 1')}
<div class="d" style="font-size:80px;margin-top:22px">Una plantilla fija para <span class="hl">cada auto</span>.</div>
<div style="font-size:36px;color:{GRIS_D};margin-top:24px;line-height:1.35">Modelo, año, kilómetros y transmisión siempre en el mismo lugar. El cliente ve lo que busca en un segundo.</div></div>
<div style="position:absolute;left:128px;top:630px;display:flex;gap:24px">{shot('post-corolla.png', 400)}{shot('post-hilux.png', 400)}</div>
{foot(3)}'''))
# 4 feed ordenado
S.append(('crema', f'''<div style="position:absolute;left:96px;right:96px;top:110px">{kick('QUÉ HICIMOS · 2', VERDE_TXT)}
<div class="d" style="font-size:80px;margin-top:22px">Un feed que funciona como <span class="hl">catálogo</span>.</div>
<div style="font-size:36px;color:{GRIS};margin-top:24px;line-height:1.35">Cada unidad publicada con la misma estética: la marca se reconoce sin leer el nombre.</div></div>
<div style="position:absolute;left:96px;right:96px;top:690px">{shot('fila-b.png', 888)}</div>
{foot(4, False)}'''))
# 5 perfil
S.append(('negro', f'''<div style="position:absolute;left:96px;right:96px;top:110px">{kick('QUÉ HICIMOS · 3')}
<div class="d" style="font-size:80px;margin-top:22px">Un perfil que responde <span class="hl">antes</span> de que pregunten.</div>
<div style="font-size:36px;color:{GRIS_D};margin-top:24px;line-height:1.35">Dirección, teléfono, horarios, web y destacados de clientes y financiación.</div></div>
<div style="position:absolute;left:130px;top:640px">{shot('perfil-header.png', 820)}</div>
{foot(5)}'''))
# 6 aprendizaje
S.append(('crema', f'''<div style="position:absolute;left:96px;right:96px;top:150px">{kick('LO QUE TE LLEVÁS', VERDE_TXT)}
<div class="d" style="font-size:84px;margin-top:22px;margin-bottom:50px">3 cosas que podés copiar hoy:</div>
''' + ''.join(f'<div style="display:flex;gap:30px;align-items:flex-start;margin-bottom:44px"><div class="d" style="font-size:76px;color:{VERDE_TXT};width:80px">{n}</div><div style="font-size:44px;line-height:1.3;font-weight:500">{t}</div></div>'
 for n, t in [('1', 'Usá la misma plantilla para cada producto.'), ('2', 'Poné los datos clave en la imagen, no solo en el texto.'), ('3', 'Completá la bio: dirección, horario y un link.')]) + f'''</div>{foot(6, False)}'''))
# 7 CTA
S.append(('negro', f'''<div style="position:absolute;left:0;right:0;top:250px;display:flex;justify-content:center">{mark_svg(CREMA, 230)}</div>
<div class="d" style="position:absolute;left:96px;right:96px;top:560px;font-size:96px;text-align:center">¿Querés esto para tu negocio?</div>
<div style="position:absolute;left:96px;right:96px;top:840px;font-size:38px;color:{GRIS_D};text-align:center;line-height:1.35">Manejamos el Instagram de tu negocio con un plan mensual.</div>
<div style="position:absolute;left:0;right:0;top:1010px;text-align:center"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:40px;padding:24px 48px"><b>Consultanos</b> · Trabajemos juntos</span></div>
<div style="position:absolute;left:0;right:0;bottom:80px;text-align:center;font-size:28px;color:{GRIS_D}">Guardalo y seguinos para más</div>'''))
pairs = []
for i, (cls, inner) in enumerate(S, 1):
    h = OUT / f'{i}.html'; h.write_text(page(inner, cls=cls)); pairs.append((h, OUT / f'triweb-caso-dalinger-{i:02d}.png'))
render(pairs); print('ok')
