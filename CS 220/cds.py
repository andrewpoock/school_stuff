# cds.py
# Andrew Poock

class MusicCD:

    def __init__(self, artist, album):
        self.artist = artist
        self.album = album
        self.tracks = []
        self.link = None

    def addtrack(self, title, duration):
        self.tracks.append((title, duration))

    def duration(self):
        duration, total = 0, 0
        for i in range(len(self.tracks)):
            title, duration = self.tracks[i]
            total += duration
        return total

    def info(self):
        info = "Album: " + str(self.album) + "\nArtist: " + str(self.artist) + "\nDuration:" + str(self.duration())
        return info

class CDCollection:

    def __init__(self):
        self._first = None

    def addCD(self, cd):
        cd.link = self._first
        self._first = cd

    def printCDs(self):
        currCD = self._first
        while currCD is not None:
            print(currCD.album)
            currCD = currCD.link

def main():
    print("Testing")
    c1 = MusicCD("Pink Floyd", "The Final Cut")
    assert c1.artist == "Pink Floyd"
    assert c1.album == "The Final Cut"
    assert c1.tracks == []
    c2 = MusicCD("Taylor Swift", "1989")
    assert c2.artist == "Taylor Swift"
    assert c2.album == "1989"
    assert c2.tracks == []
    c3 = MusicCD("The Beatles", "1")
    assert c3.artist == "The Beatles"
    assert c3.album == "1"
    assert c3.tracks == []

    c1.addtrack("The Post War Dream", 182)
    c1.addtrack("Your Possible Pasts", 262)
    assert c1.tracks == [("The Post War Dream", 182),("Your Possible Pasts", 262)]
    c2.addtrack("Blank Space", 232)
    c2.addtrack("Shake It Off", 219)
    assert c2.tracks == [("Blank Space", 232),("Shake It Off", 219)]
    c3.addtrack("Yesterday", 126)
    c3.addtrack("Elanor Rigby", 128)
    assert c3.tracks == [("Yesterday", 126),("Elanor Rigby", 128)]

    assert c1.duration() == 444
    assert c2.duration() == 451
    assert c3.duration() == 254

    # print(c1.info())
    # assert c1.info() == "Album: The Final Cut\nArtist: Pink Floyd\nDuration: 444"

    collection = c1
    c1.link = c2
    c2.link = c3
    assert collection.album == "The Final Cut"
    assert collection.link.album == "1989"
    assert collection.link.link.album == "1"

    coll2 = CDCollection()
    coll2.addCD(c1)
    coll2.addCD(c2)
    coll2.addCD(c3)
    coll2.printCDs() # each cd is added to the front, so prints in opposite order
    
    print("OK")

main()

