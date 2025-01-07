"""
mytuples_1 =((10,20,"Raja"),(1,2,3,4))

#mytuples_1[0] = 50

print(mytuples_1)
print(type(mytuples_1))

"""

name = ["Vairaperumal","Rajalingam","Manivel","Dhanalakshmi","Rajalingam"]

myname = f"my name is {name[-4]}"

if name[1] == name[-1]:
    print("Equal")
else:
    print("Not Equal")

print(myname)

name_1 = myname.split()

print(name_1)

my_numbers = [1,2,3,[4,5,6],7,8,9]

lenghth = len(my_numbers)

print(f"lenghth is {lenghth:}")

print(my_numbers[3])



mix_list = [10,20,["Raja","Lingam"]]

print(mix_list[2][0][0])


