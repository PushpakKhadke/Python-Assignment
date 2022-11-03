"""
7. Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries.
"""

Dictionary1 = {
    1 : "Kunal",
    2 : "Hardik"
}
Dictionary2 = {
    3 : "Sonali",
    4 : "Monali"
}
Dictionary3 = {
    1 : "Yash",
    2 : "Jayesh"
}
Main_Dictionary = {
  "Dictionary1" : Dictionary1,
  "Dictionary2" : Dictionary2,
  "Dictionary3" : Dictionary3
}
print(Main_Dictionary)
