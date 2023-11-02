# pizza.py
# compute cost/sq inch of pizza
# Andrew Poock

from math import pi

def area(radius):
    area = pi * radius * radius
    return area

def cost_per_area(diameter, cost):
    radius = diameter/2
    return cost/area(radius)

def main():
    print("This program returns the cost per square inch of a pizza")
    print("Enter information for pizza 1: ")
    size1 = int(input("\tEnter the diameter of the pizza: "))
    cost1 = float(input("\tEnter the price of the pizza: "))
    print("\nEnter information for pizza 2: ")
    size2 = int(input("\tEnter the diameter of the pizza: "))
    cost2 = float(input("\tEnter the price of the pizza: "))
    
    print("The cost per area of Pizza 1 is:", cost_per_area(size1, cost1))
    print("The cost per area of Pizza 2 is:", cost_per_area(size2, cost2))
    
    if cost_per_area(size1, cost1) < cost_per_area(size2, cost2):
        print("Pizza 1 is the better value")
    elif cost_per_area(size1, cost1) > cost_per_area(size2, cost2):
        print("Pizza 2 is the better value")
    else:
        print("Both Pizzas are the same value")

main()
