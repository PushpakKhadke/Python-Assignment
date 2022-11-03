"""
8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
# order based on the ram size
"""

class laptop:
    def __init__(self,brand,ram,cpu,hdd) -> None:
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

obj1=laptop("Apple",8,'m1','500gb')
obj2=laptop('Lenovo',32,'i5','1tb')
obj3=laptop('HP',16,'i7','1tb')

lis=[]
lis=sorted([obj1.ram,obj2.ram,obj3.ram])
finallist=[]
for i in lis:
    if i==obj1.ram:
        finallist.append('obj1')
    elif i==obj2.ram:
        finallist.append('obj2')
    else:
        finallist.append('obj3')

print("Final list of object on the basis of there ram : ")
print(finallist)