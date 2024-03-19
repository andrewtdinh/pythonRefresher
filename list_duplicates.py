# Check for duplicates in a list and return a list of duplicates:
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n'] 
expected = ['b', 'n']

def find_duplicates(a_list):
  dups = []
  unique_chars = set()
  for char in a_list:
    if char in unique_chars:
      # Found member in the set of unique chars (meaning char is a dup)
      dups.append(char)
    else:
      # If char not yet existed in unique set, add it
      unique_chars.add(char)
  
  return list(set(dups))


actual = find_duplicates(my_list)
print(actual)
print(expected)

