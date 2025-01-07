height = int(input("Your Height pls?"))

if height >=3 :
    print("Can ride")
    age = int(input("Age pls?"))
    if age <=18:
      print("Pay:rs.250")
    else:
      print("Pay:rs.500")
else:
    print("Permission denied")