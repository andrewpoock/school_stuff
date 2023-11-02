# stringsynth.py
#    synthesizer use Karplus-Strong algorithm

from random import random

from soundwave import SoundWave
from bqueue import BoundedQueue


class StringSynth:

    def __init__(self, volume=100, loopgain=0.99):
        self.set_loopgain(loopgain)
        self.set_volume(volume)

    def set_volume(self, volume):
        self._volume = volume/100

    def set_loopgain(self, factor):
        self._gain = factor

    def synthesize(self, freq, duration):
        # create queue
        samprate = SoundWave.samplerate
        qcap = round(samprate/freq)
        q = BoundedQueue(qcap)
        for i in range(qcap):
            q.enqueue((random()*2-1)*self._volume)

        # generate samples
        samples = []
        #damp = 0.5**(1/(samprate/freq*self._sustain))
        for i in range(round(duration*SoundWave.samplerate)):
            sample = q.dequeue()
            samples.append(sample)
            filter_sample = (sample+q.front())/2 * self._gain
            q.enqueue(filter_sample)
            
        return SoundWave(samples)

