"""
9.  Write a python program to create a School class and 3 instance variables and 1 class variable

"""


class school:
    school = 'INeuron'

    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def showdata(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)
        print("School : ", self.school)


user1 = school('Pushpak', 20, 'Male')
user2 = school("Sakshi", 20, 'Female')
user3 = school("Pooja", 19, 'FeMale')

user1.showdata()
print()
user2.showdata()
print()
user3.showdata()