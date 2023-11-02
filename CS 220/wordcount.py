# wordcount.py
#   Dictionary and iterator example

from string import punctuation

def wordgen(fname):
    with open(fname) as infile:
        for line in infile:
            line = line.replace("-", " ")
            for word in line.split():
                yield word.strip(punctuation).lower() 

def get_wordcounts(fname):
    counts = {}
    for word in wordgen(fname):
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts
