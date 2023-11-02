# keyfns.py
# Andrew Poock

# create a dictionary mapping of pitches to keys in octave 0

_BASE_KEYNUMS = {'C':-8,'C#':-7,'Db':-7,'D':-6,'D#':-5,'Eb':-5,'E':-4,'F':-3,'F#':-2,'Gb':-2,'G':-1,'G#':0,'Ab':0,'A':1,'A#':2,'Bb':2,'B':3}  # fill in this dictionary based on wikipedia page

def keyfrequency(n, tuning=440):
    """ Returns frequency of key number n.
    tuning is the the frequency desired for concert A (A4)
    """
    freq = (2**((n-49)/12))*440
    return freq

def keynum(pitch):
    """ Returns piano key number corresponding to a scientific pitch
    e.g. keynum("A4") --> 49 """
    
    # algorithm:
    #    break pitch into octave and base_pitch
    #    get base_key from dictionary using base_pitch
    #    key is base_key + 12 * octave

    base_pitch, octave = pitch.split()
    base_key = _BASE_KEYNUMS[base_pitch]
    key = base_key+12*int(octave)
    return key
    
    

    


