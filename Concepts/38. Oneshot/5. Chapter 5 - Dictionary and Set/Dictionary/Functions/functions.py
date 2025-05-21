# Creating a sample dictionary for demonstration
sample_dict = {"a": 1, "b": 2, "c": 3}

"""
This section demonstrates the use of built-in Python dictionary methods and operations.
These methods and operations allow for manipulation, analysis, and interaction with dictionaries.

Dictionary Methods:
- clear(): Removes all items from the dictionary.
- copy(): Returns a shallow copy of the dictionary.
- fromkeys(): Creates a new dictionary with keys from an iterable and values set to a specified value.
- get(): Returns the value for a specified key, or a default value if the key is not found.
- items(): Returns a view object with a list of the dictionary's key-value pairs.
- keys(): Returns a view object with a list of the dictionary's keys.
- pop(): Removes the specified key and returns the corresponding value.
- popitem(): Removes and returns the last inserted key-value pair as a tuple.
- setdefault(): Returns the value of a key if it exists, otherwise inserts the key with a specified value.
- update(): Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.
- values(): Returns a view object with a list of the dictionary's values.

Built-in Functions and Operations:
- dict(): A built-in function to create a dictionary. It can be used with keyword arguments, a mapping object, or an iterable of key-value pairs.
- del: A statement (not a method) used to delete a key-value pair from a dictionary or delete the dictionary itself.
- in: A membership operator to check if a key exists in the dictionary.
- len(): A built-in function to get the number of items in the dictionary.
- any(): Returns True if any key in the dictionary evaluates to True, otherwise False.
- all(): Returns True if all keys in the dictionary evaluate to True, otherwise False.
- sorted(): Returns a sorted list of the dictionary's keys.
- max(): Returns the largest key in the dictionary.
- min(): Returns the smallest key in the dictionary.
- sum(): Returns the sum of all keys in the dictionary (if they are numeric).
- reversed(): Returns a reverse iterator over the dictionary's keys.

Additional Notes:
- Dictionary comprehensions: A concise way to create dictionaries using a single line of code.
- Iterating over dictionaries: You can iterate over keys, values, or key-value pairs using loops.
- Nested dictionaries: Dictionaries can contain other dictionaries as values, enabling hierarchical data structures.
- Default dictionaries: Using collections.defaultdict to provide default values for missing keys.
- Immutable dictionary keys: Dictionary keys must be immutable types like strings, numbers, or tuples.
- Merging dictionaries: Use the `|` operator (Python 3.9+) or the `update()` method to merge dictionaries.
- Dictionary views: The objects returned by `keys()`, `values()`, and `items()` are dynamic views that reflect changes to the dictionary.
- Dictionary unpacking: Use `**` to unpack key-value pairs into function arguments or merge dictionaries.
"""
