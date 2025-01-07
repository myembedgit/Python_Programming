string_num = input("Enter the numbers with space:")

numbers = string_num.split()

count = 0
for num in numbers:
    count = count + 1

print(count)
print(numbers)
sum = 0
for num in range(count):
    numbers[num] = int(numbers[num])

for num in numbers:
    sum += num


print("Average is ",round(sum/count))
