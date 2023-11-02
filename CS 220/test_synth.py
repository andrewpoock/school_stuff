# test_synth.py
# Andrew Poock

import unittest
from wavesynth import WaveSynth


class TestSynth(unittest.TestCase):

    def test_default(self):
        synth = WaveSynth()
        test1 = synth.synthesize(220, .5)
        test1.extend(synth.synthesize(440, 2))
        test1.tofile("synth_test1.wav")

    def test_waveforms(self):
        synth = WaveSynth("triangle")
        wave = synth.synthesize(440, 1)
        synth.set_waveform("square")
        wave.extend(synth.synthesize(440, 1))
        synth.set_waveform("sawtooth")
        wave.extend(synth.synthesize(440, 1))
        synth.set_waveform("sine")
        wave.extend(synth.synthesize(440, 1))
        wave.tofile("synth_test2.wav")

    def test_sustain(self):
        synth = WaveSynth(sustain=0.8)
        wave = synth.synthesize(440, 1)
        wave.extend(synth.synthesize(440, 1))
        synth.set_sustain(.4)
        wave.extend(synth.synthesize(440, 1))
        synth.set_sustain(.2)
        wave.extend(synth.synthesize(440, 1))
        synth.set_sustain(.1)
        wave.extend(synth.synthesize(440, 1))
        wave.tofile("synth_test3.wav")

    def test_volume(self):
        synth = WaveSynth(volume=25)
        wave = synth.synthesize(440, 1)
        synth.set_volume(50)
        wave.extend(synth.synthesize(440, 1))
        synth.set_volume(75)
        wave.extend(synth.synthesize(440, 1))
        synth.set_volume(100)
        wave.extend(synth.synthesize(440, 1))
        wave.tofile("synth_test4.wav")


if __name__ == "__main__":
    unittest.main()
