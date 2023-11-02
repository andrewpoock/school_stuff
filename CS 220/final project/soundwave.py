# soundwave.py
#    An object for representing and combining sounds.
# by: John Zelle


import tonelib


class SoundWave:

    """A SoundWave is represented as a sequence of samples (floats in
    the range -1 to 1) sampled at 44100 hz.
    """

    samplerate = tonelib.SAMPLERATE

    def __init__(self, samples=[]):
        assert all(
            type(x) == float for x in samples), "samples must be a sequence of floats"
        self.samples = list(samples)

    def extend(self, other):
        """ add samples at the end
        pre: other is a SoundWave with same samplerate as self
        post: self has been extended with the samples from other
        """

        if not isinstance(other, SoundWave):
            raise valueError("argument must be a SoundWave")

        self.samples.extend(other.samples)

    def duration(self):
        """ return the length (playing time) in seconds
        """
        return len(self.samples)/self.samplerate

    def maxamp(self):
        """ return max deviation from 0.0
        """
        ma = 0.0
        for s in self.samples:
            if abs(s) > ma:
                ma = abs(s)
        return ma

    def clamp(self):
        """ truncate all samples to the range -1.0 to 1.0
        """
        for i, s in enumerate(self.samples):
            self.samples[i] = max(min(s, 1.0), -1.0)

    def normalize(self):
        """ scale samples (via multiplication) to the range -1.0 to 1.0
        """
        factor = self.maxamp()
        for i, s in enumerate(self.samples):
            self.samples[i] = s/factor

    def tofile(self, filename):
        """ write this SoundWave to a wave (.wav) file.
        """
        tonelib.write_wavefile(self.samples, filename)

    def play(self):
        """ play this soundwave
        """
        tonelib.playsound(self.samples)

    def __len__(self):
        """ return the number of samples in this SoundWave
        """
        return len(self.samples)

    def __add__(self, other):
        """component-wise sum of self and other 
        post: returns a new SoundWave that is the sum of self and other
        """

        s1 = self.samples
        s2 = other.samples

        if len(s1) < len(s2):
            s1, s2 = s2, s1
        samples = list(s1)
        for i, a in enumerate(s2):
            samples[i] += a
        return SoundWave(samples)

    def __mul__(self, factor):
        """ return SoundWave like self with each sample multiplied by factor
        """
        samples = [s*factor for s in self.samples]
        return SoundWave(samples)

    def __rmul__(self, factor):
        """ return SoundWave like self with each sample multiplied by factor
        """
        return self * factor
