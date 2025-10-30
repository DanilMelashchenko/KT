print("--- 1. Creating variables ---")
my_string = "Hello Python"
my_integer = 142
my_float = 3.14
my_bool = False
my_list = [1, 'apple', 2.5]
my_dict = {'student': 'Danylo', 'grade': 100}
my_tuple = (1, 'apple', 2.5)
my_none = None

print(f"String: {my_string} (Type: {type(my_string)})")
print(f"Integer: {my_integer} (Type: {type(my_integer)})")
print(f"Float: {my_float} (Type: {type(my_float)})")
print(f"Bool: {my_bool} (Type: {type(my_bool)})")
print(f"List: {my_list} (Type: {type(my_list)})")
print(f"Dict: {my_dict} (Type: {type(my_dict)})")
print(f"Tuple: {my_tuple} (Type: {type(my_tuple)})")
print(f"None: {my_none} (Type: {type(my_none)})")

print("\n--- 2. Comparison Operators ---")
print(f"100 == 100: {100 == 100}")
print(f"142 != 3.14: {142 != 3.14}")
print(f"10 > 5: {10 > 5}")
print(f"'apple' == 'apple': {'apple' == 'apple'}")
print(f"'apple' == 'Apple': {'apple' == 'Apple'}")
print(f"'a' < 'b': {'a' < 'b'}")
print(f"True == True: {True == True}")
print(f"True > False: {True > False}")
print(f"[1, 2, 3] == [1, 2, 3]: {[1, 2, 3] == [1, 2, 3]}")
print(f"[1, 2, 3] == my_list: {[1, 2, 3] == my_list}")
print(f"my_list == my_tuple: {my_list == my_tuple}")
print(f"my_dict == {{'student': 'Danylo', 'grade': 100}}: {my_dict == {'student': 'Danylo', 'grade': 100}}")

print("\n--- 3. String Operations ---")
num_str = 125
num_as_string = str(num_str)
print(f"1. Number {num_str} converted to string: '{num_as_string}' (type: {type(num_as_string)})")

message = 'Hi, my name is Python!'
message_replaced = message.replace('y', '0').replace('i', '1')
print(f"2. Original: '{message}'")
print(f"   After replace: '{message_replaced}'")

split_test = 'This is a split test'
split_result = split_test.split(' ')
print(f"3. Result of split(): {split_result}")

string_join = '...'.join(split_result)
print(f"   Result of join(): '{string_join}'")

string_length = len(string_join)
print(f"4. Length of string '{string_join}': {string_length} characters")

print("\n--- 3. List Operations ---")
list_append = [1, 2, 3]
print(f"1. List before append(): {list_append}")
list_append.append(4)
list_append.append(5)
print(f"   List after append(4) and append(5): {list_append}")

list_extend = [4, 5, 6]
print(f"2. List before extend(): {list_extend}")
list_extend.extend([7, 8, 9])
print(f"   List after extend([7, 8, 9]): {list_extend}")

index_of_6 = list_extend.index(6)
print(f"3. Index of element 6 in {list_extend}: {index_of_6}")

list_length = len(list_append)
print(f"4. Length of list {list_append}: {list_length} elements")

print("\n--- 3. Dictionary Operations ---")
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(f"Dictionary: {dict_test}")

print(f"1. Value for key 'car': {dict_test['car']}")
print(f"   Value for key 'where': {dict_test['where']}")

print(f"2. All keys: {dict_test.keys()}")
print(f"   All values: {dict_test.values()}")

print(f"3. All pairs (key-value): {dict_test.items()}")
print("   Looping through items:")
for key, value in dict_test.items():
    print(f"     Key: {key}, Value: {value}")