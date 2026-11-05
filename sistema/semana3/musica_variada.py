"""Cuatro camas musicales originales y distintas (funk, lo-fi, cumbia, trap) para los reels de la semana del 2/11."""
import sys; sys.path.insert(0, '/home/claude/triweb/audio')
import numpy as np
from musica import *   # SR, t_, env, lp, hp, bp, midi, add, kick, hat, clap, saw, pad, pluck, pop, whoosh, riser, impact, rng

def finish(mix, dur):
    mix = mix[:int(dur*SR)]; f = int(0.5*SR); mix[-f:] *= np.linspace(1, 0, f)
    mix = np.tanh(mix*0.9)/np.tanh(0.9); mix = mix/(np.max(np.abs(mix))+1e-9)*0.89
    st = np.stack([mix, np.roll(mix, int(0.0006*SR))*0.98], 1); return (st*32767).astype(np.int16)

def fx_layer(L, whooshes, end, hits=()):
    fx = np.zeros(L)
    for t in whooshes: add(fx, whoosh(0.45), max(0, t-0.22), 0.14)
    for t in hits: add(fx, kick()*0.8, t, 0.5); add(fx, pop(88), t, 0.25)
    if end:
        r = riser(1.2); add(fx, r, end-len(r)/SR, 0.09); add(fx, impact(), end, 0.8)
    return fx

def snare():
    n = rng.standard_normal(int(SR*0.22)); t = t_(0.22)
    return bp(n, 1500, 7000)*env(len(n), 0.001, 0.07) + 0.5*np.sin(2*np.pi*185*t)*env(len(t), 0.001, 0.04)

# ---------- FUNK 108 bpm (E9 / A9 vamp, bajo sincopado, clavinet) ----------
def funk(dur, whooshes=(), end=None, hits=()):
    bpm = 108; s16 = 60/bpm/4; L = int((dur+2)*SR); m = np.zeros(L)
    bass_pat = [(0, 40, 2), (3, 52, 1), (6, 40, 1), (7, 43, 1), (10, 45, 2), (12, 47, 1), (14, 40, 1)]
    clav = [2, 5, 9, 11, 13]
    nbar = int(dur/(16*s16))+1
    for bar in range(nbar):
        t0 = bar*16*s16; root = 0 if bar % 2 == 0 else 5
        if end and t0 > end: break
        for i in range(16):
            t = t0+i*s16
            if end and t >= end: break
            add(m, hat(i % 4 == 2), t, 0.10 if i % 2 else 0.16)
            if i in (0, 7, 10): add(m, kick(), t, 0.6)
            if i in (4, 12): add(m, snare(), t, 0.42)
        for i, note, ln in bass_pat:
            t = t0+i*s16
            if not end or t < end:
                b = bass(note+root, s16*ln*0.9); add(m, lp(b*1.4, 900), t, 0.38)
        for i in clav:
            t = t0+i*s16
            if not end or t < end:
                for n in (64, 68, 71, 74):
                    x = np.sign(np.sin(2*np.pi*midi(n+root)*t_(0.11)))*env(int(0.11*SR), 0.001, 0.03)
                    add(m, bp(x, 600, 3500), t, 0.05)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

# ---------- LO-FI 84 bpm (Fmaj7 Em7 Dm7 Cmaj7, swing, crackle) ----------
def keys(notes, dur):
    t = t_(dur); x = sum(np.sin(2*np.pi*midi(n)*t) + 0.3*np.sin(4*np.pi*midi(n)*t) for n in notes)/len(notes)
    return x*env(len(t), 0.01, dur*0.7)*(1 + 0.15*np.sin(2*np.pi*4.5*t))
def lofi(dur, whooshes=(), end=None, hits=()):
    bpm = 84; beat = 60/bpm; L = int((dur+2)*SR); m = np.zeros(L)
    prog = [(53, [64, 67, 69, 72]), (52, [62, 67, 69, 71]), (50, [60, 65, 69, 72]), (48, [59, 64, 67, 71])]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat; root, ch = prog[bar % 4]
        add(m, keys(ch, 4*beat), t0, 0.28)
        add(m, lp(bass(root-12, 2*beat), 250), t0, 0.35); add(m, lp(bass(root-12, beat), 250), t0+2.5*beat, 0.3)
        for q in range(4):
            t = t0+q*beat
            if end and t >= end: continue
            if q in (0,) or (q == 2): add(m, lp(kick(), 2000), t + (0.5*beat if q == 2 else 0), 0.55)
            if q in (1, 3): add(m, lp(snare(), 3000), t, 0.32)
            add(m, hat(), t, 0.07); add(m, hat(), t + beat*0.62, 0.06)   # swing
    crackle = np.zeros(L); idx = rng.integers(0, L, int(dur*25)); crackle[idx] = rng.standard_normal(len(idx))*0.6
    m += hp(crackle, 2000)*0.15 + lp(rng.standard_normal(L), 900)*0.004
    m = lp(m, 4500)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

