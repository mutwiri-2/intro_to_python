# check whether an object exists in another object using membership operators in and not in 
print("Membership operators evaluate if an object (on the left of the operator)\
 exists (is included) in another object (on the right of the operator)." )

print("The membership operators are:\n\t{}\n\t{}".format("in - evaluates if the\
 object on the left side is included in the object on the right side", "not in -\
 evaluates if the object on the left side is NOT included in the object on the right side"))
print('#' * 79)

print("They both operate on lists and strings")
print("For strings they return a bool of whether one string is a sub-string of\
 another while for a list they return a bool of whether an element exists within a list")
print('#' * 79)

print("Both membership operators (in and not in) match exactly the search object\
 on the left including uppercase / lowercase")

print("For a list, the search object must match exactly an element existing in\
 the list including uppercase and lowercase while for a string the substring must\
 be a sequence of characters exactly appearing in the same order in the string\
 including any spaces, punctuations and case")
print('#' * 79)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
greeting = 'Hey there, I am learning Python'
print("Given this list; days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',\
 'Friday', 'Saturday'],  we can look for a day as follows and see the result:\
 'monday' in days - {}, 'Sunday' in days - {}".format('monday' in days, 'Sunday' in days))
print('#' * 79)

print("Given this list; days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',\
 'Friday', 'Saturday'],  we can look for a day as follows and see the result:\
 'monday' not in days - {}, 'Sunday' not in days - {}".format('monday' not in days, 'Sunday' not in days))
print('#' * 79)

print("Given this string; greeting = 'Hey there, I am learning Python',  we can\
 look for a sub-string as follows and see the result: 'ther' in greeting - {},\
 'Iam' in greeting - {}".format('ther' in greeting, 'Iam' in greeting))
print('#' * 79)

print("Given this string; greeting = 'Hey there, I am learning Python',  we can\
 look for a sub-string as follows and see the result: 'ther' not in greeting - {},\
 'Iam' not in greeting - {}".format('ther' not in greeting, 'Iam' not in greeting))