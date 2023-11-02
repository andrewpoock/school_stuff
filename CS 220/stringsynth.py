# stringsynth.py
#    synthesizer use Karplus-Strong algorithm
# Andrew Poock

from random import random

from soundwave import SoundWave
from bqueue import BoundedQueue

SAMPLERATE = 44100

class StringSynth:

    def __init__(self, volume=100, loopgain=0.99):
        """Create a synth with the given volume and loopgain"""
        self.set_loopgain(loopgain)
        self.set_volume(volume)

    def set_volume(self, volume):
        """Set volume"""
        self._volume = volume

    def set_loopgain(self, factor):
        """Set loopgain"""
        self._loopgain = factor

    def synthesize(self, freq, duration):
        """Syntehsize a tone with the Karplus-Strong algorithm"""
        cap = int(SAMPLERATE/freq)
        q = BoundedQueue(cap)
        while q.isfull() == False:
            num = (random()*2-1)*self._volume
            q.enqueue(num)
        samples = []
        n = int(SAMPLERATE*duration)
        for i in range(n):
            sample = q.dequeue()
            samples.append(sample)
            avg_sample = (sample + q.front())/2 * self._loopgain
            q.enqueue(avg_sample)
        return SoundWave(samples)
        
