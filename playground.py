# First steps python, Operators

if 5 > 2: 
  print("test python working")

variable_1, variable_2 = 0, 1

if variable_1 == 0:
  print('working')

if variable_2 == 1:
  print('working too')

if variable_1 == 0 and variable_2 == 1:
  print('working and')

if variable_1 == 0 or variable_2 == 1:
  print('working or')

def equals(first, second):
  return first == second

if not equals(variable_1, variable_2):  
  print('working not')

if variable_1 is not variable_2:
  print('working is not')

if variable_1 is variable_2: 
  print('it should not be printed')

fruit_list = ["apple", "banana"]

if "banana" in fruit_list:
  print('working for in')

if "apricot" not in fruit_list:
  print('working for apricot not in fruit list')

