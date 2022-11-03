"""
8. Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value.
"""

keys = ["Red","Gold","Yellow"]
values = ["#FF0000","#FFD700", "#FFFF00"]
print("Keys:- ",keys)
print("Values:- ",values)
color_dictionary = {keys[i]:values[i] for i in range(len(keys))}
print("Dictionary is:- ",color_dictionary)
