"""
1. Write a python program to create a user class with 3 properties : name, age, email.
"""

class user:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email

    def showdata(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Email : ", self.email)


Pushpak = user('Pushpak', 18, "abc@gmail.com")
Ram = user("Ram", 14, "ram@mail.com")

Pushpak.showdata()
print()
Ram.showdata()