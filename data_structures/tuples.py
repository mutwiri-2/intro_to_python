# store related pieces of info using the tple data type (data structure)

print("Tuples are a data type for immutable ordered sequence of objects")

print("They are immutable meaning a tuple cannot be modified once it has been\
 created- you cannot remove or add or sort or reverse or shuffle the order of elements in it")

print("They are ordered meaning each object has an index to indicate it's position\
 in the data structure and that can be used to access it")
print('#' * 79)

print("Tuples can be created or defined in the following ways:")

dimensions = (34, 56, 90.7)
print("1. Using parantheses to delimit an ordered sequence of elements e.g\
 dimensions = (34, 56, 90.7) creates a variable dimensions and assigns to it a\
 tuple of three objects (numbers in this case). Printing out dimensions and\
 checking the type will result in: {}, {} ".format(dimensions, type(dimensions)))
print('#' * 79)

print("If your tuple has just one object, include a trailing comma (,) so that\
 Python knows it is a tuple. Otherwise, Python will assume you have just wrapped\
 a regular value in brackets. e.g type(('hello')) will result in {} while\
 type(('hello',)) will result in {}".format(type(('hello')),type(('hello',))))
print('#' * 79)

dimensions = 34, 56, 90.7
print("2. Optionally, you can ommit the parantheses used to delimit an ordered\
 sequence of elements e.g dimensions = 34, 56, 90.7 creates a variable dimensions\
 and assigns to it a tuple of three objects (numbers in this case). Printing out\
 dimensions and checking the type will result in: {}, {} ".format(dimensions, type(dimensions)))
print('#' * 79)

print("3. You can use the tuple() method to create a tuple e.g if you have list = [1,2,3]\
 you can create a tuple like this: my_tuple = tuple(list)")
print('#' * 79)

print("Tuples are like lists in that they are ordered, can be sliced and indexed,\
 with the only difference being that they are immutable unlike lists")

print("So why have tuples?? They are mostly used to store a bunch of values that\
 are so closely related that they are almost always used together e.g dimensions\
 like length, width and height or co-ordinates like latitude, longitude")
print('#' * 79)

print("Tuples can be used to assign multiple variables at once in a process known\
 as TUPLE UNPACKING e.g\n length,width,height = dimensions\n without having to\
 access individual elements using their index like you would this way;\
\nlength,width,height = dimensions[0],dimensions[1],dimensions[2]\
 \nThis is useful when you want to assign multiple variables in a compact way,\
 but if you don't need to use the tuple, just use multiple assignment directly\
 like so;\n length, width, height = 34, 56, 90.7")
print('#' * 79)