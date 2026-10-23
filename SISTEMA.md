# Sistema semanal de contenido de TriWeb

Este repositorio aloja las imágenes y videos que Metricool publica en el Instagram de TriWeb (@triweb_73) y las herramientas para producirlos. Cada semana se produce, se sube y se programa el contenido de la semana siguiente sin intervención del dueño.

## Datos fijos

- Marca en Metricool: `blogId = 7612908`, zona horaria `America/Argentina/Buenos_Aires`, red `instagram`.
- Horario de publicación: 10:00 (el de mayor actividad de la audiencia). Historias: 13:00 y 19:00.
- URL pública de cada archivo: `https://raw.githubusercontent.com/triweb73-dot/triweb-contenido/main/media/<AAAA-MM-DD del lunes>/<archivo>`.
- Reglas de marca, colores, tipografía y voz: `sistema/MARCA.md`. Negro `#0B0B0C`, crema `#F2ECDD`, único acento verde `#22C55E`. Logo: el Nudo con semilla verde.
- Llamado a la acción, siempre: **"Consultanos · Trabajemos juntos"** / "Consultanos por mensaje y trabajemos juntos". Nunca usar "DIAGNÓSTICO".
- Público: dueños de pymes y comercios de Latinoamérica, sobre todo Argentina. Español con voseo rioplatense, frases cortas, sin tecnicismos, máximo un emoji por pieza.

## Servicios (rotarlos todas las semanas)

Desarrollo web · Diseño gráfico · Branding · Edición de video · Community manager.

## Lo que se publica cada semana (lunes a sábado)

| Día | Formato |
| --- | --- |
| Lunes | Carrusel educativo para guardar (6-7 láminas) |
| Martes | Reel con gancho fuerte (tip o error común) |
| Miércoles | Reel de prueba (`TRIAL_REEL`, solo no seguidores) |
| Jueves | Motion graphic de un servicio |
| Viernes | Carrusel (checklist, mitos o proceso) |
| Sábado | Reel corto con llamado a la acción |
| Lunes a viernes | 1 historia por día (sin stickers; las de encuesta se entregan aparte para subir a mano) |

## Crecimiento de seguidores (prioridad)

El objetivo no es solo publicar: es llegar a gente que todavía no sigue a TriWeb y convertirla en seguidores y consultas.

- **Más reels que carruseles.** Los reels son lo que Instagram muestra a no seguidores. Mínimo 4 reels por semana y 2 carruseles.
- **1 reel de prueba (`TRIAL_REEL`) por semana.** Instagram lo muestra solo a no seguidores; es la forma más barata de probar ganchos nuevos. Si rinde bien, ese tema se repite como reel normal la semana siguiente.
- **Gancho en los primeros 2 segundos.** Texto grande con una pregunta o un error que duela ("Tu web te está espantando clientes"), nunca arrancar con el logo.
- **Contenido que se guarda y se comparte.** Checklists, "guardá esto para cuando...", "mandáselo a alguien que tenga un negocio". Pedirlo en el texto y en la última lámina.
- **Cerrar con "Seguinos para más"** además del "Consultanos" en carruseles educativos.
- **Palabras clave en el texto** (Instagram las usa como buscador): "diseño web", "página web para negocios", "branding", "community manager", "Buenos Aires", "Argentina". Entre 5 y 8 hashtags específicos, nada de #love o #instagood.
- **Colaboraciones.** Cuando un cliente real acepte, publicar con `instagramData.collaborators` para que el post salga también en su cuenta y llegue a sus seguidores.
- **Un sorteo al mes** (por ejemplo, un logo o una auditoría de redes gratis), con reglas claras: seguir a @triweb_73, comentar etiquetando a alguien con negocio, fecha de cierre y ganador anunciado en historias. Proponerlo en el resumen para que el dueño lo apruebe antes de publicarlo.
- **Historias todos los días** con preguntas y encuestas: aumentan la interacción y hacen que Instagram muestre más los posts.

## Procedimiento semanal

