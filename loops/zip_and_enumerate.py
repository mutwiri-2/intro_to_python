print("zip and enumerate are useful builtin functions when dealing with lists")

print("zip is a builtin function that returns an iterator which combines multiple\
 iterables into one sequence of tuples. Each tuple contains the elements at that\
 position from all iterables")
print('#' * 99)

print("The zip()function returns an iterator of tuples based on the iterable objects")

print("1. If we do not pass any parameter, zip() returns an empty iterator")

print("2. If a single iterable is passed, zip() returns an iterator of tuples with\
 each tuple having only one element")

print("3. If multiple iterables are passed, zip() returns an iterator of tuples\
 with each tuple having elements from all the iterables from that position")
print('#' * 99)

print("Suppose, two iterables are passed to zip(); one iterable containing three\
 and other containing five elements. Then, the returned iterator will contain\
 three tuples. This is because iterator stops when the shortest iterable is exhausted.")
print('#' * 99)

letters = ['a', 'b', 'c', 'd', 'e', 'f']
numbers = [1, 2, 3, 4, 5, 6]
print("for example if you had two lists as follows:\nletters = ['a', 'b', 'c', 'd', 'e', 'f']\
 and \nnumbers = [1, 2, 3, 4, 5, 6] \nand you called the zip function on them and then passed\
 the result to the list function as follows list(zip(letters, numbers)) you would get:\
 {}".format(list(zip(letters, numbers))))
print('#' * 99)

print("Note that zip returns an iterator object similar to the range() function\
 so you have to call the list function on the result of zip to convert it to a\
 list and see the results")

print("You could also just iterate through using a for loop if you want to print\
 out the result as follows\n {} to get the result below".format("for object in zip(letters, numbers):\
\n\tprint(object[0], object[1])"))
for object in zip(letters, numbers):
    print(object[0], object[1])

print('#' * 99)
print("You can also unpack each tuple (tuple-unpacking or multiple variable assignment)\
 and print the elements out as follows:\n{}".format("for letter, number in zip(letters, numbers):\
\n\tprint(letter, number)"))
for letter, number in zip(letters, numbers):
    print(letter, number)

print('#' * 99)
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
print("The zip function can also be used to unzip a list into tuples")
print("for example, if given the following list;\n manifest = [(\"bananas\", 15),\
 (\"mattresses\", 24), (\"dog kennels\", 42), (\"machine\", 120), (\"cheeses\", 5)]\n,\
 we can use zip to unzip the list into tuples using\n items, weights = zip(*manifest)\n to get the result below")
items, weights = zip(*manifest)
print(items, weights)

print('#' * 79)

print("enumerate() is a built-in function that returns an iterator of tuples\
 containing indices and values of a list")
print('#' * 99)

print("The enumerate() method adds counter to an iterable and returns it (the enumerate object).")
print("The syntax of enumerate() is:\n\tenumerate(iterable, start=0)")
print('#' * 99)

print("The enumerate() method takes two parameters:\n1. iterable - a sequence, an iterator,\
 or objects that supports iteration\n2. start (optional) - enumerate() starts counting from\
 this number. If start is omitted, 0 is taken as start")

print("The enumerate() method adds counter to an iterable and returns it. The\
 returned object is an enumerate object.")

print("On each iteration of the loop, enumerate() will return two values: the\
 index of the item in the list, and the item itself in the list")

print("The enumerate() function is useful if you need both an item and the item’s index in the loop’s block")
print('#' * 99)

print("You can convert enumerate objects to list, tuples or dicts using list(), tuple() and dict() methods respectively.")
print('#' * 99)

teams = ['Liverpool', 'Mancity', 'Leicester', 'Chelsea']
print("for example if you had a list like teams = ['Liverpool', 'Mancity', 'Leicester',\
 'Chelsea'] and you wanted to get a list of tuples of team and it's index, you\
 could do the following; print(list(enumerate(teams))) to get the following output:\
\n{}".format(list(enumerate(teams))))
print('#' * 99)

print("You could also print out the values of a list with their indices using\
 enumerate as follows:\n for i, team in enumerate(teams):\n\tprint(i, team)\nto get the following output:")
for i, team in enumerate(teams):
    print(i, team)

print("You will often use enumerate() when you need the indices and values of a list in a loop")

print('#' * 99)
# quiz
# Use zip to write a for loop that creates a string specifying the label and coordinates
# of each point and appends it to the list points. Each string should be formatted as
# label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for object in zip(labels,x_coord,y_coord,z_coord):
    object = object[0] + ': ' + str(object[1]) + ', ' + str(object[2]) + ', ' + str(object[3])
    points.append(object)
for point in points:
    print(point)

print('#' * 99)
# more succint solution
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))
for point in points:
    print(point)

print('#' * 99)
# Use zip to create a dictionary cast that uses names as keys and heights as values.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

print('#' * 99)
# Quiz: Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)

print('#' * 99)
# Quiz: Transpose with Zip
# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)
# transpose data from a 3-by-4-matrix to a 4-by-3-matrix
print(tuple(zip(*data_transpose)))

print('#' * 99)
# Quiz: Enumerate
# Use enumerate to modify the cast list so that each element contains the name
# followed by the character's corresponding height. For example, the first element
# of cast should change from "Barney Stinson" to "Barney Stinson 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for index, name in enumerate(cast):
    cast[index] = "{} {}".format(name,heights[index])
print(cast)