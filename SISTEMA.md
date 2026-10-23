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
| Lunes | Carrusel educativo (6-7 láminas) |
| Martes | Motion graphic / reel de un servicio |
| Miércoles | Carrusel (tips, errores comunes, mitos) |
| Jueves | Reel |
| Viernes | Carrusel o reel de prueba social / proceso |
| Sábado | Reel corto con llamado a la acción |
| Lunes a viernes | 1 historia por día (sin stickers; las de encuesta se entregan aparte para subir a mano) |

## Procedimiento semanal

1. **Preparar el entorno.** `cp -r sistema/* /home/claude/triweb/` (las herramientas usan esa ruta). Inter e Inter Display ya están instaladas. Playwright y ffmpeg también.
2. **Medir.** Con Metricool (`getAnalyticsDataByMetrics`) revisar alcance, guardados, compartidos y mensajes de los posts de las últimas 2 semanas. Anotar en `historial.md` qué temas y formatos rindieron más y repetir esos formatos con temas nuevos.
3. **Elegir la semana.** Con `getScheduledPosts`, encontrar la primera semana (lunes a domingo) sin publicaciones programadas que empiece dentro de los próximos 14 días. Si no hay ninguna, no producir nada y avisar.
4. **Planificar.** Elegir temas que NO estén en `historial.md`. Mezclar los 5 servicios. Ideas de banco: errores de diseño, mitos de precios web, checklist de lanzamiento, antes de contratar un logo, qué pedirle a un editor de video, frecuencia de publicación, cómo responder mensajes, Google Business, velocidad de carga, fotos de producto, tipografías, paletas, reels sin mostrar la cara.
5. **Producir** con las plantillas de `sistema/semana1` y `sistema/semana2` (`hook`, `tip`, `cta`, `service` de `carruseles.py`; escenas de `motion.py` y `reels.py`; historias de `historias.py`). Reels de 11-15 s con música original de `sistema/audio/musica.py` (sincronizada con las animaciones y normalizada a -14 LUFS). Revisar visualmente cada pieza antes de subirla: textos legibles, nada cortado ni superpuesto, contenido importante fuera de los 340 px inferiores en reels e historias.
6. **No inventar.** Sin testimonios, clientes, cifras ni casos que no existan. El único resultado real disponible es Dalinger Automotores: +1.500 seguidores en un año como community manager. Los trabajos académicos se presentan como proyectos, no como clientes.
7. **Subir** los archivos a `media/<AAAA-MM-DD del lunes>/`, hacer commit y push a `main`.
8. **Programar** cada pieza con `createScheduledPost` usando las URLs públicas (`type` POST, REEL o STORY; en reels, `videoThumbnailUrl` con la portada). Las historias van sin texto.
9. **Registrar** en `historial.md` la fecha, el formato y el tema de cada publicación. Commit y push.
10. **Avisar** al dueño con un resumen corto: qué sale cada día, qué historias con sticker tiene que subir a mano (si hay) y una recomendación de publicidad si algún post rindió muy bien.
