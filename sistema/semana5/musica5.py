"""Música original semana del 16/11: synthwave (A), chiptune (B), boom bap (C), afro house (D). Sincronizada a los golpes; -14 LUFS en mux()."""
import sys
sys.path.insert(0, '/home/claude/triweb/audio'); sys.path.insert(0, '/home/claude/triweb/semana3'); sys.path.insert(0, '/home/claude/triweb/semana5')
import numpy as np
from scipy.io import wavfile
from musica import *
from musica_variada import finish, fx_layer, snare, keys

def square(note, dur, duty=0.5):
    t = t_(dur); ph = (t*midi(note)) % 1
    return np.where(ph < duty, 1.0, -1.0)*env(len(t), 0.002, dur*0.7)

def synthwave(dur, whooshes=(), end=None, hits=()):
    """100 bpm, bombo/clap 4x4 con gated reverb, bajo en corcheas, pad de sierras Am-F-C-G y arpegio."""
    bpm = 100; beat = 60/bpm; L = int((dur+2)*SR); m = np.zeros(L)
    prog = [(45, [57, 60, 64]), (41, [53, 57, 60]), (48, [55, 60, 64]), (43, [55, 59, 62])]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat; root, ch = prog[bar % 4]
        if end and t0 >= end: break
        add(m, lp(pad(ch, 4*beat), 2500), t0, 0.16)
        for q in range(4):
            t = t0 + q*beat
            if end and t >= end: continue
            add(m, kick(), t, 0.55)
            if q % 2: add(m, clap(), t, 0.3)
            for e in range(2):
                add(m, lp(bass(root-12, beat*0.45), 500), t + e*beat/2, 0.33)
            for s in range(4):
                add(m, pluck(ch[(q*4+s) % 3] + 12, 0.18), t + s*beat/4, 0.06)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def chiptune(dur, whooshes=(), end=None, hits=()):
    """150 bpm, cuadradas de 8 bits: melodía, bajo en pulso 25% y ruido como batería."""
    bpm = 150; beat = 60/bpm; e8 = beat/2; L = int((dur+2)*SR); m = np.zeros(L)
    mel = [72, 76, 79, 76, 74, 77, 81, 77, 72, 76, 79, 84, 83, 79, 74, 71]; bas = [48, 48, 53, 53, 48, 48, 55, 55]
    for i in range(int(dur/e8)+1):
        t = i*e8
        if end and t >= end: break
        add(m, square(mel[i % 16], e8*0.9, 0.5), t, 0.07)
        if i % 2 == 0: add(m, square(bas[(i//2) % 8]-12, beat*0.8, 0.25), t, 0.09)
        if i % 4 == 0: add(m, lp(kick(), 1200), t, 0.5)
        if i % 4 == 2: n = int(SR*0.08); add(m, rng.standard_normal(n)*env(n, 0.001, 0.04), t, 0.18)
        add(m, hp(rng.standard_normal(int(SR*0.02)), 7000)*env(int(SR*0.02), 0.001, 0.008), t, 0.05)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def boombap(dur, whooshes=(), end=None, hits=()):
    """90 bpm, bombo y caja secos con swing, Rhodes en Dm9-G7, contrabajo y crujido de vinilo."""
    bpm = 90; beat = 60/bpm; L = int((dur+2)*SR); m = np.zeros(L)
    chords = [(38, [53, 57, 60, 64]), (43, [53, 59, 62, 65])]
    sw = beat*0.58
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat; root, ch = chords[bar % 2]
        if end and t0 >= end: break
        add(m, keys(ch, 4*beat*0.9), t0, 0.16)
        for q in range(4):
            t = t0 + q*beat
            if end and t >= end: continue
            if q in (0, 2): add(m, lp(kick(), 900), t, 0.6)
            if q == 2: add(m, lp(kick(), 900), t + sw, 0.4)
            if q in (1, 3): add(m, snare(), t, 0.42)
            add(m, hat(), t, 0.08); add(m, hat(), t + sw, 0.06)
            add(m, lp(bass(root-12, beat*0.8), 220), t if q % 2 == 0 else t + sw, 0.4)
    m += hp(rng.standard_normal(L), 3000)*0.004*(rng.random(L) > 0.9993)*30 + hp(rng.standard_normal(L), 5000)*0.003
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

def afrohouse(dur, whooshes=(), end=None, hits=()):
    """118 bpm, bombo 4x4, congas sintéticas en tresillo, shaker y marimba pentatónica."""
    bpm = 118; beat = 60/bpm; s16 = beat/4; L = int((dur+2)*SR); m = np.zeros(L)
    def conga(f):
        t = t_(0.18); return np.sin(2*np.pi*f*t*(1+0.3*np.exp(-t*40)))*np.exp(-t*22)
    def marimba(n):
        t = t_(0.4); f = midi(n); return (np.sin(2*np.pi*f*t) + 0.3*np.sin(2*np.pi*4*f*t)*np.exp(-t*30))*np.exp(-t*9)
    pat = [0, 3, 6, 10, 12]; mel = [69, 72, 74, 76, 79, 76, 74, 72]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat
        for i in range(16):
            t = t0 + i*s16
            if end and t >= end: break
            if i % 4 == 0: add(m, kick(), t, 0.55); add(m, lp(bass(45 if bar % 2 == 0 else 43, beat*0.5), 300), t + 2*s16, 0.3)
            if i in pat: add(m, conga(220 if i % 2 else 330), t, 0.25)
            add(m, hp(rng.standard_normal(int(SR*0.04)), 6000)*env(int(SR*0.04), 0.01, 0.015), t, 0.05 if i % 2 else 0.08)
            if i in (2, 7, 10, 14): add(m, marimba(mel[(bar*4 + i) % 8]), t, 0.13)
            if i in (4, 12): add(m, clap(), t, 0.18)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

if __name__ == '__main__':
    import reels5 as R
    O = R.OUT
    jobs = {
      'error-web-3-segundos': lambda: synthwave(14.0, whooshes=[2.4, 3.8, 5.4, 6.8, 8.4, 9.8], end=11.4, hits=[0.05, 3.3, 6.3, 9.3]),
      'pov-black-friday-notas': lambda: chiptune(10.5, whooshes=[2.0, 3.45, 4.9, 6.35], end=8.3, hits=[6.9]),
      'detras-marca-sura': lambda: boombap(16.0, whooshes=[2.4, 5.1, 7.8, 10.5], end=13.4, hits=[0.1]),
      'novedad-grilla-etiquetas': lambda: afrohouse(12.6, whooshes=[2.5, 7.2, 8.2, 9.2], end=10.2, hits=[4.4]),
    }
    for name, fn in jobs.items():
        if len(sys.argv) > 1 and name not in sys.argv[1:]: continue
        wav = O/name/'musica.wav'; wavfile.write(wav, SR, fn())
        mux(O/name/'video.mp4', wav, O/name/f'triweb-{name}.mp4'); print('ok', name)
