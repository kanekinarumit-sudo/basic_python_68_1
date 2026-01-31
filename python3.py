"""
#
# Part: Collections in Python
# Lists, Tuples, sets, and Dictionaries
#
"""

"""
#
# Lists
# 
"""
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list)
print(this_list[1])  # Accessing the second item
this_list[1] = "blackcurrant"  # Modifying the second item
print(type(this_list))  # Checking the type
print(len(this_list))  # Length of the list

"""
#
# sets
#
"""
this_set ={"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}

print(this_set)
print(type(this_set))  # Checking the type      
print(len(this_set))  # Length of the set

"""
#
# Dictionaries
# 
"""

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict)
print(this_dict["model"])  # Accessing the value of "model"
print(type(this_dict))  # Checking the type
print(len(this_dict))