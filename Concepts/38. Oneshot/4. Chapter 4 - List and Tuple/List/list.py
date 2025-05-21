import copy

# List of Built-in Functions for Python Lists

"""
This section demonstrates the use of built-in Python list methods and operations.
These methods and operations allow for manipulation, analysis, and interaction with lists.

List Methods:
- append(): Adds an element to the end of the list.
- clear(): Removes all elements from the list.
- copy(): Returns a shallow copy of the list.
- count(): Returns the number of occurrences of a specified element in the list.
- extend(): Extends the list by appending elements from another iterable.
- index(): Returns the index of the first occurrence of a specified element.
- insert(): Inserts an element at a specified position in the list.
- pop(): Removes and returns the element at a specified position (default is the last element).
- remove(): Removes the first occurrence of a specified element.
- reverse(): Reverses the elements of the list in place.
- sort(): Sorts the elements of the list in ascending order (can be customized with a key or reverse argument).

Built-in Functions and Operations:
- list(): A built-in function to create a list. It can be used with an iterable to generate a list.
- del: A statement (not a method) used to delete an element or a slice from the list, or delete the list itself.
- in: A membership operator to check if an element exists in the list.
- len(): A built-in function to get the number of elements in the list.
- any(): Returns True if any element in the list evaluates to True, otherwise False.
- all(): Returns True if all elements in the list evaluate to True, otherwise False.
- sorted(): Returns a new sorted list from the elements of the original list.
- max(): Returns the largest element in the list.
- min(): Returns the smallest element in the list.
- sum(): Returns the sum of all numeric elements in the list.
- reversed(): Returns a reverse iterator over the elements of the list.
- enumerate(): Returns an enumerate object containing index-value pairs for the list.

Additional Notes:
- List comprehensions: A concise way to create lists using a single line of code.
    Example:
    ```python
    # Create a list of squares for numbers 0 through 9
    squares = [x**2 for x in range(10)]
    print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```
- Iterating over lists: You can iterate over elements using loops.
    Example:
    ```python
    my_list = [1, 2, 3]
    for item in my_list:
        print(item)
    ```
- Nested lists: Lists can contain other lists as elements, enabling hierarchical data structures.
    Example:
    ```python
    nested_list = [[1, 2], [3, 4]]
    print(nested_list[0][1])  # Output: 2
    ```
- Slicing: Use slicing to access a subset of elements in a list.
    Example:
    ```python
    my_list = [0, 1, 2, 3, 4]
    print(my_list[1:4])  # Output: [1, 2, 3]
    ```
- Mutable nature: Lists are mutable, meaning their elements can be changed after creation.
    Example:
    ```python
    my_list = [1, 2, 3]
    my_list[1] = 10
    print(my_list)  # Output: [1, 10, 3]
    ```
- List unpacking: Use `*` to unpack elements into function arguments or other variables.
    Example:
    ```python
    my_list = [1, 2, 3]
    a, *b = my_list
    print(a, b)  # Output: 1 [2, 3]
    ```
- Deep copy: Use the `copy` module's `deepcopy()` function to create a deep copy of a list containing nested lists.
    Example:
    ```python
    nested_list = [[1, 2], [3, 4]]
    deep_copied_list = copy.deepcopy(nested_list)
    ```
- List concatenation: Use the `+` operator to concatenate two or more lists.
    Example:
    ```python
    list1 = [1, 2]
    list2 = [3, 4]
    print(list1 + list2)  # Output: [1, 2, 3, 4]
    ```
- List repetition: Use the `*` operator to repeat a list a specified number of times.
    Example:
    ```python
    my_list = [1, 2]
    print(my_list * 3)  # Output: [1, 2, 1, 2, 1, 2]
    ```
"""