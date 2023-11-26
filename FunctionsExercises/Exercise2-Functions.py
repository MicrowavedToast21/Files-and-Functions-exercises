import math


def calculate_area_degrees(a, b, angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    area = 0.5 * a * b * math.sin(angle_in_radians)

    return area

while True:
    try:
      a = float(input("Enter side a of the triangle: "))
      b = float(input("Enter side b of the triangle: "))
      angle_degrees = float(input("Enter angle of the triangle: "))
      break
    except ValueError:
        print("Invalid input.Please enter numbers")

area = calculate_area_degrees(a, b, angle_degrees)
print("The area is :", area, "m2")