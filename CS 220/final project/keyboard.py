# keyboard.py
#   Keyboard class provides functionality for mapping "keys" on a musical keyboard
#   to specific note frequencies for a sound synthesizer


from soundwave import SoundWave


class Keyboard:
    # mapping of pitches to key numbers in octave 0
    _BASE_KEYNUMS = {"B": 3,
                     "A#": 2, "Bb": 2,
                     "A": 1,
                     "G#": 0, "Ab": 0,
                     "G": -1,
                     "F#": -2, "Gb": -2,
                     "F": -3,
                     "E": -4,
                     "D#": -5, "Eb": -5,
                     "D": -6,
                     "C#": -7, "Db": -7,
                     "C": -8}

    def __init__(self, synth, tuning=440):
        self.tuning = tuning
        self.synth = synth

    def keyfrequency(self, n):
        """ frequency of key number n. 
        keyfrequency(49) --> 440 (in standard tuning)
        """
        
        return self.tuning*2**((n-49)/12)

    def keynum(self, pitch):
        """key number corresponding to scientific pitch
        e.g. keynum("A4") --> 49

        """
        octave = int(pitch[-1])
        notename = pitch[:-1]
        return self._BASE_KEYNUMS[notename] + 12 * octave

    def play_key(self, keynum, duration):
        """ play key designated by keynum for duration
        pre: keynum is an int from 1 to 88 and duration is time in seconds
        post: returns SoundWave of the give keynum and duration
        """
        freq = self.keyfrequency(keynum)
        return self.synth.synthesize(freq, duration)

    def play_keys(self, keys, duration):
        """  play keys simultaneously
        pre: keys is a list of key numbers, duration is time in seconds
        post: returns a SoundWave of keys played simulatneously 
        """
        wave = SoundWave()
        for key in keys:
            wave += self.play_key(key, duration)
        return wave

    def play_note(self, pitch, duration):
        """ play note corresponding to scientific pitch
        pre: pitch is a scientific pitch string, duration is time in seconds
        post: returns SoundWave of key correspoinding the scientific pitch
        """
        return self.play_key(self.keynum(pitch), duration)

    def play_notes(self, notes, duration):
        """ play notes simultaneously 
        pre: notes is a list of pitch strings and duration is in seconds
        pre: returns a SoundWave of the notes being played simulatneously
        """
        wave = SoundWave()
        for note in notes:
            wave = wave + self.play_note(note, duration)
        return wave

    def play_chord(self, basepitch, intervals, duration):
        """ play notes in chord
        pre: basepitch is a pitch string and intervals is a list of ints >= 0
        post: returns a SoundWave of simultaneous notes consisting specified by
              the keynum of basepitch + some i in intervals (i.e. a chord).
        Note: intervals are half-steps, so a c-major chord starting at middle
              C is play_chord("C4", [0, 4, 7]).
        """
       
        key = self.keynum(basepitch)
        keys = [key+i for i in intervals]
        return self.play_keys(keys, duration)
