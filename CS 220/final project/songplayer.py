# songplayer.py
# Andrew Poock

import tonelib
from soundwave import SoundWave
from keyboard import Keyboard
from songreader import SongReader
from stringsynth import StringSynth



class SongPlayer:

    """A SongPlayer provides a convenient interface building an audio file
    from a song description file.

    Each part of a song file can be independently rendered any number
    of times using any synthesizer to provide the "voice" of the
    instrument playing the part. The individual part renderings are
    summed to create a combined audio result that can be played and/or
    written to a wav file.

    """

    def __init__(self, songfile):
        """use SongReader to initialize from songfile"""
        self._data = SongReader(songfile)
        self._kb = Keyboard(StringSynth())
        self._sw = SoundWave()
        self.set_tempo(int(self._data.info['TEMPO']))

    def set_tempo(self, bpm):
        """set tempo to bpm beats per minute
      
        note: initial tempo is set from the TEMPO value in the song
        file

        """
        self._tempo = bpm

    def render_part(self, partnum, synth):
        """use synth to render the given part and 'merge' it into the audio
        note: the current setting of tempo is used to compute note durations
        """
        part = self._data.parts[partnum]
    
        sw = SoundWave()
        for note in part:
            pitch = note[0]
            beat = float(note[1])
            keyn = self._kb.keynum(pitch)
            freq = self._kb.keyfrequency(keyn)
            duration = (beat / self._tempo) * 60
            sw.extend(synth.synthesize(freq, duration))
        self._sw += sw

    def play_audio(self, time=None):
        """play the current audio
        time is number of seconds of audio to play (None means entire audio)
        Note: a normalized version of the audio is played, but the audio in
              the player retains its raw (unnormalized) form.
        """
        norm = SoundWave(self._sw.samples)
        if time is not None:
            norm = SoundWave(self._sw.samples[:time*tonelib.SAMPLERATE])
        norm.normalize()
        norm.play()

    def writewavfile(self, fname, prepad=1, postpad=0):
        """ save current audio to a file
        prepad is number of seconds of silence to add at the start
        postpad is number of seconds of silence to add at the end

        Note: the audio file is normalized, but the acual audio in 
        the player remains in its raw (unnormalized) form.
        """
        pre = StringSynth()
        wave = pre.synthesize(tonelib.SAMPLERATE, prepad)
        post = StringSynth()
        post = post.synthesize(tonelib.SAMPLERATE, postpad)
        norm = SoundWave(self._sw.samples)
        norm.normalize()
        wave.extend(norm)
        wave.extend(post)
        wave.tofile(fname)

def test():
    # you may want to put simple test code here during development
    pass
    
test()
