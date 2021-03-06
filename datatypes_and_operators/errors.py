# errors in Python
print("Errors are inevitable in programming. Error messages are just a way for\
 the computer to let you know that it does not quite understand what you have\
 instructed it to do. THIS DOES NOT IN ANY WAY MAKE YOU A BAD PROGRAMMER.\
 Instead, you should take this as a learning opportunity to become a better\
 programmer.")
print('#' * 79)

print("Understand common errors you may get and what to do about them.")
print("There are two types to look out for \n\t {} \n\t {}".format("Exceptions-\
 A problem that occurs when the program is running.", "Syntax / Parsing errors-\
 A problem detected when Python checks the code before it runs it."))
print('#' * 79)

print("Some common errors you might run into are:")

print("\t ZeroDivisionError: Occurs when you try to divide (normal division,\
 modulo(remainder of division) or integer division) any number by zero. This is\
 Python just enforcing the rules of Math e.g {}, {} and {} will give you a\
 ZeroDivisionError". format("3 / 0", "3 // 0", "3 % 0"))

print("\t SyntaxError: Occurs when you violate the rules of Python syntax e.g\
 leaving out a closing parantheses, having illegal whitespaces e.t.c")

print("\t TypeError: Occurs when you try calling a function or operand on a data\
 type that does not support that kind of operation or if you call a function\
 without giving all the required arguments e.g {} and {} will result in a\
 TypeError".format('len(10)', "'s'/3"))

print("\t IndexError: Occurs when you try accessing an index that does not exist\
 e.g {} will result in an IndexError because the string has up to index 2\
 because Python uses zero indexing".format("'she'[3]"))
