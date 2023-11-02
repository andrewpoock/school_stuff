# test_synth.py

import unittest
from stringsynth import StringSynth
from keyboard import Keyboard
from soundwave import SoundWave


class TestSynth(unittest.TestCase):

    def test_default(self):
        synth = StringSynth()
        test1 = synth.synthesize(220, .5)
        test1.extend(synth.synthesize(440, 2))
        test1.tofile("str_synth_test1.wav")
        
    def test_gain(self):
        synth = StringSynth(loopgain=.96)
        wave = synth.synthesize(440, .8)
        wave.extend(synth.synthesize(440, 1))
        synth.set_loopgain(.97)
        wave.extend(synth.synthesize(440, 1))
        synth.set_loopgain(.98)
        wave.extend(synth.synthesize(440, 1))
        synth.set_loopgain(.99)
        wave.extend(synth.synthesize(440, 1))
        wave.tofile("str_synth_test2.wav")

    def test_volume(self):
        synth = StringSynth(volume=25)
        wave = synth.synthesize(440, 1)
        synth.set_volume(50)
        wave.extend(synth.synthesize(440, 1))
        synth.set_volume(75)
        wave.extend(synth.synthesize(440, 1))
        synth.set_volume(100)
        wave.extend(synth.synthesize(440, 1))
        wave.tofile("str_synth_test3.wav")

    def test_play_chord(self):
        kb = Keyboard(StringSynth())
        wave = SoundWave()
        for note in ("C3 D3 E3 F3 G3 A3 B3 C4".split()):
            wave.extend(kb.play_chord(note, [0, 4, 7], .5))
        wave.tofile("str_synth_test4.wav")

    
if __name__ == "__main__":
    unittest.main()