1. **Preparar el entorno.** `cp -r sistema/* /home/claude/triweb/` (las herramientas usan esa ruta). Inter e Inter Display ya están instaladas. Playwright y ffmpeg también.
2. **Medir.** Con Metricool (`getAnalyticsDataByMetrics`) revisar alcance, guardados, compartidos y mensajes de los posts de las últimas 2 semanas. Anotar en `historial.md` qué temas y formatos rindieron más y repetir esos formatos con temas nuevos.
2b. **Investigar tendencias (antes de planificar).** Con búsqueda web, revisar lo que está pasando esa semana y adaptarlo a TriWeb:
   - Formatos de reels en tendencia en Instagram (Argentina y Latinoamérica): estructuras de gancho, memes o plantillas que se puedan recrear con diseño y texto, sin caras.
   - Fechas comerciales y efemérides de la semana siguiente en Argentina (CyberMonday, Black Friday, Hot Sale, Día del Padre/Madre, Navidad, fin de año, vuelta a clases, días del diseñador, del programador, etc.) y cómo afectan a las pymes ("preparate para el CyberMonday con tu web").
   - Novedades de Instagram, Google o herramientas web que les importen a dueños de negocios (cambios de algoritmo, funciones nuevas, IA para pymes), contadas en simple.
   - Temas que la competencia (agencias y diseñadores de Argentina) esté publicando con buen rendimiento, para hacerlo mejor y con la identidad de TriWeb, nunca copiado.
   - Audio: los reels llevan la música original de `musica.py`. Si un audio en tendencia encaja, se puede intentar con `instagramData.audioConfiguration` (solo funciona si la cuenta es Business vinculada a una página de Facebook); si Metricool lo rechaza, seguir con la música propia.
   Anotar en el resumen semanal qué tendencias se usaron. Al menos 2 de las piezas de la semana tienen que salir de esta investigación.
3. **Elegir la semana.** Con `getScheduledPosts`, encontrar la primera semana (lunes a domingo) sin publicaciones programadas que empiece dentro de los próximos 14 días. Si no hay ninguna, no producir nada y avisar.
4. **Planificar.** Elegir temas que NO estén en `historial.md`. Mezclar los 5 servicios. Ideas de banco: errores de diseño, mitos de precios web, checklist de lanzamiento, antes de contratar un logo, qué pedirle a un editor de video, frecuencia de publicación, cómo responder mensajes, Google Business, velocidad de carga, fotos de producto, tipografías, paletas, reels sin mostrar la cara.
5. **Producir** con las plantillas de `sistema/semana1` y `sistema/semana2` (`hook`, `tip`, `cta`, `service` de `carruseles.py`; escenas de `motion.py` y `reels.py`; historias de `historias.py`). Reels de 11-15 s con música original de `sistema/audio/musica.py` (sincronizada con las animaciones y normalizada a -14 LUFS). Revisar visualmente cada pieza antes de subirla: textos legibles, nada cortado ni superpuesto, contenido importante fuera de los 340 px inferiores en reels e historias.
6. **Sin fotos de personas.** Nunca usar fotos, caras ni nombres personales de Luciano ni de los socios en posts, reels o historias. El protagonista es el trabajo.
7. **No inventar.** Sin testimonios, clientes, cifras ni casos que no existan. El único resultado real disponible es Dalinger Automotores: +1.500 seguidores en un año como community manager. Los trabajos académicos se presentan como proyectos, no como clientes.
8. **Subir** los archivos a `media/<AAAA-MM-DD del lunes>/`, hacer commit y push a `main`.
9. **Programar** cada pieza con `createScheduledPost` usando las URLs públicas (`type` POST, REEL o STORY; en reels, `videoThumbnailUrl` con la portada). Las historias van sin texto.
10. **Registrar** en `historial.md` la fecha, el formato y el tema de cada publicación. Commit y push.
11. **Avisar** al dueño con un resumen corto: qué sale cada día, qué historias con sticker tiene que subir a mano (si hay) y una recomendación de publicidad si algún post rindió muy bien.
