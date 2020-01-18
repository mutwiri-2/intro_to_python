print("loops are a way to repeat blocks of code")
print("Python has two types of loops:\n\t{}, and \n\t{}".format("for loops", "while loops"))
print('#' * 99)
print("for loops are loops that iterate(repeatedly do an action) over an iterable")
print("An iterable is an object that can return each of its elements one at a time")
print("An iterable can be of the sequence types like lists, tuples, strings etc or of the non-sequence types like dicts and files")
print('#' * 99)
print("A for loop can be defined as follows:")
print("for iteration_variable in iterable:\n\t#block of code to be executed")
print('#' * 99)
print("You begin with the for keyword which signals that this is a for loop,\nthen the iteration variable which represents the element from the iterable that the loop is currently processing for each iteration\nthen the in keyword,\nthen the iterable\nFinally you end the for statement with a full colon(:)")
print('#' * 99)
print("Below the for statement is an indented block of code that executes once for each iteration")
print("The iteration variable can be accessed and used by the indented block of code during each iteration")
print('#' * 99)
print("The range() function is a useful function when dealing with loops\nIt generates an iterable sequence of numbers")
print("The range() function has three arguments, all of which must be integers as follows, of which the first and third are optional - range(start, stop, step)")
print("Start indicates which number the sequence starts from, the default is 0")
print("Stop is one number higher than the last number in the sequence- this argument is mandatory")
print("Step is the difference between each number in the sequence - defaults to one if not specified")
print('#' * 99)
print("If you supply only one argument to range() then it is used as the stop value and the start defauts to 0 and step to 1")
print("If you supply two arguments to range() then the first is used as the start value and the second as the stop value and step defaults to one.")
print("If you supply three arguments to range() then the first is used as the start value, the second as the stop value and the third as the step")
print('#' * 99)
print("range() is often used to repeat a block of code a number of times e.g to print a greeting 10 times we would do it as follows;\n for i in range(10):\n\tprint('Helloooo')")
for i in range(10):
    print("Helloooo")


print('#' * 99)
# PRACTICE
teams = ['Liverpool', 'Mancity', 'Man-u', 'Arsenal', 'Tottenham']
for team in teams:
    print(team.lower()) # print out each element in teams converted to lower case
print("All Done!")

print('#' * 79)

reversed_elements_list = []
for team in teams:
    reversed_elements_list.append(team[::-1])  #  reverse each string(element) in the teams list and add it to the new list
print(reversed_elements_list)

print('#' * 79)

#modify the team list to have all caps using the range() function
for index in range(len(teams)):
    teams[index] = teams[index].upper()
print(teams)

print('#' * 79)

print(range(0, 100, 5))  # returns a range object
print(list(range(0, 100, 5)))  # convert range object to a list object
for num in range(0, 100, 5):  # iterate through the range object and print each number
    # print(num, end =" ")   #print numbers on the same line
    print(num)

print('#' * 79)
# Use a for loop to take a list and print each element of the list in its own line.
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)

print('#' * 79)

# Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
for num in range(5,31,5):
    print(num)

print('#' * 99)

# Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should create the list:

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
user_names = []
for name in names:
    name = name.replace(' ', '_').lower()
    user_names.append(name)
print(user_names)

print('#' * 79)
# Write a for loop that uses range() to iterate over the positions in names to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores.

for index in range(len(names)):
    names[index] = names[index].replace(' ', '_').lower()
print(names)

print('#' * 79)

# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.
# tokens = ['<greeting>', 'Hello World!', '</greeting>']
# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print("There are {} xml tags in the list of strings, tokens".format(count))

print('#' * 79)

