import math
# equilateral triangle, three separate rounded strokes with gaps
def mark(size=200, sw=None, colors=("#3B5BFF","#FF5C4D","#FFC233")):
    sw = sw or size*0.12
    cx, cy, r = size/2, size*0.56, size*0.40
    pts=[(cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a))) for a in (-90,30,150)]
    gap=0.21
    segs=[]
    for i in range(3):
        (x1,y1),(x2,y2)=pts[i],pts[(i+1)%3]
        ax,ay=x1+(x2-x1)*gap,y1+(y2-y1)*gap
        bx,by=x1+(x2-x1)*(1-gap),y1+(y2-y1)*(1-gap)
        segs.append(f'<line x1="{ax:.2f}" y1="{ay:.2f}" x2="{bx:.2f}" y2="{by:.2f}" stroke="{colors[i]}" stroke-width="{sw:.2f}" stroke-linecap="round"/>')
    return "\n".join(segs)
