"""
numbers = [1,2,3,4,5]

for number in numbers:
    print(number)
else:
    print("Completed")
"""


numbers = (1,2,3,4,5)   #tuple

for number in numbers:
    if number == 6:
        print("Break Executing")
        break
    else:
        print(number)
else:
    print("Completed")

print("Out of Loop")