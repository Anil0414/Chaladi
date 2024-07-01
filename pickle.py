import pickle

data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Serialize the object and save it to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Serialize the object and save it to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
# Load the object from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
