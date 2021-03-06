# boolean data type and the comparison & logical operators
# represent true or false / yes or no / on or off using the boolean data type
print("In Programming, you will work with data or information that has two\
 values only, either True or False (like simple 'yes' or 'no' values). Python's\
 data type to represent this is the bool (short for Boolean)")
print('#' * 79)

print("An example would be like below where we assign to a variable\
 'raining_outside' the value True then check the type() for that variable and it\
 should give the boolean type then reassign with the value False and check the\
 type again:")
print('#' * 79)

raining_outside = True
print("raining_outside = True and checking" , "type(raining_outside) gives",\
 type(raining_outside))

raining_outside = False
print("raining_outside = False and checking" , "type(raining_outside) gives",\
 type(raining_outside))

print('#' * 79)

print("Note: Python is case sensitive and thus 'True' and 'False' is not the\
 same as 'true' and 'false'. Our assignment will only work with the capitalized\
 ones (which are Python keywords) and not the lowercase ones")

print("This direct assignment of the boolean type to a variable is not very\
 useful as it is not usually very practical.\n Comes in, comparison operators\
 (comparing values) and logical operators which perform logical operations and\
 give their result as a boolean type")
print('#' * 79)

print("These are the comparison operators (also called relational operators) in\
 Python:")

print("1. greater than operator (>) e.g 50 > 49.9 results in", 50 > 49.9)

print("2. less than operator (<) e.g 20 < 21 results in", 20 < 21)

print("3. greater than or equal to operator (>=) e.g 50 >= 50.0 results in", 50 >= 50.0)

print("4. less than or equal to operator (<=) e.g 50 <= 40 results in", 50 <= 40)

print("5. equal to operator (==) e.g 0.1 == 0.1 results in", 0.1 == 0.1)

print("6. not equal to operator (!=) e.g 0.3 != 0.1+0.1+0.1 results in", 0.3 != 0.1+0.1+0.1)

print('#' * 79)

print("The logical operators (also called boolean operators) in Python are:")
print("They are called boolean operators because they operate on boolean values")

print("1. 'and' operator that evaluates if both sides of the equation are true\
 e.g 20>5 and 30==30 evaluates to", 20>5 and 30==30)

print("2. 'or' operator that evaluates if at least one side of the equation is\
 true e.g 20<5 or 30==30 evaluates to", 20<5 or 30==30)

print("and & or are binary boolean operators because they always take two\
 boolean values (or expressions)")

print("3. 'not' operator that inverses the value of a boolean e.g not True\
 evaluates to", not True)

print("not is a unary boolean operator because it only operates on one boolean\
 value (or expression)")

print("Boolean operators have order of operations like arithmetic operators:\
 NAO (not, and, or)")
