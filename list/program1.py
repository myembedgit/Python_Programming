
# Storing a number in 3x3 matrix #

final_list = [['😀','😀','😀'],['😎','😎','😎'],['😍','😍','😍']]

user_choice = input("Enter the place number to store the value:")

row    = int(user_choice[0]) - 1
column = int(user_choice[1]) - 1

user_number = int(input("Enter the number to store in array:"))

final_list[row][column] = user_number

print(final_list)