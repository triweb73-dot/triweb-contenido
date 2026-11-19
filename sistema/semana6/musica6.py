"""Música original semana del 23/11: tango electrónico (A), drum & bass (B), UK garage 2-step (C), nu-disco (D).
Sincronizada con los golpes de cada reel; normalizada a -14 LUFS en mux()."""
import sys
sys.path.insert(0, '/home/claude/triweb/audio'); sys.path.insert(0, '/home/claude/triweb/semana3'); sys.path.insert(0, '/home/claude/triweb/semana6')
import numpy as np
from scipy.io import wavfile
from musica import *
from musica_variada import finish, fx_layer, snare, keys

def bandoneon(note, dur):
    """Lengüetas: dos sierras desafinadas + cuadrada, filtro medio, vibrato lento y ataque de fuelle."""
    t = t_(dur); f = midi(note)*(1 + 0.004*np.sin(2*np.pi*5.2*t))
    ph = np.cumsum(f)/SR
    x = (2*((ph) % 1) - 1)*0.5 + (2*((ph*1.006) % 1) - 1)*0.5 + 0.4*np.sign(np.sin(2*np.pi*ph*2))
    x = bp(x, 300, 3200); n = len(x); a = int(0.06*SR)
    e = np.ones(n); e[:a] = np.linspace(0, 1, a); e[-int(0.08*SR):] *= np.linspace(1, 0, int(0.08*SR)); return x*e

def tango(dur, whooshes=(), end=None, hits=()):
    """116 bpm, marcato en 4 con acento 3-3-2, bajo de contrabajo sintético, bandoneón en staccato Am-Dm-E."""
    bpm = 116; beat = 60/bpm; e8 = beat/2; L = int((dur+2)*SR); m = np.zeros(L)
    prog = [(45, [69, 72, 76]), (50, [69, 74, 77]), (52, [68, 71, 76]), (45, [69, 72, 76])]
    mel = [76, 77, 76, 72, 74, 76, 71, 69]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat; root, ch = prog[bar % 4]
        for i in range(8):
            t = t0 + i*e8
            if end and t >= end: break
            if i in (0, 3, 6): add(m, kick(), t, 0.5); add(m, lp(bass(root-12, e8*1.4), 300), t, 0.42)
            if i in (2, 6): add(m, snare(), t, 0.22)
            if i in (0, 3, 6):
                for n in ch: add(m, bandoneon(n-12, e8*0.8), t, 0.07)
            add(m, hp(rng.standard_normal(int(SR*0.03)), 5000)*env(int(SR*0.03), 0.001, 0.01), t, 0.05)
        if not end or t0 + 2*beat < end:
            add(m, bandoneon(mel[(bar*2) % 8], beat*1.6), t0 + 2*beat, 0.12); add(m, bandoneon(mel[(bar*2+1) % 8], beat*0.9), t0 + 3.5*beat, 0.1)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def dnb(dur, whooshes=(), end=None, hits=()):
    """172 bpm, break de dos pasos (bombo 1 y 2.5, caja 2 y 4), reese bass y pad en Fm."""
    bpm = 172; beat = 60/bpm; L = int((dur+2)*SR); m = np.zeros(L)
    roots = [41, 41, 44, 39]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat; r = roots[bar % 4]
        if end and t0 >= end: break
        add(m, lp(pad([r+24, r+27, r+31], 4*beat), 1800), t0, 0.12)
        reese = lp(saw(midi(r-12), 4*beat, -0.006) + saw(midi(r-12), 4*beat, 0.006), 380)*env(int(4*beat*SR), 0.01, 4*beat)
        add(m, reese, t0, 0.2)
        for k, (pos, kind) in enumerate([(0, 'k'), (1, 's'), (2.5, 'k'), (3, 's'), (3.75, 'g')]):
            t = t0 + pos*beat
            if end and t >= end: continue
            if kind == 'k': add(m, kick(), t, 0.6)
            elif kind == 's': add(m, snare(), t, 0.48)
            else: add(m, snare(), t, 0.15)
        for s in range(8): add(m, hat(), t0 + s*beat/2, 0.07 if s % 2 else 0.04)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def garage(dur, whooshes=(), end=None, hits=()):
    """132 bpm 2-step: bombo saltado, clap en 2 y 4, hats con swing, acordes de órgano cortados y sub bass."""
    bpm = 132; beat = 60/bpm; s16 = beat/4; sw = s16*0.18; L = int((dur+2)*SR); m = np.zeros(L)
    prog = [(46, [61, 65, 68, 72]), (44, [60, 63, 68, 70]), (41, [60, 63, 65, 68]), (39, [58, 63, 65, 67])]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat; root, ch = prog[bar % 4]
        for i in range(16):
            t = t0 + i*s16 + (sw if i % 2 else 0)
            if end and t >= end: break
            if i in (0, 10): add(m, kick(), t, 0.55)
            if i in (4, 12): add(m, clap(), t, 0.32)
            if i % 2: add(m, hat(), t, 0.07)
            if i in (3, 6, 11, 14): add(m, keys(ch, s16*1.5), t, 0.16)
            if i in (0, 7, 10): add(m, lp(bass(root-12, s16*3), 180), t, 0.42)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def nudisco(dur, whooshes=(), end=None, hits=()):
    """120 bpm, bombo 4x4, hat abierto a contratiempo, bajo de octavas, guitarra 'chicken scratch' y cuerdas."""
    bpm = 120; beat = 60/bpm; L = int((dur+2)*SR); m = np.zeros(L)
    prog = [(45, [64, 69, 72]), (43, [62, 67, 71]), (41, [60, 65, 69]), (40, [59, 64, 68])]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat; root, ch = prog[bar % 4]
        if end and t0 >= end: break
        add(m, lp(pad([n+12 for n in ch], 4*beat), 3000), t0, 0.1)
        for q in range(4):
            t = t0 + q*beat
            if end and t >= end: continue
            add(m, kick(), t, 0.55); add(m, hat(True), t + beat/2, 0.08)
            if q % 2: add(m, clap(), t, 0.25)
            for e in range(2): add(m, lp(bass(root-12 + 12*e, beat*0.4), 900), t + e*beat/2, 0.3)
            for s in (1, 3): add(m, hp(pluck(ch[s % 3], 0.07), 900), t + s*beat/4, 0.1)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

if __name__ == '__main__':
    import reels6 as R
    O = R.OUT
    jobs = {
      'confesion-logo-sura': lambda: tango(9.5, whooshes=[3.45, 6.35], end=6.5, hits=[0.05, 4.9]),
      'quiz-a-o-b-web': lambda: dnb(15.0, whooshes=[7.2, 8.5, 9.8, 11.65], end=11.8, hits=[0.1, 3.0, 4.0, 5.0, 6.0]),
      'novedad-ia-edits': lambda: garage(12.0, whooshes=[3.75, 4.1, 6.2], end=9.5, hits=[]),
      'landing-7-dias-black-friday': lambda: nudisco(16.0, whooshes=[2.9, 9.5], end=9.5, hits=[0.15, 1.2, 3.0, 5.0, 7.0]),
    }
    for name, fn in jobs.items():
        if len(sys.argv) > 1 and name not in sys.argv[1:]: continue
        wav = O/name/'musica.wav'; wavfile.write(wav, SR, fn())
        mux(O/name/'video.mp4', wav, O/name/f'triweb-{name}.mp4'); print('ok', name)
