def main():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    x = 6
    def bigsub():
        a = 1
        b = 2
        c = 3
        def sub1():
            a = 1
            d = 2
            a = b + c + x # spot 1
            print("spot 1:", b, c, x)
        def sub2(x):
            b = 1
            e = 2
            def sub3():
                c = 1
                e = 4
                sub1()
                e = a + b + x # spot 2
                print("spot 2:", a, b, x)
            sub3()
            print(e)
            e = a + d + e + x # spot 3
            print("spot 3:", a, d, e ,x)
        sub2(7)
    bigsub()
main()
