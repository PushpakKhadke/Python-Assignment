"""
1. Write a python script to create a Profile class with 3 attributes (name, email, age)
"""

class Profile:
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.age = age
        self.email = email


obj1 = Profile('Pushpak', 'pushpakkhadke1617@gmail.com', 18)