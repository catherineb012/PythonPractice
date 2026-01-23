#16 - Calculate the area of a rectangle (part 2)

print("16 - Calculate the area of a rectangle (part 2)")
print()

print("RECTANGLE 1")
print()

length_1 = int(input("Please enter the length of rectangle 1: "))
width_1 = int(input("Please enter the width of rectangle 1: "))
area_1 = length_1 * width_1


print()
print("RECTANGLE 2")
print()

length_2 = int(input("Please enter the length of rectangle 2: "))
width_2 = int(input("Please enter the width of rectangle 2: "))
area_2 = length_2 * width_2

print()

if area_1 > area_2:
    print("Rectangle 1 has the largest area with an area of ", area_1)

else:
    print("Rectangle 2 has the largest area with an area of ", area_2)
