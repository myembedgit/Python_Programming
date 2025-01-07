

pizza_size = input("Enter pizza size S->Small,M->Medium,L->Large:")

price = 0
size  = 0
if pizza_size == 's' or pizza_size == 'S':
    size = 1
elif pizza_size == 'm' or pizza_size == 'M':
    size = 2
elif pizza_size == 'L' or pizza_size == 'l':
    size = 3

if  size != 0:
  if 4:
    price = 100
  elif pizza_size == "M" or pizza_size == "m":
    price = 200
  elif pizza_size == "L" or pizza_size == "l":
    price = 300

  if pizza_size == "s" or pizza_size == "S":
    print("Pepper:30")
    price = price + 30
  elif (pizza_size == "M" or pizza_size == "m") or (pizza_size == "L" or pizza_size == "l") :
    print("Pepper RS.50")
    price = price + 50

  extra_chees = input("Extra Chees Y/N:")

  if(extra_chees == 'Y') or (extra_chees == 'y'):
    print("Extra Rs.20")
    price = price + 20;

  print(f"Total:{price}")
else:
    print("Try again!!!")

print("Thanks")


