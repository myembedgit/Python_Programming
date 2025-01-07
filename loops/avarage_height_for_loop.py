

numbers_str  = input("Enter the heights:")

numbers_str2 = numbers_str.split()
numbers = []
for number in numbers_str2:
    numbers.append(int(number))

sum1 = 0

print(numbers)

for num in range(len(numbers)):
    sum1 += numbers[num]

average_numbers  = round(sum1 / len(numbers))

print(f"The avarage height is {average_numbers}")


