print("--- Conditional Constructions ---")

print("\n1. Password Check:")
correct_password = "password123"

# Test 1: Correct guess
user_guess_correct = "password123"
if user_guess_correct == correct_password:
    print("Test 1 Result: System access granted.")
else:
    print("Test 1 Result: Incorrect password.")

# Test 2: Incorrect guess
user_guess_wrong = "pass123"
if user_guess_wrong == correct_password:
    print("Test 2 Result: System access granted.")
else:
    print("Test 2 Result: Incorrect password.")


print("\n2. Day of the Week:")
# Test 1: Valid day
day_number = 5
if day_number == 1:
    print(f"Test 1: Day {day_number} is Monday.")
elif day_number == 2:
    print(f"Test 1: Day {day_number} is Tuesday.")
elif day_number == 3:
    print(f"Test 1: Day {day_number} is Wednesday.")
elif day_number == 4:
    print(f"Test 1: Day {day_number} is Thursday.")
elif day_number == 5:
    print(f"Test 1: Day {day_number} is Friday.")
elif day_number == 6:
    print(f"Test 1: Day {day_number} is Saturday.")
elif day_number == 7:
    print(f"Test 1: Day {day_number} is Sunday.")
else:
    print(f"Test 1: Day {day_number} is an invalid day number.")

# Test 2: Invalid day
day_number_invalid = 9
if day_number_invalid < 1 or day_number_invalid > 7:
    print(f"Test 2: Day {day_number_invalid} is an invalid day number.")


print("\n--- Loops ---")

print("\n1. Multiplication Table:")
number_to_multiply = 7
print(f"Multiplication table for {number_to_multiply}:")
for i in range(1, 11):
    print(f"{number_to_multiply} * {i} = {number_to_multiply * i}")


print("\n2. Sum of Numbers (using a loop):")
numbers_list = [10, 20, 30, 40]
total_sum = 0
for num in numbers_list:
    total_sum = total_sum + num
print(f"The sum of {numbers_list} is {total_sum}.")


print("\n3. Factorial:")
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print(f"Factorial of {n} (or {n}!) is {factorial}.")


print("\n4. Even Numbers from 1 to 50:")
even_numbers = []
for i in range(1, 51):
    if i % 2 == 0:
        even_numbers.append(i)
print(f"Even numbers (1-50): {even_numbers}")


print("\n5. Prime Numbers (in a range):")
start_range = 1
end_range = 20
primes = []
for num in range(start_range, end_range + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
print(f"Prime numbers between {start_range} and {end_range}: {primes}")


print("\n--- Lists ---")

print("\n1. List Operations:")
my_list = [5, 15, 25]
print(f"Original list: {my_list}")
my_list.append(10)
my_list.append(20)
print(f"After appending 10 and 20: {my_list}")
my_list.remove(10)
print(f"After removing 10: {my_list}")


print("\n2. Sum of a list (using built-in function):")
list_to_sum = [5, 15, 25, 100]
total = sum(list_to_sum)
print(f"The sum of {list_to_sum} is {total}.")


print("\n3. Doubled Values:")
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
for num in numbers:
    doubled_numbers.append(num * 2)
print(f"Original list: {numbers}")
print(f"Doubled list: {doubled_numbers}")


print("\n--- Tuples ---")

print("\n1. Accessing tuple elements:")
my_tuple = ("apple", "banana", "orange")
print(f"Tuple: {my_tuple}")
print(f"Element 0: {my_tuple[0]}")
print(f"Element 1: {my_tuple[1]}")
print(f"Element 2: {my_tuple[2]}")


print("\n2. Concatenating tuples:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
print(f"Combined: {combined_tuple}")


print("\n--- Dictionaries ---")

print("\n1. Dictionary Operations:")
athlete = {
    "name": "Mykhailo Mudryk",
    "age": 24, # (in 2025)
    "sport": "Football",
    "team": "Chelsea"
}
print(f"Athlete's Name: {athlete['name']}")
print(f"Athlete's Sport: {athlete['sport']}")
print(f"Athlete's Team: {athlete['team']}")


print("\n2. Updating a dictionary:")
favorite_books = {
    "Dune": 1965,
    "1984": 1949
}
print(f"Original books: {favorite_books}")
favorite_books["Brave New World"] = 1932
print(f"Updated books: {favorite_books}")


print("\n3. Find value by key (Dictionary search):")
capitals = {
    "Ukraine": "Kyiv",
    "USA": "Washington, D.C.",
    "France": "Paris"
}

# Test 1: Find "Ukraine"
country_to_find = "Ukraine"
if country_to_find in capitals:
    print(f"Test 1: The capital of {country_to_find} is {capitals[country_to_find]}.")
else:
    print(f"Test 1: Capital for {country_to_find} not found.")

# Test 2: Find "Germany"
country_to_find_fail = "Germany"
if country_to_find_fail in capitals:
    print(f"Test 2: The capital of {country_to_find_fail} is {capitals[country_to_find_fail]}.")
else:
    print(f"Test 2: Capital for {country_to_find_fail} not found.")