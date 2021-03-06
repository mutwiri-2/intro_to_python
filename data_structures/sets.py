# store unique elements with no particular ordering using the set data structure

print("Sets are a data type for a mutable collection of unique elements in no\
 particular order")

print("Sets are mutable meaning you can modify the contents. They are unordered,\
 meaning you cannot index or slice to access elements")
print('#' * 79)

print("Sets can be created as follows:")
a_set = {1,2,3,4,5,2,3,1,5,1,3,6,7,1,2}

print("1. By using curly braces '{}' to delimit a collection of elements\
 separated by commas.\n If there are any duplicate elements, they will be removed\
 and the set will only store unique elements e.g\n if we declare a set as follows;\
 a_set = {1,2,3,4,5,2,3,1,5,1,3,6,7,1,2} and print it out we will get-", a_set)
print('#' * 79)

list_sentence = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore','she',\
 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
set_sentence = set(list_sentence)

print("2. Using the set() method which can for example be used to quickly remove\
 duplicates from a list and create a set e.g given\n list_sentence = ['she', 'sells',\
 'sea', 'shells', 'by', 'the', 'sea', 'shore','she', 'sells', 'sea', 'shells', 'by',\
 'the', 'sea', 'shore'] \nWe can create a set as follows: set_sentence = set(list_sentence)\
 to get;\n", set_sentence)
print('#' * 79)

print("Sets are mutable so you can add or remove elements from them using:\n\t{}\
  \n\t{}".format("add() method- adds an element to the set", "pop() method removes\
 and returns an element from the set"))

set_sentence.add('fish')
print("set_sentence.add('fish') then print(set_sentence) to get:\n",set_sentence)

removed_element = set_sentence.pop()
print("removed_element = set_sentence.pop() then print(removed_element, set_sentence)\
 to get:\n removed element is {} and remaining set is {}".format(removed_element, set_sentence))
print('#' * 79)

print("The remove() method removes the specified element from the set. e.g set_sentence.remove('fish')")

print('#' * 79)

print("Sets are simple data structures and they have one main use - collecting\
 unique elements".upper())
print("sets also make it easier to perform mathematical set operations such as\
 union, intersection and difference")