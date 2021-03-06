# quickly get valid attributes of an object in Python using dir() and their
# definitions using help() built-in functions
print("The dir() built-in fuction returns information about an object. It can be\
 useful when you have an object and want to quickly find out what you can do with\
 it. It returns some of the attributes and methods of that object (Remember \
 every object you encounter in Python has a type and this is what will determine\
 the attributes and methods returned)")
print('#' * 79)

num = 5
print("Say you have an integer like 5 assigned to the variable num, calling dir()\
 on num will result in the following attributes:")

for index, attribute in enumerate(dir(num)):
    print(index, attribute)

print('#' * 79)

print("Calling dir() on a string like dir('s') would result in the following:")

for index, attrib in enumerate(dir('s')):
    print(index, attrib)

print('#' * 79)

print("The information printed is not very useful so we have another built-in\
 function called help() which gives a short description of any of the attributes\
 returned by dir(). You call help() on the attribute using the dot notation e.g\
 help(num.__add__) or help('s'.rfind)")
print('#' * 79)
# print(help(num.__add__))

print(r'''
The python help function is used to display the documentation of modules, functions, classes, keywords etc.
The help function has the following syntax:

help([object]) e.g help(print)
If the help function is passed without an argument, then the interactive help utility starts up on the console.

''')

print('#' * 79)
