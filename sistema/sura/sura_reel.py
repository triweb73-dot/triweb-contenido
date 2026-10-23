"""Sura branding reel: 'De la idea a la marca' (15 s, 1080x1920) with cuts on the beat."""
import sys, pathlib
sys.path.insert(0, '/home/claude/triweb'); sys.path.insert(0, '/home/claude/triweb/semana1')
import motion
from kit import *

D = pathlib.Path('/home/claude/triweb/sura'); S = D / 'src'
img = lambda n: (S / f'{n}.png').as_uri()
M = 96

KB = """<script>
(function(){const base=render;render=function(t){base(t);
 document.querySelectorAll('[data-kb]').forEach(el=>{const [a,b]=el.dataset.kb.split(',').map(Number);
   const p=Math.min(1,Math.max(0,(t-a)/(b-a)));el.style.transform=`scale(${1.04+0.08*p})`;});};})();
</script>"""

def shot(name, a, b, fit='cover', pos='center', bg=NEGRO, label=None):
    lab = (f'<div style="position:absolute;left:{M}px;top:330px;background:{CREMA};color:{NEGRO};border-radius:999px;'
           f'padding:14px 28px;font-size:32px;font-weight:800">{label}</div>') if label else ''
    return (f'<div data-scene="{a},{b}" style="position:absolute;left:0;top:440px;width:1080px;height:1080px;overflow:hidden;background:{bg};opacity:0">'
            f'<img data-kb="{a},{b}" src="{img(name)}" style="width:100%;height:100%;object-fit:{fit};object-position:{pos};display:block"></div>'
            + (f'<div data-scene="{a},{b}" style="opacity:0">{lab}</div>' if label else ''))

cuts = [('cartel-obra', 'center 60%'), ('casco', 'center 55%'), ('tarjetas', 'center 40%'), ('carta', 'center'),
        ('carpeta', 'center'), ('local', 'center 55%'), ('tubo', 'center')]
seq = ''.join(shot(n, 7.5 + i*0.5, 8.0 + i*0.5, pos=p) for i, (n, p) in enumerate(cuts))
sw = ''.join(f'<div data-grow="{6.0 + k*0.25}" style="position:absolute;left:{M}px;top:{560 + k*190}px;width:{1080-2*M}px;height:160px;border-radius:24px;background:{c}"></div>'
             f'<div data-in="{6.15 + k*0.25}" style="position:absolute;left:{M+36}px;top:{618 + k*190}px;font-size:40px;font-weight:800;color:{CREMA}">{nm}</div>'
             for k, (c, nm) in enumerate([('#313c14', 'Verde oliva'), ('#323232', 'Grafito'), ('#a27850', 'Bronce'), ('#959a86', 'Salvia')]))

html = motion.scene(f'''
<div class="c" data-in=".15" data-out="1.9" style="top:250px;font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:{VERDE}">Caso · Sura Arquitectura</div>
<div class="c d" data-in=".3" data-out="1.9" style="top:310px;font-size:118px">De la idea<br>a la <span class="hl">marca</span>.</div>
<div class="c" data-in=".8" data-out="1.9" style="top:640px;font-size:42px;line-height:1.35;color:{GRIS_D}">Branding para un estudio de arquitectura.</div>
<div data-scene="2.0,6.0" style="position:absolute;left:{M}px;top:250px;font-size:30px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:{VERDE};opacity:0">Proyecto de branding</div>
{shot('moodboard', 2.0, 4.0, 'contain', 'center', '#1d2410', 'Moodboard')}
{shot('logo-negro', 4.0, 6.0, 'cover', 'center 45%', NEGRO, 'El símbolo')}
<div data-scene="6.0,7.5" style="position:absolute;inset:0;opacity:0">
  <div style="position:absolute;left:{M}px;top:330px;background:{CREMA};color:{NEGRO};border-radius:999px;padding:14px 28px;font-size:32px;font-weight:800">La paleta</div>{sw}</div>
<div data-scene="7.5,11.0" style="position:absolute;left:{M}px;top:330px;background:{CREMA};color:{NEGRO};border-radius:999px;padding:14px 28px;font-size:32px;font-weight:800;opacity:0">Las aplicaciones</div>
{seq}
{motion.ending(11.0, '¿Tu marca puede<br>ser la próxima?')}''') .replace('</body>', KB + '</body>')

if __name__ == '__main__':
    motion.OUT = D
    motion.make('sura-reel', html, 15, 4.6)
