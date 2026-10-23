import sys, pathlib
sys.path.insert(0, '/home/claude/triweb'); sys.path.insert(0, '/home/claude/triweb/semana1')
from kit import *
from carruseles import hook, tip, cta, service

OUT = pathlib.Path('/home/claude/triweb/semana2')

posts = {
 '5-community-manager': [
   hook('Lo que hace un <span class="hl">community manager</span> por tu negocio',
        'Y por qué tu Instagram no crece si lo hacés "cuando hay tiempo".', 1, 7, 108),
   tip('01', 'Planifica el mes.', 'Un calendario con qué se publica cada día y para qué: vender, mostrar trabajos o ganar confianza.', 2, 7),
   tip('02', 'Diseña cada pieza.', 'Posts, historias y reels con la misma estética, para que te reconozcan sin leer tu nombre.', 3, 7),
   tip('03', 'Escribe textos que venden.', 'Ganchos que frenan el scroll y un llamado claro a escribirte, en cada publicación.', 4, 7),
   tip('04', 'Responde rápido.', 'Mensajes y comentarios contestados en el día: un cliente que espera, se va con otro.', 5, 7),
   tip('05', 'Mide qué funciona.', 'Revisa los números cada mes y repite lo que trae consultas, no solo likes.', 6, 7),
   cta('¿Querés dejar de pensar en qué publicar?',
       'Manejamos el Instagram de tu negocio con un plan mensual. Consultanos y trabajemos juntos.', 7, 7),
 ],
 '6-logo-no-es-marca': [
   hook('Tu logo <span class="hl">no es</span> tu marca.',
        'Es solo una parte. Esto es lo que hace que un negocio se vea profesional.', 1, 6, 132),
   tip('01', 'Colores fijos.', 'Dos o tres colores que se repiten en todo: el local, las redes, los presupuestos.', 2, 6),
   tip('02', 'Tipografías claras.', 'Una para títulos y otra para textos. Siempre las mismas.', 3, 6),
   tip('03', 'Una forma de hablar.', 'Cercana, formal, divertida: lo importante es que suene igual en todos lados.', 4, 6),
   tip('04', 'Piezas que combinan.', 'Tarjetas, cartelería, posts y web hechas con las mismas reglas.', 5, 6),
   cta('¿Tu marca se ve igual en todos lados?',
       'Armamos tu identidad completa, no solo el logo. Consultanos y trabajemos juntos.', 6, 6),
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
        d = OUT / name; imgs = sorted(d.glob('triweb-*.png'))
        sheet = page('<div style="display:flex;flex-wrap:wrap;gap:12px;padding:12px">' + ''.join(f'<img src="{i.name}" style="width:300px">' for i in imgs) + '</div>', 1300, 860)
        (d / 'sheet.html').write_text(sheet); render([(d / 'sheet.html', OUT / f'sheet-{name}.png')])
        for h in d.glob('*.html'): h.unlink()
    print('ok', len(pairs))
