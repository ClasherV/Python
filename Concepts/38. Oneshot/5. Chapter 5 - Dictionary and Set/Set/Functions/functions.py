# Using curly braces
my_set = {1, 2, 3}
"""
This section demonstrates the use of built-in Python set methods and operations.
These methods and operations allow for manipulation, analysis, and interaction with sets.

Set Methods:
- add(): Adds an element to the set.
- remove(): Removes a specified element from the set (raises KeyError if the element is not found).
- discard(): Removes a specified element from the set (does not raise an error if the element is not found).
- pop(): Removes and returns an arbitrary element from the set.
- clear(): Removes all elements from the set.
- copy(): Returns a shallow copy of the set.
- update(): Updates the set with elements from another set or iterable.
- intersection_update(): Updates the set with the intersection of itself and another set.
- difference_update(): Updates the set with the difference of itself and another set.
- symmetric_difference_update(): Updates the set with the symmetric difference of itself and another set.

Set Operations:
- union(): Returns a new set with elements from both sets.
- intersection(): Returns a new set with elements common to both sets.
- difference(): Returns a new set with elements in the first set but not in the second set.
- symmetric_difference(): Returns a new set with elements in either set but not in both.

Set Comparisons:
- issubset(): Checks if the set is a subset of another set.
- issuperset(): Checks if the set is a superset of another set.
- isdisjoint(): Checks if the set has no elements in common with another set.

Built-in Functions and Operations:
- set(): A built-in function to create a set from an iterable.
- len(): Returns the number of elements in the set.
- in: A membership operator to check if an element exists in the set.
- not in: A membership operator to check if an element does not exist in the set.
- any(): Returns True if any element in the set evaluates to True, otherwise False.
- all(): Returns True if all elements in the set evaluate to True, otherwise False.
- sorted(): Returns a sorted list of the set's elements.
- max(): Returns the largest element in the set.
- min(): Returns the smallest element in the set.
- sum(): Returns the sum of all elements in the set (if they are numeric).
- frozenset(): Creates an immutable version of a set.

Additional Notes:
- Sets are unordered collections of unique elements.
- Sets do not allow duplicate elements.
- Sets are mutable, but their elements must be immutable types like strings, numbers, or tuples.
- Frozensets are immutable sets that can be used as dictionary keys or elements of other sets.
- Set comprehensions: A concise way to create sets using a single line of code.
- Iterating over sets: You can iterate over elements of a set using loops.
- Nested sets are not allowed because sets themselves are mutable and cannot be hashed.
"""
# Using the set() constructor
my_set = set([1, 2, 3])
