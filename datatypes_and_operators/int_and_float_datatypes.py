# how to represent numerical data using the int and float data types
print("Every object you encounter in Python has a data type. Data types are a\
 way to represent the various types (categories) of information we will be\
 dealing with in our programs.")
print("Data types are also useful in the sense that they define what kind of\
 functions and operations work on a given object and how these operations and\
 functions work")
print('#' * 79)

print("For numerical data in our programs, we can represent them using two data\
 types -- int (short for integer) and float (short for floating point numbers).")
print("int is a data type for real whole numbers - either positive or negative.")
print("float is a data type for real numbers (positive or negative) that use a\
 decimal point to allow numbers with fractional values.")
print('#' * 79)

print("A real number is a number that is not imaginary. Imaginary numbers are\
 like the square root of -1, infinite e.t.c")
print("A real number is a point on an infinitely long line called the number line\
 or the real line")
print('#' * 79)

print("We can use the built-in 'type()' function to check the data type of any\
 object in python")
print("type(0) is", type(0))
print("type(0.9) is", type(0.9))
print("type(1) is", type(1))
print("type(1.) is", type(1.))
print("type(10) is", type(10))
print("type(10.123) is", type(10.123))
print("type(109876127) is", type(109876127))
print("type(-234) is", type(-234))
print("type(-677.78) is", type(-677.78))
print('#' * 79)

print("You can convert one numerical data type to the other i.e from float to int\
 and int to float using the 'int()' and 'float()' built-in methods - This creates\
 new objects of the new type like below:")
print('#' * 79)

print("int(5.7) will convert 5.7 which is a float to the integer", int(5.7))
print("Note that the int() function cuts off the part after the decimal and does\
 not round it off")
print('#' * 79)

print("float(150) will convert the integer 150 to a float", float(150))
print("Note the float() function adds a .0 (a decimal point zero) to the end of\
 the integer to make it a float")
print('#' * 79)

print("'int operator float' will always produce a float as the answer")
print("type(25 * 5.0)", type(25 * 5.0))
print("type(25 + 5.0)", type(25 + 5.0))
print("type(25 - 5.0)", type(25 - 5.0))
print("type(25 % 5.0)", type(25 % 5.0))
print("type(25 // 5.0)", type(25 // 5.0))
print("int division int will also produce float as the answer - because '/' is\
 the arithmetic operator for float division")
print("type(45/9)", type(45/9))
print('#' * 79)

print("'int operator int' will always produce an int as the answer except for\
 the '/' (float division operator")
print("type(25 * 5)", type(25 * 5))
print("type(25 + 5)", type(25 + 5))
print("type(25 - 5)", type(25 - 5))
print("type(25 % 3)", type(25 % 3))
print("type(25 // 5)", type(25 // 5))
print('#' * 99)

print("When programming, you will have to use your own judgement to pick your\
 numerical data types in a way that works for your program but remember use 'int'\
 for values that are whole numbers without decimal places (fractional values) and\
 'float' for values with fractional values i.e if what you will be working with\
 is not neccessarily a whole number")
print('#' * 99)

print("Floats can represent an enormous range of numbers (the fractional value\
 part after the decimal) hence floating point numbers are actually approximations\
 of the numbers they are supposed to represent")
print("Due to the fact above, there are some small margins of error which are\
 most times insignificant in our programs for example:")
print("0.1 + 0.1 + 0.1 == 0.3 will evaluate to", 0.1+0.1+0.1==0.3)
print("The above evaluates to False because 0.1 + 0.1 + 0.1 results in {} instead\
 of the expected 0.3".format(0.1+0.1+0.1))