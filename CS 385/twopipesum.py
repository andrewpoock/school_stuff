# twopipesum.py
# Andrew Poock

import os, random

def main():
    r, w = os.pipe()
    child1 = os.fork()
    if child1 == 0:
        os.close(r)
        w = os.fdopen(w, "w")
        random.seed(os.getpid()*13)
        b = str(random.randint(0, 100))
        print(b, flush=True, file=w)
    else:
        os.close(w)
        r2, w2 = os.pipe()
        child2 = os.fork()
        if child2 == 0:
            os.close(r)
            os.close(r2)
            w2 = os.fdopen(w2, "w")
            random.seed(os.getpid()*13)
            b = str(random.randint(0, 100))
            print(b, flush=True, file=w2)
        else:
            os.close(w2)
            os.wait()
            os.wait()
            r = os.fdopen(r)
            r2 = os.fdopen(r2)
            num1 = int(r.readline()[:-1])
            num2 = int(r2.readline()[:-1])
            print(f"[{os.getpid()}]: spawning children")
            print(f"[{child1}]: picks {num1}")
            print(f"[{os.getpid()}]: reaping numbers")
            print(f"[{child2}]: picks {num2}")
            print(f"[{os.getpid()}]: sum is: {num1 + num2}")
            

main()
