my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n'] 
expected = ['b', 'n']

def list_duplicates(a_list):
  duplicates = []
  for char in a_list:
    if (a_list.count(char) > 1) & (char not in duplicates):
      duplicates.append(char)
  
  return duplicates

actual = list_duplicates(my_list)
print(f'Expected: {expected}')
print(f'Actual: {actual}')
