# songreader.py
#   A class to process simple song files


class SongReader:
    """Extract information from a songfile:

    public attributes:

        info: dictionary of the meta information at the top of the song file
        parts:  list of the "parts" from the song file

        each part is a list of pairs of the form (note:str, beats:float)
              note is a scientific pitch and 
              beats is the number of beats the that the note is held.
    """       

    def __init__(self, songfile):
        """ read data from songfile
        pre: songfile is the name of a file containing song information
        post: the extracted information is in info and parts
        """
        self._read_songfile(songfile)

    def _read_songfile(self, songfile):
        ''' read song file and set self.title, self.tempo, self.parts '''
        with open(songfile, 'r') as infile:
            self._read_info(infile)
            self._read_parts(infile)

    def _read_info(self, infile):
        self.info = {}
        while True:
            line = infile.readline().strip()
            if line == "":
                break
            label, value = line.split(":")
            self.info[label] = value

    def _read_parts(self, infile):
        self.parts = []
        part = []
        for line in infile:
            line = line.strip()
            if line == "":
                self.parts.append(part)
                part = []
            for notespec in line.split():
                if notespec != "|":
                    if "-" not in notespec:
                        notespec += "-1"
                    pitchinfo, beats = notespec.split("-")
                    part.append((self._parse_pitch(pitchinfo), float(beats)))
        if part != []:
            self.parts.append(part)

    def _parse_pitch(self, abc):
        octave = 4
        i = 0
        while abc[i] in ",":
            octave -= 1
            i += 1
        while abc[i] in "'":
            octave += 1
            i += 1
        return abc[i:]+str(octave)

