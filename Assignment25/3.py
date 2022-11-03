"""
3.Write a python script to update 2nd Question, change email and age to __email and __age

"""




class Profile:
    def __init__(self, name, email, age) -> None:
        self.name = name
        self.__age = age
        self.__email = email

    def show(self):
        print(self.name)
        print(self.__email)
        print(self.__age)


obj1 = Profile('Pushpak', 'pushpakkhadke1617@gmail.com', 18)

obj1.name = 'Yash'
obj1.email = 'yash21@gmail.com'
obj1.age = 28

obj1.show()