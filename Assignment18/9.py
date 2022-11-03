"""
9. Write a python program to merge two python dictionaries into one dictionary.

"""

Dictionary1 = {
    11:"Pushpak",
    12:"Yash"
}
Dictionary2 = {
    13: "Rohini",
    14: "Pooja"
}

Dictionary1.update(Dictionary2)
print(Dictionary1)
