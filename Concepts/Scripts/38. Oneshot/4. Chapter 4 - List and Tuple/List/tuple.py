# Tuple of Built-in Functions for Python Tuples

"""
This section demonstrates the use of built-in Python tuple methods and operations.
These methods and operations allow for manipulation, analysis, and interaction with tuples.

Tuple Methods:
- count(): Returns the number of occurrences of a specified element in the tuple.
- index(): Returns the index of the first occurrence of a specified element.

Built-in Functions and Operations:
- tuple(): A built-in function to create a tuple. It can be used with an iterable to generate a tuple.
- del: A statement (not a method) used to delete a tuple (tuples are immutable, so individual elements cannot be deleted).
- in: A membership operator to check if an element exists in the tuple.
- len(): A built-in function to get the number of elements in the tuple.
- any(): Returns True if any element in the tuple evaluates to True, otherwise False.
- all(): Returns True if all elements in the tuple evaluate to True, otherwise False.
- sorted(): Returns a new sorted list from the elements of the tuple.
- max(): Returns the largest element in the tuple.
- min(): Returns the smallest element in the tuple.
- sum(): Returns the sum of all numeric elements in the tuple.
- reversed(): Returns a reverse iterator over the elements of the tuple.
- enumerate(): Returns an enumerate object containing index-value pairs for the tuple.

Additional Notes:
- Tuple unpacking: Use `*` to unpack elements into function arguments or other variables.
    Example:
    ```python
    my_tuple = (1, 2, 3)
    a, *b = my_tuple
    print(a, b)  # Output: 1 [2, 3]
    ```
- Iterating over tuples: You can iterate over elements using loops.
    Example:
    ```python
    my_tuple = (1, 2, 3)
    for item in my_tuple:
        print(item)
    ```
- Nested tuples: Tuples can contain other tuples as elements, enabling hierarchical data structures.
    Example:
    ```python
    nested_tuple = ((1, 2), (3, 4))
    print(nested_tuple[0][1])  # Output: 2
    ```
- Slicing: Use slicing to access a subset of elements in a tuple.
    Example:
    ```python
    my_tuple = (0, 1, 2, 3, 4)
    print(my_tuple[1:4])  # Output: (1, 2, 3)
    ```
- Immutable nature: Tuples are immutable, meaning their elements cannot be changed after creation.
    Example:
    ```python
    my_tuple = (1, 2, 3)
    # my_tuple[1] = 10  # This will raise a TypeError
    ```
- Tuple concatenation: Use the `+` operator to concatenate two or more tuples.
    Example:
    ```python
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    print(tuple1 + tuple2)  # Output: (1, 2, 3, 4)
    ```
- Tuple repetition: Use the `*` operator to repeat a tuple a specified number of times.
    Example:
    ```python
    my_tuple = (1, 2)
    print(my_tuple * 3)  # Output: (1, 2, 1, 2, 1, 2)
    ```
"""