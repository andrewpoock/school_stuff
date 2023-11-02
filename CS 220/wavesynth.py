# wavesynth.py
# Andrew Poock
#    Simple waveform synthesizer based on tonelib


import tonelib
from soundwave import SoundWave


class WaveSynth:

    """A WaveSynth generates SoundWaves representing simple tones with
    adjustable waveform (sine, triangle, square, and sawtooth), decay
    time, and volume.

    """

    _WAVE_FNS = {"sine": tonelib.sinewave,
                 "triangle": tonelib.trianglewave,
                 "square": tonelib.squarewave,
                 "sawtooth": tonelib.sawtoothwave
                 }             

    def __init__(self, waveform="sine", sustain=0, volume=100):
        self.set_waveform(waveform)
        self.set_sustain(sustain)
        self.set_volume(volume)

    def set_waveform(self, waveform):
        """ set sythesizer's wave form
        pre: waveform in ["sine", "square", "triangle", "sawtooth"]
        post: synthesize will use the specified wave function
        """
        self._wavefn = WaveSynth._WAVE_FNS[waveform]

    def set_sustain(self, sustain):
        """ set amount of sustain
        pre: sustain is "half-life" of tone in seconds
        post: if sustain is 0, tones will have infinite sustain, otherwise
              tones will decay with a half-life equal to sustain.
        """
        self._sustain = sustain

    def set_volume(self, pct):
        """ set volume as a percentage
        pre: 0 <= pct <= 100
        post: generated tones will have max amplitude of pct/100
        """
        self._volume = pct/100

    def synthesize(self, freq, duration):
        """ generate tone
        pre: duration > 0
        post: returns a SoundWave with given frequency and duration (in seconds) with
              waveform, sustain, and volume as previously set.
        """
        
        self._samples = tonelib.tone(self._wavefn, freq, duration, self._volume)
        if self._sustain != 0:
            tonelib.fadeout(self._samples, self._sustain)
        return SoundWave(self._samples)
