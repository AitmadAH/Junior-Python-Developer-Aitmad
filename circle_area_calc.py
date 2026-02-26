print("Circle Area Calculator by Junior Python Developer AITMAD")
import math

# Logical side of code
def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    area = math.pi * (radius ** 2)
    return area

# Below is the part to get user input about circle
def main():
    try:
        radius_input = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius_input)
        print(f"The area of the circle with radius {radius_input} is: {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

# Run this code here to execute       
main()
