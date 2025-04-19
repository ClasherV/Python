"""
This section demonstrates the use of built-in Python string methods and operations.
These methods and operations allow for manipulation, analysis, and interaction with strings.

String Methods:
- capitalize(): Converts the first character of the string to uppercase.
- casefold(): Converts the string to lowercase, suitable for caseless comparisons.
- center(): Returns a centered string of a specified width.
- count(): Returns the number of occurrences of a specified substring in the string.
- encode(): Encodes the string using the specified encoding.
- endswith(): Returns True if the string ends with the specified suffix.
- expandtabs(): Replaces tab characters with spaces, using a specified tab size.
- find(): Returns the index of the first occurrence of a specified substring, or -1 if not found.
- format(): Formats the string using placeholders and specified values.
- format_map(): Formats the string using a mapping object.
- index(): Returns the index of the first occurrence of a specified substring, raises ValueError if not found.
- isalnum(): Returns True if all characters in the string are alphanumeric.
- isalpha(): Returns True if all characters in the string are alphabetic.
- isascii(): Returns True if all characters in the string are ASCII.
- isdecimal(): Returns True if all characters in the string are decimal characters.
- isdigit(): Returns True if all characters in the string are digits.
- isidentifier(): Returns True if the string is a valid Python identifier.
- islower(): Returns True if all cased characters in the string are lowercase.
- isnumeric(): Returns True if all characters in the string are numeric.
- isprintable(): Returns True if all characters in the string are printable.
- isspace(): Returns True if all characters in the string are whitespace.
- istitle(): Returns True if the string is title-cased.
- isupper(): Returns True if all cased characters in the string are uppercase.
- join(): Concatenates the elements of an iterable with the string as a separator.
- ljust(): Returns a left-justified string of a specified width.
- lower(): Converts all characters in the string to lowercase.
- lstrip(): Removes leading characters (default is whitespace) from the string.
- maketrans(): Returns a translation table for use with the translate() method.
- partition(): Splits the string into three parts using the first occurrence of a specified separator.
- replace(): Replaces occurrences of a specified substring with another substring.
- rfind(): Returns the index of the last occurrence of a specified substring, or -1 if not found.
- rindex(): Returns the index of the last occurrence of a specified substring, raises ValueError if not found.
- rjust(): Returns a right-justified string of a specified width.
- rpartition(): Splits the string into three parts using the last occurrence of a specified separator.
- rsplit(): Splits the string into a list using a specified separator, starting from the right.
- rstrip(): Removes trailing characters (default is whitespace) from the string.
- split(): Splits the string into a list using a specified separator.
- splitlines(): Splits the string into a list at line breaks.
- startswith(): Returns True if the string starts with the specified prefix.
- strip(): Removes leading and trailing characters (default is whitespace) from the string.
- swapcase(): Converts uppercase characters to lowercase and vice versa.
- title(): Converts the string to title case.
- translate(): Returns a string where specified characters are replaced using a translation table.
- upper(): Converts all characters in the string to uppercase.
- zfill(): Pads the string with zeros on the left to reach a specified width.

Built-in Functions and Operations:
- str(): A built-in function to create a string. It can be used to convert other data types to strings.
- len(): A built-in function to get the number of characters in the string.
- in: A membership operator to check if a substring exists in the string.
- not in: A membership operator to check if a substring does not exist in the string.
- ord(): Returns the Unicode code point of a specified character.
- chr(): Returns the character corresponding to a specified Unicode code point.
- ascii(): Returns a string containing a printable representation of an object, escaping non-ASCII characters.
- repr(): Returns a string containing a printable representation of an object.
- format(): Formats a string using placeholders and specified values.
- bytes(): Converts the string to a bytes object using a specified encoding.
- enumerate(): Returns an enumerate object containing index-value pairs for the string.

Additional Notes:
- String concatenation: Use the `+` operator to concatenate two or more strings.
    Example:
    ```python
    str1 = "Hello"
    str2 = "World"
    print(str1 + " " + str2)  # Output: "Hello World"
    ```
- String repetition: Use the `*` operator to repeat a string a specified number of times.
    Example:
    ```python
    my_string = "Hi"
    print(my_string * 3)  # Output: "HiHiHi"
    ```
- String slicing: Use slicing to access a subset of characters in a string.
    Example:
    ```python
    my_string = "Hello"
    print(my_string[1:4])  # Output: "ell"
    ```
- String immutability: Strings are immutable, meaning their characters cannot be changed after creation.
    Example:
    ```python
    my_string = "Hello"
    # my_string[0] = "h"  # This will raise a TypeError
    ```
- String formatting: Use f-strings, `format()`, or `%` for string interpolation.
    Example:
    ```python
    name = "Alice"
    age = 25
    print(f"My name is {name} and I am {age} years old.")  # Output: "My name is Alice and I am 25 years old."
    ```
"""