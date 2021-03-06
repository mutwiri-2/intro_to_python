print("Input validation checks that values entered by the user in your program are formatted correctly")
print("This helps in avoiding bugs, making sure your programs do not crash later on due to invalid values for example if you ask a user for their age, you expect a number (digit value) - an integer to be precise which should not be negative ofcourse. If a user input does not adhere to the above rules, you should prompt them to re-enter the value again")

print('#' * 99)

print("Input validation also can help avoid security vulnerabilities")
print("For example say you were implementing a withdraw_from_account() function and the user had to input the amount they want to withdraw. You have to make sure that the user does not enter a negative amount because subtracting a negative amount from the account would end up actually adding. Therefore, the 'withdrawal' would end up adding money to the account instead of subtracting")

print('#' * 99)

# input validation example
while True:
    age = input("Enter your age:\n")
    try:
        age = int(age)
    except:
        print("Please input a number in digits")
        continue
    if age < 1:
        print("Age cannot be negative. Input a positive number")
        continue
    elif age > 150:
        print("You cannot be that old. Come on!!")
        continue
    else:
        break
print(f'Hey {age} years old human!')

print('#' * 99)

print("PyInputPlus".center(99, '='))
print("PyInputPlus is a Python3 module to provide input()-like functions with additional validation features")
print("PyInputPlus is not part of the Python Standard Library thus has to be installed separately using pip as follows\n 'pip3 install pyinputplus' ")
print("The module contains functions similar to the standard Python input() function for different kinds of data e.g email addresses, dates, numbers e.t.c")

print('#' * 99)

print("If a user ever enters an invalid input of the kind of data specified by any of the PyInputPlus input functions, eg a wrongly formatted date, PyInputPlus will re-prompt them to enter the input again")
print("In addition to re-prompting, PyInputPlus has other useful features e.g a limit of the number of times to re-prompt user for input, a timeout feature if the user is required to respond within a specific time duration")

print('#' * 99)

print("PyInputPlus Functions".center(99, '='))
pyip_functions = {
    'inputStr()': "Prompts the user to enter any string input. This is similar to Python’s input() function but with PyInputPlus’s additional features such as timeouts, retry limits, stripping, allowlist/blocklist, etc",
    'inputNum()': "Prompts the user to enter a number, either an integer or a floating-point value. Returns an int or float value (depending on if the user entered a decimal in their input.)",
    'inputChoice()': "Prompts the user to enter one of the provided choices. Returns the selected choice as a string.",
    'inputMenu()': "Prompts the user to enter one of the provided choices. Also displays a small menu with bulleted, numbered, or lettered options. Returns the selected choice as a string.",
    'inputDatetime()': "Prompts the user to enter a datetime, formatted as a strptime-format in the formats list. Returns a datetime.datetime object.",
    'inputYesNo': "Prompts the user to enter a yes/no response. The user can also enter y/n and use any case. Returns the yesVal or noVal argument (which default to 'yes' and 'no'), depending on the user’s selection.",
    'inputBool()': "Prompts the user to enter a True/False response. The user can also enter t/f and in any case. Returns a boolean value.",
    'inputEmail()': "Prompts the user to enter an email address. Returns the email address as a string",
    'inputFilepath()': "Prompts the user to enter a filepath. If mustExist is True, then this filepath must exist on the local filesystem. Returns the filepath as a string",
    'inputPassword()': "Prompts the user to enter a password. Mask characters will be displayed instead of the actual characters"
}
import pprint
print(pprint.pformat(pyip_functions))

print('#' * 99)

print("Here are some PyInputFunctions and what they do".center(99, '='))
for function, definition in pyip_functions.items():
    print(function)
    print(definition)

print('#' * 99)

# example of PyInputPlus in action
import pyinputplus as pyip

response = pyip.inputNum("Enter a number\n")
print(f"Number entered is {response} and is of type {type(response)}")

print('#' * 99)

print("The min, max, lessThan and greaterThan kwargs".center(99, '='))
print("The inputNum(), inputInt() and inputFloat() functions which accept int and float numbers have min, max, lessThan and greaterThan keyword arguments which specify a range of valid input values")
print("They are optional but if specified they have the following effect:")
print("1. min - the input value cannot be less than the min argument (but can be equal to it.)")
print("2. max - the input value cannot be greater than the max argument (but can be equal to it.)")
print("3. lessThan - the input value cannot be less than the lessThan argument (and cannot be equal to it.)")
print("4. greaterThan - the input value cannot be greater than the greaterThan argument (and cannot be equal to it.)")

