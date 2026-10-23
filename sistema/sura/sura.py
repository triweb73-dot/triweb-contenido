"""Sura Arquitectura branding case study: carousel slides for TriWeb's Instagram."""
import sys, pathlib
sys.path.insert(0, '/home/claude/triweb'); sys.path.insert(0, '/home/claude/triweb/semana1')
from kit import *
from carruseles import chrome, ghost, cta, M

D = pathlib.Path('/home/claude/triweb/sura'); S = D / 'src'; OUT = D / 'carrusel'; OUT.mkdir(exist_ok=True)
img = lambda n: (S / f'{n}.png').as_uri()
TOTAL = 8
TAG = lambda dark: (f'<div style="position:absolute;right:{M}px;top:{M}px;font-size:24px;font-weight:700;letter-spacing:.08em;'
                    f'text-transform:uppercase;color:{GRIS_D if dark else GRIS}">Proyecto de branding</div>')

def pic(n, h, fit='cover', pos='center', bg=NEGRO):
    return (f'<div style="height:{h}px;border-radius:24px;overflow:hidden;background:{bg}">'
            f'<img src="{img(n)}" style="width:100%;height:100%;object-fit:{fit};object-position:{pos};display:block"></div>')

def step(num, title, body, media, n):
    return page(f'''{TAG(False)}
<div style="position:absolute;left:{M}px;right:{M}px;top:{M+64}px;bottom:{M+80}px;display:flex;flex-direction:column;gap:28px">
 <div style="display:flex;align-items:center;gap:22px">
   <span class="d" style="font-size:56px;line-height:1;background:{VERDE};color:{NEGRO};border-radius:16px;padding:12px 18px 10px">{num}</span>
   <span class="d" style="font-size:66px">{title}</span></div>
 <div style="font-size:38px;line-height:1.35;color:{GRIS};max-width:880px">{body}</div>
 <div style="flex:1;min-height:0;display:flex;flex-direction:column;gap:18px">{media}</div>
</div>{chrome(n, TOTAL, False)}''', cls='crema')

def row(*cells, h=None):
    return f'<div style="display:flex;gap:18px;flex:1;min-height:0">' + ''.join(f'<div style="flex:1;min-width:0;display:flex;flex-direction:column">{c}</div>' for c in cells) + '</div>'

def fill(n, pos='center', fit='cover', bg='transparent'):
    return (f'<div style="flex:1;min-height:0;border-radius:24px;overflow:hidden;background:{bg}"><img src="{img(n)}" '
            f'style="width:100%;height:100%;object-fit:{fit};object-position:{pos};display:block"></div>')
def col(*cells):
    return '<div style="display:flex;flex-direction:column;gap:18px;flex:1;min-height:0">' + ''.join(cells) + '</div>'

swatches = ''.join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:14px"><div style="flex:1;border-radius:24px;background:{c}"></div>'
    f'<div style="font-size:30px;font-weight:700">{name}</div><div style="font-size:24px;color:{GRIS};font-variant-numeric:tabular-nums">{c.upper()}</div></div>'
    for c, name in [('#313c14', 'Verde oliva'), ('#323232', 'Grafito'), ('#a27850', 'Bronce'), ('#959a86', 'Salvia')])

slides = [
 page(f'''{ghost()}{TAG(True)}
<div style="position:absolute;left:{M}px;right:{M}px;top:{M+70}px">
 <div style="font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:{VERDE}">Caso · Sura Arquitectura</div>
 <div class="d" style="font-size:104px;margin-top:28px">Así nació la marca de un <span class="hl">estudio de arquitectura</span>.</div></div>
<div style="position:absolute;left:{M}px;right:{M}px;top:700px;height:470px;border-radius:28px;overflow:hidden">
 <img src="{img('logo-negro')}" style="width:100%;height:100%;object-fit:cover;object-position:center 45%"></div>
{chrome(1, TOTAL, True)}''', cls='negro'),
 step('01', 'El punto de partida', 'Un estudio que diseña, planifica y construye. Tenía que verse moderno, orgánico, profesional y meticuloso.',
      fill('moodboard', 'center', 'contain', '#1d2410'), 2),
 step('02', 'El símbolo', 'Un ave posada sobre una viga reticulada: la naturaleza que habita la estructura, en un solo trazo.',
      fill('logo-verde', 'center 42%'), 3),
 step('03', 'La paleta', 'Colores de la tierra y de la obra: verde oliva, grafito, bronce y salvia.',
      f'<div style="display:flex;gap:18px;flex:1">{swatches}</div>', 4),
 step('04', 'En la obra', 'Tiene que verse igual de bien en un cartel de obra, un casco o un tubo de planos.',
      col(fill('cartel-obra', 'center 62%'), row(fill('casco', 'center 55%'), fill('tubo', 'center'))), 5),
 step('05', 'En el día a día', 'Tarjetas, carta, carpetas y papelería con el mismo sistema.',
      row(fill('tarjetas', 'center 40%')) + row(fill('carta'), fill('carpeta')), 6),
 step('06', 'En la calle y en redes', 'Del vinilo del local al perfil de Instagram: una marca que se reconoce en todos lados.',
      row(fill('local', 'center 60%'), fill('celular', 'center 30%', 'contain', '#d9d5cc')), 7),
 cta('¿Tu marca necesita algo así?', 'Diseñamos identidades completas: símbolo, colores, tipografía y todas las piezas. Consultanos y trabajemos juntos.', 8, TOTAL),
]

if __name__ == '__main__':
    pairs = []
    for o in OUT.glob('*'): o.unlink()
    for i, h in enumerate(slides, 1):
        p = OUT / f'{i:02d}.html'; p.write_text(h); pairs.append((p, OUT / f'triweb-sura-branding-{i:02d}.png'))
    render(pairs)
    imgs = sorted(OUT.glob('triweb-*.png'))
    sheet = page('<div style="display:flex;flex-wrap:wrap;gap:12px;padding:12px">' + ''.join(f'<img src="{i.name}" style="width:300px">' for i in imgs) + '</div>', 1300, 860)
    (OUT / 'sheet.html').write_text(sheet); render([(OUT / 'sheet.html', D / 'sheet-carrusel.png')])
    for h in OUT.glob('*.html'): h.unlink()
    print('ok', len(imgs))
