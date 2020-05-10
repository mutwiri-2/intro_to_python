print("functions have the advantage of making code easier to understand by making it easier to read and write blocks of code")
print("functions can help break down a program into smaller chunks by implementing a singular task that is part of the whole")
print("By naming functions using descriptive names of what task they accomplish, we help in improving understanding of code")
print('#' * 99)
print("Apart from using descriptive names for functions, we can also add documentation to help other programmers and our future selves understand what a funtion does")
print("DOCSTRINGS (documentation strings) are a type of comments that describe the purpose of a function and how to use it.")
print('#' * 99)

print("A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object")
print("All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the __init__ constructor) should also have docstrings. A package may be documented in the module docstring of the __init__.py file in the package directory.")

print("String literals occurring elsewhere in Python code may also act as documentation. They are not recognized by the Python bytecode compiler and are not accessible as runtime object attributes (i.e. not assigned to __doc__), but two types of extra docstrings may be extracted by software tools:")

print('1. String literals occurring immediately after a simple assignment at the top level of a module, class, or __init__ method are called "attribute docstrings".')
print('2. String literals occurring immediately after another docstring are called "additional docstrings"')

print('#' * 99)

print('For consistency, always use """triple double quotes""" around docstrings. Use r"""raw triple double quotes""" if you use any backslashes in your docstrings. For Unicode docstrings, use u"""Unicode triple-quoted strings""".')

print('#' * 99)

print("There are two forms of docstrings: one-liners and multi-line docstrings.")
print("One-liners are for really obvious cases. They should really fit on one line")
print("Notes for one-liners:")
print("1. Triple quotes are used even though the string fits on one line. This makes it easy to later expand it")
print("2. The closing quotes are on the same line as the opening quotes. This looks better for one-liners")
print("3. There's no blank line either before or after the docstring")
print('4. The docstring is a phrase ending in a period. It prescribes the function or method\'s effect as a command ("Do this", "Return that"), not as a description; e.g. don\'t write "Returns the pathname ...".')

print('#' * 99)
print('#' * 99)


print("The first line of a docstring gives a brief description of what the function does. This is enough if the function is not that complicated")
print('#' * 99)
print("If the function is a little complicated, you can include a paragraph to further describe the function")
print("The next line after the brief description is a description of the inputs (arguments) to the function. Here you list the arguments the function will take and their expected types, Then a description of what the arguments actually are (what they represent)")
print("After the inputs description, it is good to give a description of the output of the function also (what the function returns or prints out)")
print('#' * 99)
print('#' * 99)
print("an example of a docstring")
print("def population_density(population, land_area):\n\t\"\"\" Calculate the population density of an area\n\t\tINPUT:\n\t\tpopulation: int. The number of people in an area\n\t\tland_area: int or float. This is unit-agostic meaning if you give the area in a certain unit,\n\t\tsay kilometres or miles, the answer will be given in that unit\n\t\tOUTPUT:\n\t\tpopulation_density: population/land_area. The population density of a given area \"\"\"\n\treturn population/land_area")
print('#' * 99)

def population_density(population, land_area):
    """ Calculate the population density of an area
        INPUT:
        population: int. The number of people in an area
        land_area: int or float. This is unit-agostic meaning if you give the area in a certain unit, say kilometres or miles, the answer will be given in that unit
        OUTPUT:
        population_density: population/land_area. The population density of a given area """ 
    return population/land_area
print(population_density(900, 90))

print('#' * 99)
# Quiz: Write a Docstring
# Write a docstring for the readable_timedelta function
# Given an integer that represents a number of days, write a function that returns a string that states the number of weeks and number of days for example if days = 10, it should return 1 week(s) and 3 day(s)

def readable_timedelta(days):
    """ a function to calculate number of weeks and days given a number of days
        INPUT:
        days: int. a number representing the number of days
        OUTPUT:
        a string stating the number of days given, and the number of weeks and days that evaluates to"""
    weeks = days // 7
    remainder = days % 7
    return "Given {} days that is {} week(s) and {} days(s)".format(days, weeks, remainder)

print(readable_timedelta(90))
# help(readable_timedelta)


print('#' * 99)
# a better way to define the docstring
def readable_timedelta(days):
    """
    Return a string of days input and the number of weeks and days included in days

    Parameters:
    days -- number of days to convert(int)

    Returns:
    a string of days input and the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "Given {} days that translates to {} week(s) and {} day(s)".format(days, weeks, remainder)

print(readable_timedelta(366))
# help(readable_timedelta)