# Create a HashMap (dictionary)
hash_map = {}

# Insert values into the HashMap
hash_map["apple"] = 1
hash_map["banana"] = 2

# Search for a key in the HashMap
print("Value for 'apple':", hash_map.get("apple", "Not found"))

# Delete a key from the HashMap
del hash_map["banana"]
print("HashMap after deletion:", hash_map)
