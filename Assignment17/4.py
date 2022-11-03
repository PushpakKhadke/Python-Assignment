# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
# "Python", "Django"}

thisset = {"Java", "Python", "Django"}
for i in thisset:
    if i=="Python":
        print('Yes it is present ')

"""
2nd Way! 

thisset = {"Java", "Python", "Django"}
print("Python" in thisset)
"""