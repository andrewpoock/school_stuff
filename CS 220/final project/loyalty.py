# loyalty.py
# Andrew Poock

from songplayer import SongPlayer
from stringsynth import StringSynth


def main():

    sp = SongPlayer('./loyalty.sng')
    sp.render_part(0, StringSynth())
    sp.render_part(1, StringSynth())
    sp.render_part(2, StringSynth())
    sp.render_part(3, StringSynth())
    sp.writewavfile("loyalty4.wav")

main()
