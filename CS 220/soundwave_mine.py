# soundwave.py
#    An object for representing and combining sounds.


import tonelib


class SoundWave:

    """A SoundWave is represented as a sequence of samples (floats in
    the range -1 to 1) sampled at 44100 hz.
    """

    samplerate = tonelib.SAMPLERATE

    def __init__(self, samples=[]):
        self._samples = list(samples)

    def __len__(self):
        return len(self._samples)

    def extend(self, sw):
        self._samples.extend(sw._samples)

    def duration(self):
        return len(self._samples)/self.samplerate

    def maxamp(self):
        minn = min(self._samples)
        maxx = max(self._samples)
        if abs(minn) > abs(maxx):
            return abs(minn)
        elif abs(maxx) > abs(minn):
            return abs(maxx)
        else:
            return abs(maxx)

    def clamp(self):
        for i in range(len(self._samples)):
            if abs(self._samples[i]) > 1.0:
                self._samples[i] = (self._samples[i]/abs(self._samples[i]))

    def normalize(self):
        max_amp = self.maxamp()
        for i, num in enumerate(self._samples):
            num = (num/max_amp)
            self._samples[i] = num

    def __add__(self, sw):
        if len(self._samples) < len(sw._samples):
            self._samples, sw._samples = sw._samples, self._samples

        samples = list(self._samples)
        for i in range(len(sw._samples)):
            samples[i] += sw._samples[i]
        return SoundWave(samples)

    def __mul__(self, factor):
        for i in range(len(self._samples)):
            self._samples[i] = self._samples[i]*factor
        return SoundWave(self._samples)

    def __rmul__(self, factor):
        for i in range(len(self._samples)):
            self._samples[i] = factor*self._samples[i]
        return SoundWave(self._samples)

    def play(self):
        tonelib.playsound(self._samples)

    def tofile(self, fname):
        tonelib.write_wavefile(self._samples, fname)
