# test_keyboard.py
# Andrew Poock

import unittest
from keyboard import Keyboard
from wavesynth import WaveSynth
from soundwave import SoundWave


class Test_Keyboard(unittest.TestCase):

    def setUp(self):
        self.kb = Keyboard(WaveSynth("sawtooth", sustain=.3))

    def test_keyfrequency(self):
        self.assertAlmostEqual(self.kb.keyfrequency(49), 440.0)
        self.assertAlmostEqual(self.kb.keyfrequency(1), 27.500)

    def test_keynum(self):
        self.assertEqual(self.kb.keynum("B0"), 3)
        self.assertEqual(self.kb.keynum("A#1"), 14)
        self.assertEqual(self.kb.keynum("Bb1"), 14)
        self.assertEqual(self.kb.keynum("A2"), 25)
        self.assertEqual(self.kb.keynum("G#0"), 0)
        self.assertEqual(self.kb.keynum("Ab0"), 0)
        self.assertEqual(self.kb.keynum("G1"), 11)
        self.assertEqual(self.kb.keynum("F#1"), 10)
        self.assertEqual(self.kb.keynum("Gb1"), 10)
        self.assertEqual(self.kb.keynum("F1"), 9)
        self.assertEqual(self.kb.keynum("E1"), 8)
        self.assertEqual(self.kb.keynum("D#1"), 7)
        self.assertEqual(self.kb.keynum("Eb1"), 7)
        self.assertEqual(self.kb.keynum("D1"), 6)
        self.assertEqual(self.kb.keynum("C#1"), 5)
        self.assertEqual(self.kb.keynum("Db1"), 5)
        self.assertEqual(self.kb.keynum("C1"), 4)

    def test_play_key(self):
        wave = SoundWave()
        for k in [40, 42, 44, 45, 47, 49, 51, 52]:
            wave.extend(self.kb.play_key(k, .5))
        wave.tofile("kb_test1.wav")

    def test_play_keys(self):
        wave = self.kb.play_keys([40, 44, 47], 2)
        wave.tofile("kb_test2.wav")

    def test_play_note(self):
        wave = SoundWave()
        for note in ("C3 D3 E3 F3 G3 A3 B3 C4".split()):
            wave.extend(self.kb.play_note(note, .5))
        wave.tofile("kb_test3.wav")

    def test_play_notes(self):
        wave = self.kb.play_notes(["C3", "E3", "G3"], 2)
        wave.tofile("kb_test4.wav")

    def test_play_chord(self):
        wave = SoundWave()
        for note in ("C3 D3 E3 F3 G3 A3 B3 C4".split()):
            wave.extend(self.kb.play_chord(note, [0, 4, 7], .5))
        wave.tofile("kb_test5.wav")

    def test_tuning(self):
        wave = self.kb.play_note("A4", .5)
        wave.extend(self.kb.play_key(49, .5))
        self.kb.tuning = 420
        wave.extend(self.kb.play_note("A4", .5))
        wave.extend(self.kb.play_key(49, .5))
        wave.tofile("kb_test6.wav")
        
        
        
        
        

if __name__ == "__main__":
    unittest.main()
