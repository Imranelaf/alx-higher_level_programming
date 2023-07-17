from models.rectangle import Rectangle
from models.square import Square

# Test save_to_file and load_from_file methods for Rectangle
r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]

Rectangle.save_to_file(list_rectangles_input)

list_rectangles_output = Rectangle.load_from_file()

for rect in list_rectangles_input:
    print("[{}] {}".format(id(rect), rect))

print("---")

for rect in list_rectangles_output:
    print("[{}] {}".format(id(rect), rect))

print("---")
print("---")

# Test save_to_file and load_from_file methods for Square
s1 = Square(5)
s2 = Square(7, 9, 1)
list_squares_input = [s1, s2]

Square.save_to_file(list_squares_input)

list_squares_output = Square.load_from_file()

for square in list_squares_input:
    print("[{}] {}".format(id(square), square))

print("---")

for square in list_squares_output:
    print("[{}] {}".format(id(square), square))

print("---")
print("---")

# Test save_to_file_csv and load_from_file_csv methods for Rectangle
r3 = Rectangle(4, 3, 1, 2)
r4 = Rectangle(5, 5)
list_rectangles_input_csv = [r3, r4]

Rectangle.save_to_file_csv(list_rectangles_input_csv)

list_rectangles_output_csv = Rectangle.load_from_file_csv()

for rect in list_rectangles_input_csv:
    print("[{}] {}".format(id(rect), rect))

print("---")

for rect in list_rectangles_output_csv:
    print("[{}] {}".format(id(rect), rect))

print("---")
print("---")

# Test save_to_file_csv and load_from_file_csv methods for Square
s3 = Square(3)
s4 = Square(6, 4, 5)
list_squares_input_csv = [s3, s4]

Square.save_to_file_csv(list_squares_input_csv)

list_squares_output_csv = Square.load_from_file_csv()

for square in list_squares_input_csv:
    print("[{}] {}".format(id(square), square))

print("---")

for square in list_squares_output_csv:
    print("[{}] {}".format(id(square), square))

print("---")
print("---")

# Test draw method
list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

Base.draw(list_rectangles, list_squares)
