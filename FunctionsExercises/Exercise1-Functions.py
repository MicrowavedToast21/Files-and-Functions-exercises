import math
def area_right_angled_triangle(base, height):
    return(base * height) / 2

while True:
    try:
      base = float(input("Enter the base of the triangle: "))
      height = float(input("Enter the height of the triangle: "))
      break
    except ValueError:
        print("Invalid input, please enter an actual number: ")

area = area_right_angled_triangle(base, height)
print(f"The area of the triangle is: {area} m2")