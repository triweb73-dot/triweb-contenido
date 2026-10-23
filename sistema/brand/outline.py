import sys; sys.path.insert(0,'brand')
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from mark import mark
F='/usr/share/fonts/opentype/inter/'
def text_path(s,font,size,x,y,track=0):
    f=TTFont(F+font); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm; sc=size/upm
    out=[]
    for ch in s:
        g=cmap[ord(ch)]; pen=SVGPathPen(gs)
        gs[g].draw(TransformPen(pen,(sc,0,0,-sc,x,y))); out.append(pen.getCommands())
        x+=gs[g].width*sc+track
    return ' '.join(out),x
INK="#0F1222"; CREMA="#F5F2EA"
def wordmark(fg,x0=222,y=132,size=112):
    a,x=text_path('tri','InterDisplay-ExtraBold.otf',size,x0,y,-4)
    b,x=text_path('web','InterDisplay-Regular.otf',size,x,y,-4)
    return f'<path d="{a} {b}" fill="{fg}"/>',x
def horizontal(fg):
    wm,x=wordmark(fg); w=int(x+16)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 200" width="{w}" height="200"><g transform="translate(10,0)">{mark(200)}</g>{wm}</svg>'
def mono(fg):  # single-ink mark
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">{mark(200,colors=(fg,fg,fg))}</svg>'
if __name__=='__main__':
    open('brand/triweb-logo.svg','w').write(horizontal(INK))
    open('brand/triweb-logo-crema.svg','w').write(horizontal(CREMA))
    open('brand/triweb-isotipo.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">{mark(200)}</svg>')
    open('brand/triweb-isotipo-mono.svg','w').write(mono(INK))
    open('brand/triweb-avatar.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="320" height="320"><rect width="320" height="320" fill="{INK}"/><g transform="translate(40,28) scale(1.2)">{mark(200)}</g></svg>')
