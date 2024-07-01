x = ['a', 'b', 'c']
y = ['1', '2', '3']
Z = ['a' : '1','b':'2','c':'3']

# Creating the dictionary
z = {key: value for key, value in zip(x, y)}

# Printing the result
print(z)  # Output: {'a': '1', 'b': '2', 'c': '3'}
