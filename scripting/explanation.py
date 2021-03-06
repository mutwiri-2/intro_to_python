print("A script or scripting language is a computer language with a series of\
 commands within a file that is capable of being executed without being compiled\
 but can be compiled if need be")

print("A program becomes more intuitive by interacting with user input")
print('#' * 99)

print("The built-in function input() is used to get raw input data from the user.\
 It has an optional string argument that allows us to use as a prompt to the user")

print("The input() function takes in whatever the user types and stores it as a string")

print("for example\n name = input('Enter your name:')then we can\n print(name)")
name = input('Enter your name: ')
print("Hey", name)
print('#' * 99)

print("input() interprets the raw input data as a string so we need to wrap it\
 with int() or float() if we need to use it as a number")
print('#' * 99)
print("for example, if we wanted to print a string the number of times a user wants\
     we can prompt them to enter the number of times they want it printed as\
     follows:\nnum = int(input('Enter number of times you want the name printed'))\
    \nIf however the user enters a float, the code will generate an error,\
     ValueError because the int() function does not accept a literal with a float\
     value. We can however resolve this by using float to wrap the input method")
print('#' * 99)

print("But a float value would generate an error if we tried multiplying a string\
 by it because a string can only be multiplied by a whole number. To remedy this,\
 we can catch the input exception by using float then use int to catch the string\
 repetition by multiplication as follows:\nnum = int(float(input('Enter number of\
 times you want the name printed: ')))")

num = int(float(input('Enter number of times you want the name printed: ')))
print('mutwiri-2 ' * num)
print('#' * 99)
print("eval() function is a built-in function that evaluates a string as a line\
 of Python e.g\n print(eval(input('Enter an expression to evaluate: ')))")
print(eval(input('Enter an expression to evaluate: ')))
print('#' * 99)
print('eval() can only run simple python expressions that are not complex i.e\
 single lines of code without logic, conditional statements or control flow')
print('#' * 99)
print("if we want to run more complex code e.g conditional statements or loops,\
 we can use the built-in exec() function e.g\nexec(input('Enter a block of code: '))")
print("\nBe careful while using exec() !!!!!".upper())
print(r'''
Consider a situation, you are using a Unix system (macOS, Linux etc) and you have
 imported os module. The os module provides a portable way to use operating system
 functionalities like: read or write a file.

If you allow users to input a value using exec(input()), the user may issue
 commands to change file or even delete all the files using command os.system('rm -rf *')''')