"""Original, royalty-free music beds for TriWeb reels, synthesized and synced to each animation's events."""
import sys, re, pathlib, subprocess
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 44100
sys.path.insert(0, '/home/claude/triweb/semana1'); sys.path.insert(0, '/home/claude/triweb')
OUT = pathlib.Path('/home/claude/triweb/audio'); OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(7)

def t_(dur): return np.arange(int(dur*SR))/SR
def env(n, a=0.005, d=0.2):
    t = np.arange(n)/SR; e = np.minimum(1, t/max(a, 1e-4))*np.exp(-np.maximum(0, t-a)/d); return e
def lp(x, f, order=2): return sosfilt(butter(order, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, order=2): return sosfilt(butter(order, f, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), x)
def midi(m): return 440*2**((m-69)/12)

def add(buf, x, at, gain=1.0):
    i = int(at*SR)
    if i >= len(buf): return
    x = x[:len(buf)-i]; buf[i:i+len(x)] += gain*x

# ---- instruments ----
def kick():
    t = t_(0.45); f = 45 + 95*np.exp(-t/0.04)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*env(len(t), 0.002, 0.18)
def hat(open_=False):
    n = rng.standard_normal(int(SR*(0.25 if open_ else 0.06)))
    return hp(n, 7000)*env(len(n), 0.001, 0.08 if open_ else 0.02)
def clap():
    n = rng.standard_normal(int(SR*0.3)); x = bp(n, 900, 3500)*env(len(n), 0.002, 0.11)
    t = t_(0.3); return x + 0.3*np.sin(2*np.pi*190*t)*env(len(t), 0.001, 0.05)
def saw(f, dur, det=0.0):
    t = t_(dur); ph = (f*(1+det))*t; return 2*(ph - np.floor(ph+0.5))
def bass(note, dur):
    x = saw(midi(note), dur) + 0.5*np.sin(2*np.pi*midi(note-12)*t_(dur))
    return lp(x, 380)*env(len(x), 0.004, dur*0.6)
def pad(notes, dur):
    x = sum(saw(midi(n), dur, d) for n in notes for d in (-0.004, 0.004))/ (2*len(notes))
    x = lp(x, 1500); n = len(x); a = int(0.35*SR); r = int(0.4*SR)
    e = np.ones(n); e[:a] = np.linspace(0, 1, a); e[-r:] = np.linspace(1, 0, r); return x*e
def pluck(note, dur=0.35):
    x = saw(midi(note), dur) * 0.6 + 0.4*np.sign(np.sin(2*np.pi*midi(note)*t_(dur)))
    return lp(x, 2600)*env(len(x), 0.002, 0.09)
def pop(pitch=84):
    t = t_(0.12); f = midi(pitch)*(1+0.5*np.minimum(1, t/0.03))
    return np.sin(2*np.pi*np.cumsum(f)/SR)*env(len(t), 0.001, 0.035)
def tick():
    t = t_(0.08); return (np.sin(2*np.pi*1500*t) + 0.5*np.sin(2*np.pi*2400*t))*env(len(t), 0.0005, 0.018)
def whoosh(dur=0.5):
    n = rng.standard_normal(int(SR*dur)); t = np.linspace(0, 1, len(n))
    x = bp(n, 600, 5000) * np.sin(np.pi*t)**2; return x
def riser(dur=1.4):
    n = rng.standard_normal(int(SR*dur)); t = np.linspace(0, 1, len(n))
    out = np.zeros_like(n); seg = len(n)//14
    for k in range(14):  # stepped bandpass sweep upward
        lo = 300*2**(k*0.32); s = slice(k*seg, (k+1)*seg if k < 13 else len(n))
        out[s] = bp(n[s], lo, min(lo*3, 18000))
    return out * t**2
def impact():
    k = kick()*1.3; n = rng.standard_normal(int(SR*1.6))
    crash = hp(n, 4000)*env(len(n), 0.002, 0.35)*0.14
    out = np.zeros(len(crash)); out[:len(k)] += k; return out + crash

# ---- arrangement ----
PROGS = {
 'a': [(57, [69, 72, 76]), (53, [69, 72, 77]), (48, [67, 72, 76]), (55, [67, 71, 74])],   # Am F C G
 'b': [(50, [65, 69, 74]), (58, [65, 70, 74]), (53, [65, 69, 72]), (48, [64, 67, 72])],   # Dm Bb F C
 'c': [(52, [67, 71, 76]), (48, [67, 72, 76]), (55, [67, 71, 74]), (50, [66, 69, 74])],   # Em C G D
}

def track(dur, bpm, prog, pops=(), ticks=(), whooshes=(), end=None, drop=0.0):
    beat = 60/bpm; bar = 4*beat
    L = int((dur+2)*SR); mus = np.zeros(L); drums = np.zeros(L); fx = np.zeros(L)
    nb = int(np.ceil(dur/bar))+1
    stop = end + 0.02 if end else dur   # drums cut on the ending hit, pad rings out
    for b in range(nb):
        root, chord = PROGS[prog][b % 4]; t0 = b*bar
        if t0 >= dur: break
        add(mus, pad(chord, bar+0.4), t0, 0.34)
        for e8 in range(8):
            t = t0 + e8*beat/2
            if t >= stop or t < drop: continue
            add(mus, bass(root - 12 + (12 if e8 in (3, 7) else 0), beat/2*0.9), t, 0.32)
        for q in range(4):
            t = t0 + q*beat
            if t >= stop: continue
            if t >= drop:
                add(drums, kick(), t, 0.62)
                if q in (1, 3): add(drums, clap(), t, 0.35)
            add(drums, hat(), t + beat/2, 0.16 if t >= drop else 0.08)
        # arpeggio on the chord tones, sixteenth feel on the second half of each bar
        if t0 >= drop:
            for s in range(8):
                t = t0 + 2*beat + s*beat/4
                if t < stop: add(mus, pluck(chord[s % 3] + 12), t, 0.16)
    for t in pops: add(fx, pop(84 + int(rng.integers(0, 5))*2), t, 0.35)
    for t in ticks: add(fx, tick(), t, 0.5)
    for t in whooshes: add(fx, whoosh(), max(0, t-0.25), 0.16)
    if end:
        r = riser(); add(fx, r, end - len(r)/SR, 0.10); add(fx, impact(), end, 0.9)
    # sidechain-style ducking of music under kicks
    mix = drums + mus*0.9 + fx
    mix = mix[:int(dur*SR)]
    n = len(mix); fade = int(0.6*SR); mix[-fade:] *= np.linspace(1, 0, fade)
    mix = np.tanh(mix*0.9)/np.tanh(0.9)            # gentle saturation / limiting
    mix = mix/ (np.max(np.abs(mix))+1e-9) * 0.89
    st = np.stack([mix, np.roll(mix, int(0.0007*SR))*0.98], 1)  # slight width
    return (st*32767).astype(np.int16)

def events(html):
    g = lambda attr: sorted({float(x) for x in re.findall(attr + r'="([\d.]+)', html)})
    return g('data-pop'), g('data-draw'), g('data-grow'), g('data-in')

def thin(ts, gap=0.12):
    out = []
    for t in sorted(ts):
        if not out or t - out[-1] >= gap: out.append(t)
    return out

def mux(video, wav, out):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(video), '-i', str(wav), '-map', '0:v', '-map', '1:a',
                    '-c:v', 'copy', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=7', '-ar', '44100', '-c:a', 'aac', '-b:a', '192k', '-shortest', str(out)], check=True)

if __name__ == '__main__':
    import motion, reels
    S1 = pathlib.Path('/home/claude/triweb/semana1')
    jobs = [
      # name, html, dur, bpm, prog, ending, video path, drop
      ('servicio-web', motion.web, 12, 120, 'a', 9.4, S1/'motion/triweb-servicio-web.mp4', 1.0),
      ('servicio-branding', motion.brand, 12, 120, 'b', 9.4, S1/'motion/triweb-servicio-branding.mp4', 1.0),
      ('servicio-video', motion.video, 12, 120, 'c', 9.4, S1/'motion/triweb-servicio-video.mp4', 1.0),
      ('servicio-community', motion.cmreel, 12, 120, 'a', 9.4, S1/'motion/triweb-servicio-community.mp4', 1.0),
      ('reel-tres-servicios', reels.reel_b, 11, 120, 'b', 6.4, S1/'4-reel-tres-servicios/triweb-4-reel-tres-servicios.mp4', 0.4),
      ('reel-prueba-5-segundos', reels.reel_a, 15, 120, 'c', 12.9, S1/'2-reel-prueba-5-segundos/triweb-2-reel-prueba-5-segundos.mp4', 2.9),
    ]
    for name, html, dur, bpm, prog, end, video, drop in jobs:
        pops, draws, grows, ins = events(html)
        ticks = []
        if name == 'reel-prueba-5-segundos':
            ticks = [4.2 + i*0.5 for i in range(5)]
        p = thin([t for t in pops + draws if abs(t - end) > 0.15 and t < dur - 0.3])
        w = thin([t for t in ins if 0.3 < t < end - 0.3 and all(abs(t - x) > 0.2 for x in p)], 0.8)
        data = track(dur, bpm, prog, pops=p, ticks=ticks, whooshes=w, end=end, drop=drop)
        wav = OUT / f'{name}.wav'; wavfile.write(wav, SR, data)
        tmp = video.with_suffix('.music.mp4'); mux(video, wav, tmp); tmp.replace(video)
        print('ok', name, len(p), 'pops', len(w), 'whooshes')
