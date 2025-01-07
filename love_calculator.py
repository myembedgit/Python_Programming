from platform import libc_ver

True_var = "true"
Love_var = "love"

name1 = input("Enter the name:")

name2 = input("Enter the pair name:")

name = name1 + name2

print(name)

name_lower = name.lower()

print(name_lower)


count_0 = name_lower.count(True_var[0])
count_1 = name_lower.count(True_var[1])
count_2 = name_lower.count(True_var[2])
count_3 = name_lower.count(True_var[3])


true_count = count_0 + count_1 +count_2 + count_3
print(count_0)
print(count_1)
print(count_2)
print(count_3)

print(true_count)

count_0 = name_lower.count(Love_var[0])
count_1 = name_lower.count(Love_var[1])
count_2 = name_lower.count(Love_var[2])
count_3 = name_lower.count(Love_var[3])

love_count = count_0 + count_1 +count_2 + count_3

print(love_count)

love_score = int(str(love_count) + str(true_count))

if love_score < 10 or love_score > 90 :
    print("Like mentos and Cock")
elif (love_score >= 40) and (love_score <= 90) :
    print("Commited")
else:
    print(f"Your Love score:{love_score}")
