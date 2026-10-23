import sys, pathlib; sys.path.insert(0, '/home/claude/triweb')
from kit import *

OUT = pathlib.Path('/home/claude/triweb/semana1/historias'); OUT.mkdir(exist_ok=True)
for o in OUT.glob('*'): o.unlink()
M = 96; TOP = 280   # stay clear of Instagram's top bar and bottom reply bar

def foot(dark=True):
    col = GRIS_D if dark else GRIS
    return (f'<div style="position:absolute;left:{M}px;bottom:360px;width:52px;height:52px">{mark_svg(CREMA if dark else NEGRO, 52)}</div>'
            f'<div class="handle" style="left:{M+68}px;bottom:372px;color:{col}">@triweb_73</div>')

def story(inner, cls='negro', dark=True):
    return page(inner + foot(dark), 1080, 1920, cls)

def kicker(txt, dark=True):
    return f'<div style="font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:{VERDE if dark else VERDE_TXT}">{txt}</div>'

stories = {
 '1-lun-nueva-identidad': story(f'''
  <div style="position:absolute;left:{M}px;right:{M}px;top:{TOP}px">{kicker('Nueva etapa')}
   <div class="d" style="font-size:118px;margin-top:36px">TriWeb<br>se renovó.</div>
   <div style="font-size:42px;line-height:1.35;color:{GRIS_D};margin-top:40px;max-width:820px">Tres personas, una línea que nos conecta. Y un triángulo verde en el centro: el <b style="color:{CREMA}">Tri</b> de TriWeb.</div></div>
  <div style="position:absolute;left:50%;top:1000px;transform:translateX(-50%);width:520px;height:520px">{mark_svg(CREMA, 520)}</div>'''),
 '2-lun-encuesta': story(f'''
  <div style="position:absolute;left:{M}px;right:{M}px;top:{TOP}px">{kicker('Pregunta rápida')}
   <div class="d" style="font-size:120px;margin-top:36px">¿Tenés un <span class="hl">negocio</span>?</div>
   <div style="font-size:42px;line-height:1.35;color:{GRIS_D};margin-top:40px">Contanos y te mostramos ideas pensadas para tu rubro.</div></div>'''),
 '3-mar-tu-web': story(f'''
  <div style="position:absolute;left:{M}px;right:{M}px;top:{TOP}px">{kicker('Pregunta del día', False)}
   <div class="d" style="font-size:120px;margin-top:36px">¿Tu negocio tiene web?</div>
   <div style="font-size:42px;line-height:1.35;color:{GRIS};margin-top:40px">Sí, no, o "tengo una pero me da vergüenza mostrarla". Todas valen.</div></div>''', 'crema', False),
 '4-mie-reel': story(f'''
  <div style="position:absolute;left:{M}px;right:{M}px;top:{TOP}px">{kicker('Nuevo reel')}
   <div class="d" style="font-size:120px;margin-top:36px">La prueba de los <span class="hl">5 segundos</span>.</div>
   <div style="font-size:42px;line-height:1.35;color:{GRIS_D};margin-top:40px">Hacela con tu web ahora mismo. Te explicamos cómo en el último reel.</div></div>
  <div style="position:absolute;left:{M}px;right:{M}px;top:1120px;height:300px;border-radius:28px;background:{RAISED_D};display:flex;align-items:center;justify-content:center"><div class="d vd" style="font-size:200px">5</div></div>'''),
 '5-jue-proceso': story(f'''
  <div style="position:absolute;left:{M}px;right:{M}px;top:{TOP}px">{kicker('Cómo trabajamos', False)}
   <div class="d" style="font-size:104px;margin-top:36px">De la primera charla a tu web lista.</div>
   <div style="margin-top:64px;display:flex;flex-direction:column;gap:22px">''' + ''.join(
     f'<div style="display:flex;align-items:center;gap:30px;background:#fff;border-radius:26px;padding:28px 34px"><span class="d" style="font-size:56px;width:84px;height:84px;border-radius:20px;display:flex;align-items:center;justify-content:center;background:{VERDE if i==4 else NEGRO};color:{NEGRO if i==4 else CREMA}">{i}</span><span style="font-size:42px;font-weight:600">{t}</span></div>'
     for i, t in enumerate(['Primera charla sin costo', 'Propuesta con precio cerrado', 'Diseño y desarrollo', 'Entrega y capacitación'], 1)) + '</div></div>', 'crema', False),
 '6-vie-preguntas': story(f'''
  <div style="position:absolute;left:{M}px;right:{M}px;top:{TOP}px">{kicker('Preguntanos')}
   <div class="d" style="font-size:118px;margin-top:36px">¿Qué querés saber de tu web o tu marca?</div>
   <div style="font-size:42px;line-height:1.35;color:{GRIS_D};margin-top:40px">Respondemos todas el lunes.</div></div>'''),
 '7-sab-diagnostico': story(f'''
  <div style="position:absolute;inset:0;background:{VERDE}"></div>
  <div style="position:absolute;left:{M}px;right:{M}px;top:{TOP}px;color:{NEGRO}">
   <div style="font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase">Tu negocio, al siguiente paso</div>
   <div class="d" style="font-size:132px;margin-top:36px">Trabajemos juntos.</div>
   <div style="font-size:44px;line-height:1.35;margin-top:44px;max-width:820px">Web, diseño, video y redes para que tu negocio consiga más clientes.</div>
   <div style="margin-top:70px"><span class="pill" style="background:{NEGRO};color:{CREMA};font-size:42px;padding:26px 50px"><b style="color:{VERDE}">Consultanos</b> por mensaje</span></div></div>
  <div style="position:absolute;left:{M}px;bottom:360px;width:52px;height:52px">{mark_svg(NEGRO, 52, seed=CREMA)}</div>
  <div class="handle" style="left:{M+68}px;bottom:372px;color:{NEGRO}">@triweb_73</div>''', 'verdebg'),
}
# the last story draws its own footer on green
stories['7-sab-diagnostico'] = stories['7-sab-diagnostico'].replace(foot(True), '')

pairs = []
for k, html in stories.items():
    h = OUT / f'{k}.html'; h.write_text(html); pairs.append((h, OUT / f'triweb-historia-{k}.png'))
render(pairs)
imgs = sorted(OUT.glob('triweb-*.png'))
sheet = page('<div style="display:flex;gap:10px;padding:10px">' + ''.join(f'<img src="{i.name}" style="width:200px">' for i in imgs) + '</div>', 1500, 380)
(OUT / 'sheet.html').write_text(sheet); render([(OUT / 'sheet.html', OUT.parent / 'sheet-historias.png')])
for h in OUT.glob('*.html'): h.unlink()
print('ok', len(imgs))
