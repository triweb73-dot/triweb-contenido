import sys, pathlib; sys.path.insert(0, '/home/claude/triweb')
from kit import *

OUT = pathlib.Path('/home/claude/triweb/semana1')
M = 96  # outer margin at 1080
GHOST = '#1D1D20'  # the Nudo as a large background motif on negro

def chrome(n, total, dark):
    col = GRIS_D if dark else GRIS
    return (f'<div style="position:absolute;left:{M}px;bottom:{M-16}px;width:56px;height:56px">{mark_svg(CREMA if dark else NEGRO, 56)}</div>'
            f'<div class="handle" style="left:{M+72}px;bottom:{M-2}px;color:{col}">@triweb_73</div>'
            f'<div class="num" style="right:{M}px;bottom:{M-2}px;color:{col}">{n}/{total}</div>')

def swipe():
    return f'<div style="position:absolute;right:{M}px;top:{M}px;font-size:28px;font-weight:700;color:{CREMA};opacity:.6">deslizá →</div>'

def ghost():
    return f'<div style="position:absolute;right:-340px;bottom:-300px;width:1000px;height:1000px">{mark_svg(GHOST, 1000, seed="#12301E")}</div>'

def hook(title_html, sub, n, total, size=128):
    return page(f'''{ghost()}{swipe()}
<div style="position:absolute;left:{M}px;right:{M}px;top:250px">
 <div class="d" style="font-size:{size}px">{title_html}</div>
 <div style="margin-top:52px;font-size:40px;line-height:1.3;color:{GRIS_D};max-width:760px">{sub}</div>
</div>{chrome(n,total,True)}''', cls='negro')

def body_block(top_html, title, body, title_size=110):
    return f'''<div style="position:absolute;left:{M}px;right:{M}px;top:{M}px;bottom:{M+80}px;display:flex;flex-direction:column;justify-content:center">
 <div>{top_html}</div>
 <div class="d" style="font-size:{title_size}px;margin-top:60px">{title}</div>
 <div style="margin-top:48px;font-size:46px;line-height:1.36;color:{GRIS};max-width:860px">{body}</div></div>'''

def service(tag, title, body, n, total):
    tag_html = f'<span class="pill" style="background:{NEGRO};color:{CREMA};font-size:32px">{tag}</span>'
    return page(body_block(tag_html, title, body) + chrome(n, total, False), cls='crema')

def tip(num, title, body, n, total):
    num_html = (f'<span class="d" style="display:inline-block;font-size:140px;line-height:1;background:{VERDE};color:{NEGRO};'
                f'border-radius:28px;padding:22px 32px 18px;letter-spacing:-.04em">{num}</span>')
    return page(body_block(num_html, title, body, 100) + chrome(n, total, False), cls='crema')

def cta(title, body, n, total):
    return page(f'''{ghost()}
<div style="position:absolute;left:{M}px;right:{M}px;top:{M}px;bottom:{M+80}px;display:flex;flex-direction:column;justify-content:center">
 <div style="width:132px;height:132px">{mark_svg(CREMA, 132)}</div>
 <div class="d" style="font-size:112px;margin-top:60px">{title}</div>
 <div style="margin-top:48px;font-size:42px;line-height:1.35;max-width:820px;color:{GRIS_D}">{body}</div>
 <div style="margin-top:68px"><span class="pill" style="background:{VERDE};color:{NEGRO};font-size:38px;padding:24px 46px"><b>Consultanos</b> · Trabajemos juntos</span></div>
</div>
<div class="handle" style="left:{M}px;bottom:{M-2}px;color:{GRIS_D}">@triweb_73</div>
<div class="num" style="right:{M}px;bottom:{M-2}px;color:{GRIS_D}">{n}/{total}</div>''', cls='negro')

posts = {
 '1-relanzamiento': [
   hook('Volvimos.<br>Y ahora hacemos <span class="hl">todo</span>.',
        'Web, diseño, branding y video para tu negocio. Con un solo equipo.', 1, 5, 132),
   service('Desarrollo web', 'Una web que trabaja por vos.',
           'Rápida, que se ve bien en el celular y que podés actualizar sin depender de nadie.', 2, 5),
   service('Diseño y branding', 'Una marca que se ve profesional.',
           'Logo, colores, tipografías y piezas listas para tu local, tus redes y tus presupuestos.', 3, 5),
   service('Edición de video', 'Videos que se miran hasta el final.',
           'Reels y videos editados para que tus redes muestren lo que hacés y lo bien que lo hacés.', 4, 5),
   cta('¿Tu negocio necesita una mano?',
       'Contanos qué necesitás y armamos juntos la mejor solución para tu negocio.', 5, 5),
 ],
 '3-cinco-senales': [
   hook('5 señales de que tu web te está <span class="hl">haciendo perder</span> clientes',
        'Si tu web tiene una sola, ya vale la pena revisarla.', 1, 7, 112),
   tip('01', 'Tarda en cargar.', 'Si tenés que esperar más de 3 segundos, muchas visitas se van antes de ver qué vendés. Probala desde tu celular con datos.', 2, 7),
   tip('02', 'Se ve mal en el celular.', 'Textos chiquitos, botones que no se pueden tocar, cosas cortadas. Y la mayoría de tus clientes te busca desde el teléfono.', 3, 7),
   tip('03', 'No dice qué hacés en 5 segundos.', 'Si alguien entra y no entiende enseguida qué ofrecés y dónde estás, se va a buscar otra opción.', 4, 7),
   tip('04', 'Contactarte es difícil.', 'Sin un botón de WhatsApp visible, el cliente que ya estaba decidido termina escribiéndole a otro.', 5, 7),
   tip('05', 'Está desactualizada.', 'Precios viejos, horarios que cambiaron, un "© 2019" al pie. Da la sensación de que el negocio no está atendiendo.', 6, 7),
   cta('¿Tu web tiene alguna?',
       'Consultanos y la dejamos lista para que te traiga clientes.', 7, 7),
 ],
}

if __name__ == '__main__':
    pairs = []
    for name, slides in posts.items():
        d = OUT / name; d.mkdir(parents=True, exist_ok=True)
        for old in d.glob('*'): old.unlink()
        for i, html in enumerate(slides, 1):
            h = d / f'{i:02d}.html'; h.write_text(html); pairs.append((h, d / f'triweb-{name}-{i:02d}.png'))
    render(pairs)
    for name in posts:
        d = OUT / name
        imgs = sorted(d.glob('triweb-*.png'))
        sheet = page('<div style="display:flex;flex-wrap:wrap;gap:12px;padding:12px">' + ''.join(f'<img src="{i.name}" style="width:300px">' for i in imgs) + '</div>', 1300, 860)
        (d / 'sheet.html').write_text(sheet); render([(d / 'sheet.html', OUT / f'sheet-{name}.png')])
        for h in d.glob('*.html'): h.unlink()
    print('ok', len(pairs))
