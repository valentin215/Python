""" Numbers and Numeric types
# int / float / complex (5+6j)
"""

int_1 = 1
float_1 = 1.04
boolean_true = True
complex_1 = 5 + 6j

if isinstance(int_1, int):
  print('working for int')

if isinstance(float_1, float):
  print('working for float')

if isinstance(boolean_true, bool):
  print('working for boolean')

# string(boolean) --> cast boolean into string

if isinstance(complex_1, complex):
  print('working for complex numner')

""" String types
# string + methods
"""

string = "Python"
length = len(string)
char = string[:-5]
print(length)
print(char)

test_tuple = ('John', 'Peter', 'Val')
result = ', '.join(test_tuple)
print(result)

formating_variable = 2020
sentence = f'We are in {formating_variable}'
print(f'We are in {formating_variable}') 
print(sentence)

# .format 
sentence_test = '{}, were are in {}'.format('Hello', 2020)
print(sentence_test)

""" List type """

list_test = [1, 2, 3]
list_test.append(4)
print(list_test)
list_test.remove(4)
print(list_test)
list_test[:] = []
list_test = [1, 2, 3]
index = list_test.index(2)
print(index)
list_looped = [x * 2 for x in list_test]
print(list_looped)

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
print(transposed_matrix)

transposed = []
for i in range(4):
  transposed.append([row[i] for row in matrix])
  print(transposed)

# transposed_second = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         row = row[i]
#         print(row)
#         transposed_row.append(row[i])
#     transposed_second.append(transposed_row)  

""" Tuples """

fruits_tuple = ("apple", "banana", "cherry")
length_tuple = len(fruits_tuple)
print(fruits_tuple)
print(length_tuple)

""" Sets """

fruits_set = {"apple", "banana", "cherry"}
first_fruit_set = set('apple')
print (first_fruit_set)

""" Dictionaries """

fruits_dictionary = {
        'cherry': 'red',
        'apple': 'green',
        'banana': 'yellow',
    }

dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
del dictionary_for_string_keys["sape"]
print(dictionary_for_string_keys)

""" Type casting """

number = 1
int(number)
result = isinstance(number, int) 
print(result)
print(number)
float(number)
print(number)
result_string = isinstance(str(number), str)
print(result_string)
print(number)

