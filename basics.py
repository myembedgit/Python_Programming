"""
age = int(input("Enter your age:"))

if age < 18:
    print("Minor")
else:
    print("Adult")

"""
from xml.dom.minidom import ProcessingInstruction

"""
choice = 1

if choice == 1:
    print("1 is selected")
elif choice == 2:
    print("2 is selected")
else:
    print("Invalid option")

def case1():
    return "Option 1 selected."

def case2():
    return "Option 2 selected."

def default():
    return "Invalid option."

switch = {
    1: case1,
    2: case2
}


print(switch.get(choice, default)())  # Output: Option 2 selected.


"""

"""
fruits = ["Apple", "Banana", "Cherry", "Mango"]

# Loop through a list
for fruit in fruits:
    print(fruit)
"""

#printing name by char by char

name = "Rajalingam V"

print(len(name))

for letter in name:
 print(letter)

