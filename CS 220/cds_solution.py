# cds.py
#  by: CS 220 Class

class MusicCD:

    def __init__(self, artist, album):
        self.artist = artist
        self.album = album
        self.tracks = []
        self.link = None

    def addtrack(self, title, duration):
        self.tracks.append((title, duration))

    def duration(self):
        total = 0
        for (title, dur) in self.tracks:
            total = total + dur
        return total

    def info(self):
        return f"Album: {self.album}\nArtist: {self.artist}\nDuration: {self.duration()}"


class CDCollection:

    def __init__(self):
        self._first = None
        self._last = None

    def addCD(self, cd):
        if self._last is None:
            self._first = cd
        else:
            self._last.link = cd
        self._last = cd

    def printCDs(self):
        currCD = self._first
        while currCD is not None:
            print(currCD.info())
            print()
            currCD = currCD.link

    def __iter__(self):
        currCD = self._first
        while currCD is not None:
            yield currCD
            currCD = currCD.link

           
def main():
    print("Testing")
    c1 = MusicCD("Pink Floyd", "The Final Cut")
    assert c1.artist == "Pink Floyd"
    assert c1.album == "The Final Cut"
    assert c1.tracks == []

    c1.addtrack("The Post War Dream", 182)
    c1.addtrack("Your Possible Pasts", 262)

    c2 = MusicCD("Sleepy Bones Allison", "Too Young to Play the Blues")
    c3 = MusicCD("Ritterchor", "Arrrrr, Me Mateys!")

    coll = CDCollection()
    coll.addCD(c1)
    coll.addCD(c2)
    coll.addCD(c3)
    coll.printCDs()

    for cd in coll:
        print(cd.info())
        print()

    
    print("OK")

if __name__ == "__main__":
    main()
    
