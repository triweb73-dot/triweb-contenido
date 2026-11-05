"""Música original semana del 9/11: house (R5), dembow/reggaetón (R6), bossa nova (R7). Sincronizada a los golpes, -14 LUFS al mezclar."""
import sys, pathlib
sys.path.insert(0, '/home/claude/triweb/audio'); sys.path.insert(0, '/home/claude/triweb/semana3'); sys.path.insert(0, '/home/claude/triweb/semana4')
import numpy as np
from scipy.io import wavfile
from musica import *
from musica_variada import finish, fx_layer, snare, keys

def dembow(dur, whooshes=(), end=None, hits=()):
    """Dembow 95 bpm: bombo en negras, snare en 'la' del 2 y 4 + 3er 16vo; bajo Am-F-C-G; pluck sintético."""
    bpm = 95; beat = 60/bpm; s16 = beat/4; L = int((dur+2)*SR); m = np.zeros(L)
    prog = [57, 53, 48, 55]; lead = [76, 74, 72, 74, 72, 69, 72, 71]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat; r = prog[bar % 4]
        for q in range(4):
            t = t0 + q*beat
            if end and t >= end: continue
            add(m, kick(), t, 0.6)
            add(m, snare(), t + 3*s16, 0.38)            # el "tú-ca" del dembow
            if q % 2 == 1: add(m, snare(), t + 0*s16, 0.30)
            add(m, hat(), t + 2*s16, 0.12)
            add(m, lp(bass(r-24, beat*0.9), 300), t, 0.4)
        for j in range(8):
            t = t0 + j*beat/2
            if (not end or t < end) and j % 2 == 0:
                add(m, pluck(lead[(bar*4 + j//2) % 8]), t + s16, 0.12)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def nylon(note, dur=0.6):
    t = t_(dur); f = midi(note)
    x = sum(np.sin(2*np.pi*f*k*t)/k**1.5 for k in range(1, 6))
    return lp(x, 3000)*env(len(t), 0.002, 0.25)

def bossa(dur, whooshes=(), end=None, hits=()):
    """Bossa nova 130 bpm (sensación de 2): Dm9 G13 Cmaj9 A7b9, guitarra con síncopa clásica, bajo 1-5, rim y shaker."""
    bpm = 130; beat = 60/bpm; e8 = beat/2; L = int((dur+2)*SR); m = np.zeros(L)
    prog = [(38, [53, 57, 60, 64]), (43, [53, 59, 64, 65]), (36, [52, 55, 59, 62]), (45, [55, 58, 61, 64])]
    comp = [0, 3, 6, 10, 13]          # síncopa de bossa en 16 corcheas (2 compases)
    rim = [0, 3, 6, 10, 12]
    for bar2 in range(int(dur/(8*beat))+1):
        t0 = bar2*8*beat
        for half in range(2):
            root, ch = prog[(bar2*2 + half) % 4]; tb = t0 + half*4*beat
            if end and tb >= end: break
            add(m, lp(bass(root, beat*1.4), 260), tb, 0.42); add(m, lp(bass(root+7, beat*1.4), 260), tb + 2*beat, 0.36)
        for i in range(16):
            t = t0 + i*e8
            if end and t >= end: break
            add(m, hp(rng.standard_normal(int(SR*0.05)), 6000)*env(int(SR*0.05), 0.01, 0.02), t, 0.06)  # shaker
            root, ch = prog[(bar2*2 + i//8) % 4]
            if i in comp:
                for k, n in enumerate(ch): add(m, nylon(n, 0.5), t + k*0.012, 0.09)
            if i in rim:
                tt = t_(0.05); add(m, bp(np.sin(2*np.pi*1700*tt) + rng.standard_normal(len(tt))*0.3, 1000, 4000)*env(len(tt), 0.0005, 0.012), t, 0.16)
            if i % 8 == 0: add(m, lp(kick(), 800), t, 0.4)
    m = lp(m, 6000)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

if __name__ == '__main__':
    import reels4 as R
    O = R.OUT
    jobs = {
      'antes-despues-web': lambda: track(15.0, 124, 'c', pops=[4.7, 7.3, 9.9], whooshes=[2.3, 2.9, 4.35, 6.95, 9.55], end=12.1, drop=2.9),
      'instagram-original': lambda: dembow(13.0, whooshes=[3.4, 9.8], end=9.8, hits=[3.5, 5.6, 7.7]),
      'google-3-pasos': lambda: bossa(20.0, whooshes=[1.9, 4.4, 8.6, 12.8, 13.5, 14.2], end=17.1, hits=[3.2]),
    }
    for name, fn in jobs.items():
        if len(sys.argv) > 1 and name not in sys.argv[1:]: continue
        wav = O/name/'musica.wav'; wavfile.write(wav, SR, fn())
        mux(O/name/'video.mp4', wav, O/name/f'triweb-{name}.mp4'); print('ok', name)
