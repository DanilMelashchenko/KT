import utilities

my_numbers = [5, 10, 22, 9, 81, 12]

print(f"Working with the list: {my_numbers}")

avg = utilities.calculate_average(my_numbers)
print(f"The average value is: {avg}")

maximum = utilities.find_max(my_numbers)
print(f"The maximum value is: {maximum}")

empty_list = []
print(f"\nWorking with an empty list: {empty_list}")
avg_empty = utilities.calculate_average(empty_list)
max_empty = utilities.find_max(empty_list)
print(f"The average value is: {avg_empty}")
print(f"The maximum value is: {max_empty}")