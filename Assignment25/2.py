"""
2. Write a python script to update the above Profile class with encapsulation

"""

class Profile:
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.age = age
        self.email = email

    def show(self):
        print(self.name)
        print(self.email)
        print(self.age)


obj1 = Profile('Pushpak', 'pushpakkhadke1617@gmail.com', 18)
obj1.show()
