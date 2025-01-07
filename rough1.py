height = int(input("Enter height in Feet:"))
price = 0
if height >= 3 :
    age = int(input("Enter your age:"))
    if age < 12 :
        price = 150
        print("Rs.150 for Ride")
    elif (age >= 12) and (age < 18) :
        price = 250
        print("Rs.250 for Ride")
    elif age >=18:
        price = 500
        print("Rs.500 for Ride")
    else:
        print("Can not ride")

    choice = input("Photo need Y/N:")

    if(choice == "y") or (choice == "Y"):
        price = price + 50
        print("Rs.50 extra you need to pay")

    print(f"Total Amount:{price}")

    print("Enjoy the ride")
else:
    print("Can not ride")

print(f"Thanks you! welcome again")