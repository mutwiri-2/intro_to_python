# execute or skip blocks of code depending on conditions evaluating to true or false.

print("Python code is normally read and executed line by line from top to bottom\
 by the Python interpreter")
print("However, sometimes we might want to have some block of code executed and\
 other blocks skipped depending on some conditions")

print("if statements are conditional statements that execute or skip blocks of\
 code depending on whether the conditions they check evaluate to True or False")
print('#' * 79)

print("An if statement is declared as follows:\n\tYou begin with the if keyword\
 followed by a condition which must be a boolean expression (meaning the\
 expression must evaluate to either True or False) then end with a full colon(:)\
 \n\tBelow that you then have an indented block of code that you wish to be\
 evaluated if the conditional statement evaluates to True, or otherwise skipped\
 if it evaluates to False. This block is called the if clause")
print('#' * 79)

print("Python indents blocks of code using spaces (4 spaces by default - use\
 spaces instead of TABS according to Python specification but you can still use\
 TABS long as you are consistent and do not mix them).")

print("The indented block of code beneath an if statement is executed if and\
 only if the condition in the if clause executes to True")
print('#' * 79)

print("Sometimes, you have a few blocks of code which have different conditions\
 you want executed depending on which condition executes to True.\n In this case,\
 Python has two more clauses you can use to have your different conditions and\
 their corresponding blocks of code executed as follows:")
print('#' * 79)

print("1. elif (short for else if) statement - This is a conditional clause that\
 begins with the elif keyword followed by a condition to be checked then a full\
 colon(:) and below it an indented block of code that will execute if condition\
 evaluates to True")

print("You can have as many elif clauses as neccessary, each with its condition\
 to check and evaluates if the other clauses above it execute to false ie the rest\
 of the elif clauses are automatically skipped once a True condition has been found")
print('#' * 79)

print("2. else - This clause is the last in an if statement. It will execute if\
 all other clauses (the ifs and elifs) execute to false. It does not need a\
 condition (boolean expression) - just define it using the else keyword followed\
 by a full colon (:)")
print('#' * 79)

print("An example of an if statement:\nweather = 'rainy'\nif weather == 'sunny':\
\n\tprint(\"Wear light clothes\")\nelif weather == 'cold':\n\tprint(\"Wear warm\
 clothes\")\nelif weather == 'rainy':\n\tprint(\"Carry an umbrella\")\nelse:\n\t\
print(\"Weather is confusing!)")

weather = 'rainy'
if weather == 'sunny':
    print("Wear light clothes")
elif weather == 'cold':
    print("Wear warm clothes")
elif weather == 'rainy':
    print("Carry an umbrella")
else:
    print("Weather is confusing!")
print('#' * 79)

print("After the example, the line printed is 'Carry an umbrella' because that\
 is the block that will be executed since our weather variable is set to 'rainy'")
print('#' * 79)

print("The if statement executes from top to bottom - once a condition is satisfied,\
 the execution stops and exits from the if statement to the next code block after it.\
 This understanding should help you structure your if statements well for the best\
 efficiency for your code execution")
print('#' * 79)

print("The condition that follows the if keyword or elif for that matter need not\
 always be a single boolean expression. You can create complex boolean expressions\
 by having multiple comparison operators in the same expression  e.g checking for\
 a range if object is of a numerical type\nYou can also use logical operators to\
 create a long complicated condition. Use parantheses to clearly show your order\
 of execution or clarify your criteria")
print('#' * 79)

print("A few examples of some complex conditions using multiple comparison\
 operators in the same expression and logical operators to create a long\
 complicated condition, using parantheses to clearly show order of execution or\
 clarify criteria:")
print('#' * 79)

print("if 20000 <= salary <= 100000:\n\tprint('tax to be paid is 20%)")
print('#' * 79)

print("if (not_unsubscribed) and (location == 'KE' or location == 'TZ') and (payed):\
\n\tprint('Send email link')")
print('#' * 79)

print("If you give a non-boolean object as your condition in the if statement,\
 then Python does what is called TRUTH VALUE TESTING i.e it checks for the truth\
 value of the object and then depending on the result it either runs the code\
 block that follows or it doesn't")
print('#' * 79)

print("Objects have a truth value of True unless specified as False in the Python\
 documentation. The buit-in objects specified as false are: \n\t{}, \n\t{} and\
 \n\t{}".format("Constants defined to be False- None and False", "Zero values of\
 any numeric data type- 0, 0.0, 0j, Decimal(0), Fraction(0,1)", "empty collections\
 and sequences - '', \"\", [], {}, set(), range(0)"))
print('#' * 79)

print("There are a few do's and dont's when defining conditional statements:")
print("1. Do not use the keywords True or False as conditions or any combination\
 that results in True or False always - They might be valid boolean expressions\
 but it does not make sense to use them as conditions because;\n\t for the True\
 value, the statement will always evaluate to True and the block of code indented\
 below it will always run\n\t  for the False value, the statement will always\
 evaluate to False and the block of code indented below it will never run")
print('#' * 79)

print("2. Be careful when dealing with logical operators, as they have quite a\
 different meaning in Python in contrast to English. Make sure that each expression\
 to either side of a logical operator is a valid boolean expression that results\
 in a boolean value to make sure your code works as expected e.g:")

print("if weather == 'cold' and 'rainy':\n\tprint(\"carry an umbrella\")")

print("The above code would not execute as expected because to the right of the\
 and logical operator we do not have a boolean expression, rather we have a string.\
 This is still valid in Python (as Python will do truth value testing on this\
 non-boolean object) but will not give the expected result.")

print("if weather == 'cold' and weather == 'rainy':\n\tprint(\"carry an umbrella\")")

print("The above is an unambigous and correct version of the code, where the expression\
 to each side of the logical operator is a boolean expression")
print('#' * 79)

print("3. Do not compare variables with '==True' and '==False' - If you have a\
 variable which is already a boolean, you do not need to compare it using\
 '==True' and '==False' since it is already a boolean object.")
print('#' * 79)

print("NOTE: Always try to write succint (clear, clean and short code) by\
 considering the flow of the if statement and the 3 rules above")