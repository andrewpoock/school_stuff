# dietest.py
# Andrew Poock

from msdie import MSDie

def main():
    d1 = MSDie(6)
    d2 = MSDie(10)
    
    for i in range(10):
        d1.roll()
        d2.roll()
        print(d1.getValue())
        print(d2.getValue())
        d1.flip()
        d2.flip()
        print(d1.getValue())
        print(d2.getValue())

main()
