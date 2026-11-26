"""Música original semana del 30/11: electro swing (A), techno minimal (B), amapiano (C), chacarera electrónica 6/8 (D).
Sincronizada con los golpes de cada reel; normalizada a -14 LUFS en mux()."""
import sys
sys.path.insert(0, '/home/claude/triweb/audio'); sys.path.insert(0, '/home/claude/triweb/semana3'); sys.path.insert(0, '/home/claude/triweb/semana7')
import numpy as np
from scipy.io import wavfile
from musica import *
from musica_variada import finish, fx_layer, snare, keys

def horn(note, dur):
    """Bronce sintético: sierra filtrada con ataque suave y vibrato."""
    t = t_(dur); f = midi(note)*(1 + 0.006*np.sin(2*np.pi*5.5*t)*np.clip(t*3, 0, 1)); ph = np.cumsum(f)/SR
    x = lp(2*(ph % 1) - 1, 2400); n = len(x); a = int(0.04*SR); e = np.ones(n); e[:a] = np.linspace(0, 1, a); e[-int(0.06*SR):] *= np.linspace(1, 0, int(0.06*SR))
    return x*e

def electroswing(dur, whooshes=(), end=None, hits=()):
    """124 bpm, bombo 4x4, caja en 2 y 4, contrabajo caminando, hats con swing y riffs de bronce (Gm)."""
    bpm = 124; beat = 60/bpm; sw = beat*0.16; L = int((dur+2)*SR); m = np.zeros(L)
    walk = [43, 46, 48, 50, 51, 50, 48, 46]; riff = [67, 70, 72, 74, 72, 70]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat
        for q in range(4):
            t = t0 + q*beat
            if end and t >= end: break
            add(m, kick(), t, 0.5)
            if q % 2: add(m, snare(), t, 0.3)
            add(m, hat(), t + beat/2 + sw, 0.09); add(m, hat(), t, 0.04)
            add(m, lp(bass(walk[(bar*4+q) % 8]-12, beat*0.9), 500), t, 0.4)
        if not end or t0 + beat < end:
            for k, n in enumerate(riff[:3] if bar % 2 else riff[3:]):
                add(m, horn(n, beat*0.45), t0 + 2*beat + k*(beat/2 + (sw if k % 2 else 0)), 0.1)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def techno(dur, whooshes=(), end=None, hits=()):
    """126 bpm minimal: bombo seco, clap con eco, hat abierto a contratiempo, bajo de 16avos y blip de rim."""
    bpm = 126; beat = 60/bpm; s16 = beat/4; L = int((dur+2)*SR); m = np.zeros(L)
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat
        for i in range(16):
            t = t0 + i*s16
            if end and t >= end: break
            if i % 4 == 0: add(m, kick(), t, 0.62)
            if i in (4, 12): add(m, clap(), t, 0.22); add(m, clap(), t + 3*s16, 0.06)
            if i % 4 == 2: add(m, hat(True), t, 0.08)
            if i in (1, 3, 6, 9, 11, 14): add(m, lp(bass(33 + (5 if bar % 4 == 3 else 0), s16*0.8), 260), t, 0.38)
            if i in (7, 13) and bar % 2: add(m, hp(pluck(81, 0.08), 1500), t, 0.08)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def logdrum(note, dur=0.35):
    """El 'log drum' del amapiano: seno grave con caída de tono rápida y algo de saturación."""
    t = t_(dur); f = midi(note)*(1 + 1.5*np.exp(-t*40)); x = np.sin(2*np.pi*np.cumsum(f)/SR)
    return np.tanh(2.2*x)*np.exp(-t*7)

def amapiano(dur, whooshes=(), end=None, hits=()):
    """112 bpm: shaker en 16avos, bombo suelto, log drum sincopado y acordes de piano jazzero (Dm9-G13)."""
    bpm = 112; beat = 60/bpm; s16 = beat/4; L = int((dur+2)*SR); m = np.zeros(L)
    prog = [[62, 65, 69, 72, 76], [59, 64, 67, 71, 74], [60, 64, 67, 71, 74], [57, 61, 64, 67, 71]]
    roots = [38, 43, 36, 33]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat
        if end and t0 >= end: break
        for i in range(16):
            t = t0 + i*s16
            if end and t >= end: break
            add(m, hp(rng.standard_normal(int(SR*0.04)), 6000)*env(int(SR*0.04), 0.002, 0.02), t, 0.05 if i % 2 else 0.03)
            if i in (0, 8): add(m, kick(), t, 0.42)
            if i in (4, 12): add(m, clap(), t, 0.16)
            if i in (3, 6, 10, 11, 14): add(m, logdrum(roots[bar % 4], 0.3), t, 0.3)
            if i in (0, 6, 12): add(m, keys(prog[bar % 4], s16*2.5), t, 0.12)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def guitarra(note, dur=0.4):
    """Rasguido de criolla: pulsado brillante con caída rápida."""
    return hp(pluck(note, dur), 200)

def bombo_leg(dur=0.3):
    t = t_(dur); return np.sin(2*np.pi*np.cumsum(70*(1 + np.exp(-t*30)))/SR)*np.exp(-t*12)

def chacarera(dur, whooshes=(), end=None, hits=()):
    """6/8 a 100 negras con punto por minuto: bombo legüero (parche y aro), rasguido en Am-E y bajo de sintetizador; bombo 4x4 debajo."""
    q = 60/100/2  # corchea
    L = int((dur+2)*SR); m = np.zeros(L)
    prog = [(45, [57, 60, 64]), (40, [56, 59, 64]), (45, [57, 60, 64]), (40, [56, 59, 64])]
    for bar in range(int(dur/(6*q))+1):
        t0 = bar*6*q; root, ch = prog[bar % 4]
        for i in range(6):
            t = t0 + i*q
            if end and t >= end: break
            if i in (0, 3): add(m, kick(), t, 0.45)
            if i in (0, 2, 3, 5): add(m, bombo_leg(), t, 0.35 if i in (2, 5) else 0.2)
            if i in (1, 4): add(m, hp(rng.standard_normal(int(SR*0.03)), 3000)*env(int(SR*0.03), 0.001, 0.015), t, 0.12)  # aro
            for k, n in enumerate(ch): add(m, guitarra(n, 0.3), t + k*0.012, 0.06 if i in (0, 2, 3, 5) else 0.03)
            if i in (0, 3, 5): add(m, lp(bass(root-12, q*1.2), 400), t, 0.38)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

if __name__ == '__main__':
    import reels7 as R
    O = R.OUT
    jobs = {
      'mitos-del-logo': lambda: electroswing(15.5, whooshes=[2.2, 5.9, 9.6], end=13.5, hits=[0.15, 4.1, 7.8, 11.5]),
      'links-vs-web': lambda: techno(13.0, whooshes=[2.4, 4.4, 6.4, 8.4], end=10.6, hits=[0.0, 0.7, 2.4, 4.4, 6.4, 8.4]),
      'preguntas-web': lambda: amapiano(17.5, whooshes=[1.9, 5.4, 8.2, 11.0], end=14.05, hits=[0.0, 2.6]),
      'antes-despues-marca': lambda: chacarera(12.5, whooshes=[4.6, 5.2, 5.8, 6.4], end=8.5, hits=[0.9, 1.05, 1.2, 1.35]),
    }
    for name, fn in jobs.items():
        if len(sys.argv) > 1 and name not in sys.argv[1:]: continue
        wav = O/name/'musica.wav'; wavfile.write(wav, SR, fn())
        mux(O/name/'video.mp4', wav, O/name/f'triweb-{name}.mp4'); print('ok', name)
