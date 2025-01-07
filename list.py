my_list = [10,-2,15,10,3,0,4]

#print(my_list[1::])  # max - 1

#my_list.sort()

#print(my_list)

minimum = min(my_list)
print(minimum)

maximum = max(my_list)
print(maximum)


print(len(my_list))
print(my_list)
my_list.reverse()

print(my_list)


my_list.append(20)

print(my_list)

my_list.insert(0,30)

my_list.insert(9,30)
print(my_list)

print(my_list[-1])
print(my_list[-2])

my_list.extend([30,60,90])
print(my_list)

my_list.remove(30)
print(my_list)

print(my_list.pop(2))

print(my_list)

print(my_list.count(30))