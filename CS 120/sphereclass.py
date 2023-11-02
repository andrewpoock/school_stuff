# sphereclass.py
# Andrew Poock

class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        self.volume = (4/3)*3.14*(self.radius**3)
        return self.volume

    def surfaceArea(self):
        self.surfaceArea = 4*3.14*(self.radius**2)
        return self.surfaceArea

        
def main():
    r = float(input("What is the radius of the sphere? "))
    s = Sphere(r)
    print("The volume of the sphere is:", s.volume(), "cubic units")
    print("The surface area is:", s.surfaceArea(), "square units")

main()