print('#' * 99)
# max and min
user_int = pyip.inputInt(prompt="Enter an integer\n", max=100, min=-50)
print(f"Number entered is {user_int}")
# lessThan and greaterThan
user_float = pyip.inputFloat(prompt="Enter a number with a decimal point\n", greaterThan=10.0, lessThan=50)
print(f"Number entered is {user_float}")

print('#' * 99)

print("The blank kwarg".center(99, '='))
print("By default, blank argument is not allowed unless blank kwarg is set to True")
print("Use blank=True if you would like the input to be optional and the user does not have to enter a value")
# no blank input allowed
optional_input = pyip.inputStr(limit=3, default='No input entered')
print(optional_input)
# blank input allowed
optional_input = pyip.inputStr(prompt='>>>', blank=True)
print(type(optional_input))

print('#' * 99)

print("The limit, timeout and default kwargs".center(99, '='))
print("limit keyword argument is passed an integer to determine how many seconds a PyInputPlus function will make to receive a valid input before giving up")
print("timeout keyword argument is passed an integer to determine how many seconds a PyInputPlus function will wait to receive a valid input before giving up")
print("If the user fails to enter a valid input before limit and timeout are reached, PyInputPlus will raise a RetryLimitException and TimeoutException respectively")
print("Pass a default keyword argument to be returned by the functions instead when limit and timeout is reached instead of an exception being raised")

print('#' * 99)

timeout_input = pyip.inputPassword(prompt="Enter Password\n", timeout=3, default="Wrong Password")
print(timeout_input)

limit_input = pyip.inputPassword(prompt="Enter Password\n", limit=3, default="No input")
print(limit_input)

print('#' * 99)
print("allowRegexes and blockRegexes keyword arguments".center(99,'='))
print("You can use regular expressions to specify whether an input is allowed or not")
print("allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus will accept or decline as valid input")

print('#' * 99)

# allowRegexes
allow_roman_numerals = pyip.inputNum(prompt="Enter a number\n", allowRegexes=[r'(i|v|x|l|m|c|d)+'])
print(allow_roman_numerals)

# blockRegexes
block_odd_numbers = pyip.inputNum(prompt="Enter a number\n", blockRegexes=[r'[13579]$'])
print(block_odd_numbers)

print('#' * 99)

print("If you pass both a allowRegexes and blockRegexes argument, the allow overrides the block incase of any conflict")
allow_overrides = pyip.inputStr(prompt="enter any word\n", allowRegexes=[r'catastrophe', r'caterpillar'], blockRegexes=[r'cat'])
print(allow_overrides)

print('#' * 99)

print("Passing a custom validation function to inputCustom()".center(99,'='))
print("You can write a function that performs some custom validation logic not provided by the functions in PyInputPlus by passing the function to inputCustom()")
print("Your function should:")
print("1. Accept a string argument of what your user entered")
print("2. Raise an exception if the string fails validation")
print("3. Returns None (or has no return statement) if inputCustom should return the string unchanged")
print("4. Returns a non-None value if inputCustom() should return a different string from the one the user entered")
print("5. Be passed as the first argument to inputCustom()")
print("Note that the function call looks like inputCustom(name_of_custom_function) and not inputCustom(name_of_custom_function()) because you are passing the function itself to inputCustom() and not calling the custom function and passing the return value to inputCustom()")

print('#' * 99)

# custom validation function 
def add_up_to_ten(numbers):
    numbers_list = list(numbers)
    for i, digit in enumerate(numbers_list):
        numbers_list[i] = int(digit)
    if sum(numbers_list) != 10:
        raise Exception("The sum of the numbers should be equal to {} not {}".format(10, sum(numbers_list)))
    return(int(numbers))

response = pyip.inputCustom(add_up_to_ten, prompt="Enter numbers adding up to ten\n")
print(response)

print('#' * 99)

print("Writing your own custom validation function is useful when it is otherwise impossible to write a regex for valid input")

print('#' * 99)
