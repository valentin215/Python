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

formating_variable = 'Hello'
# sentence = f'We are in {formating_variable}'
print(f'We are in {formating_variable}')