# ---------- CUMBIA 96 bpm (Am / Dm / E, güira, bajo 1-5, acordeón) ----------
def cumbia(dur, whooshes=(), end=None, hits=()):
    bpm = 96; beat = 60/bpm; L = int((dur+2)*SR); m = np.zeros(L)
    prog = [(45, [69, 72, 76]), (50, [69, 74, 77]), (52, [68, 71, 76]), (45, [69, 72, 76])]
    mel = [76, 74, 72, 74, 76, 76, 77, 76, 74, 72, 71, 72]
    k = 0
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat; root, ch = prog[bar % 4]
        for q in range(4):
            t = t0+q*beat
            if end and t >= end: continue
            add(m, lp(bass(root-12 + (7 if q % 2 else 0), beat*0.8), 400), t, 0.4)
            add(m, kick(), t, 0.35 if q % 2 == 0 else 0.2)
            # güira: largo-corto-corto
            for off, ln, g in ((0, 0.16, 0.10), (0.5, 0.05, 0.08), (0.75, 0.05, 0.08)):
                n = rng.standard_normal(int(SR*ln)); add(m, hp(n, 5000)*env(len(n), 0.01, ln*0.5), t+off*beat, g)
            # conga (tumbao) en el contratiempo
            tt = t_(0.12); add(m, np.sin(2*np.pi*(210 if q % 2 else 300)*tt)*env(len(tt), 0.001, 0.05), t+0.5*beat, 0.18)
            # acordeón: acordes en contratiempo
            for n in ch:
                x = saw(midi(n), beat*0.35) * (1 + 0.1*np.sin(2*np.pi*6*t_(beat*0.35)))
                add(m, lp(x, 2200)*env(len(x), 0.01, 0.15), t+0.5*beat, 0.05)
        if bar % 2 == 1 and (not end or t0 < end - 2*beat):
            for j in range(6):
                n = mel[k % len(mel)]; k += 1; d = beat/2
                x = saw(midi(n), d*0.95)*(1 + 0.12*np.sin(2*np.pi*6*t_(d*0.95)))
                add(m, lp(x, 2600)*env(len(x), 0.02, 0.3), t0 + j*d, 0.10)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)

# ---------- TRAP 140 half-time (Cm, 808 con glide, hats con rolls) ----------
def b808(note, dur, glide_to=None):
    t = t_(dur); f0 = midi(note); f1 = midi(glide_to) if glide_to else f0
    f = f0 + (f1-f0)*np.clip((t-dur*0.6)/(dur*0.3), 0, 1)
    x = np.sin(2*np.pi*np.cumsum(f)/SR)*env(len(t), 0.003, dur*0.8)
    return np.tanh(x*2.5)
def bell(note, dur=0.5):
    t = t_(dur); f = midi(note)
    return (np.sin(2*np.pi*f*t) + 0.4*np.sin(2*np.pi*f*2.76*t)*np.exp(-t/0.08))*env(len(t), 0.002, 0.25)
def trap(dur, whooshes=(), end=None, hits=()):
    bpm = 140; beat = 60/bpm; L = int((dur+2)*SR); m = np.zeros(L)
    mel = [72, 75, 79, 77, 75, 72, 74, 70]
    for bar in range(int(dur/(4*beat))+1):
        t0 = bar*4*beat
        if end and t0 >= end: break
        add(m, b808(36 if bar % 2 == 0 else 32, beat*2.5, 31 if bar % 4 == 3 else None), t0, 0.45)
        add(m, kick(), t0, 0.5); add(m, kick(), t0+2.5*beat, 0.4)
        add(m, clap(), t0+2*beat, 0.45)
        for i in range(8):
            t = t0+i*beat/2
            if end and t >= end: break
            if bar % 2 == 1 and i == 6:
                for r in range(6): add(m, hat(), t + r*beat/12, 0.12)
            else: add(m, hat(), t, 0.14)
        for j, n in enumerate(mel[:4] if bar % 2 == 0 else mel[4:]):
            add(m, bell(n), t0+j*beat, 0.10)
    return finish(m + fx_layer(L, whooshes, end, hits), dur)
