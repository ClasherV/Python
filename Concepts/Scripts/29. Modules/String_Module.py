print(help("string"))

"""
O/p: Help on module string:
     
     NAME
         string - A collection of string constants.
     
     MODULE REFERENCE
         https://docs.python.org/3.12/library/string.html
     
         The following documentation is automatically generated from the Python
         source files.  It may be incomplete, incorrect or include features that
         are considered implementation detail and may vary between Python
         implementations.  When in doubt, consult the module reference at the
         location listed above.
     
     DESCRIPTION
         Public module variables:
     
         whitespace -- a string containing all ASCII whitespace
         ascii_lowercase -- a string containing all ASCII lowercase letters
         ascii_uppercase -- a string containing all ASCII uppercase letters
         ascii_letters -- a string containing all ASCII letters
         digits -- a string containing all ASCII decimal digits
         hexdigits -- a string containing all ASCII hexadecimal digits
         octdigits -- a string containing all ASCII octal digits
         punctuation -- a string containing all ASCII punctuation characters
         printable -- a string containing all ASCII characters considered printable
     
     CLASSES
         builtins.object
             Formatter
             Template
     
         class Formatter(builtins.object)
          |  Methods defined here:
          |
          |  check_unused_args(self, used_args, args, kwargs)
          |
          |  convert_field(self, value, conversion)
          |
          |  format(self, format_string, /, *args, **kwargs)
          |
          |  format_field(self, value, format_spec)
          |
          |  get_field(self, field_name, args, kwargs)
          |      # given a field_name, find the object it references.
          |      #  field_name:   the field being looked up, e.g. "0.name"
          |      #                 or "lookup[3]"
          |      #  used_args:    a set of which args have been used
          |      #  args, kwargs: as passed in to vformat
          |
          |  get_value(self, key, args, kwargs)
          |
          |  parse(self, format_string)
          |      # returns an iterable that contains tuples of the form:
          |      # (literal_text, field_name, format_spec, conversion)
          |      # literal_text can be zero length
          |      # field_name can be None, in which case there's no
          |      #  object to format and output
          |      # if field_name is not None, it is looked up, formatted
          |      #  with format_spec and conversion and then used
          |
          |  vformat(self, format_string, args, kwargs)
          |
          |  ----------------------------------------------------------------------
          |  Data descriptors defined here:
          |
          |  __dict__
          |      dictionary for instance variables
          |
          |  __weakref__
          |      list of weak references to the object
     
         class Template(builtins.object)
          |  Template(template)
          |
          |  A string class for supporting $-substitutions.
          |
          |  Methods defined here:
          |
          |  __init__(self, template)
          |      Initialize self.  See help(type(self)) for accurate signature.
          |
          |  get_identifiers(self)
          |
          |  is_valid(self)
          |
          |  safe_substitute(self, mapping={}, /, **kws)
          |
          |  substitute(self, mapping={}, /, **kws)
          |
          |  ----------------------------------------------------------------------
          |  Class methods defined here:
          |
          |  __init_subclass__()
          |      This method is called when a class is subclassed.
          |
          |      The default implementation does nothing. It may be
          |      overridden to extend subclasses.
          |
          |  ----------------------------------------------------------------------
          |  Data descriptors defined here:
          |
          |  __dict__
          |      dictionary for instance variables
          |
          |  __weakref__
          |      list of weak references to the object
          |
          |  ----------------------------------------------------------------------
          |  Data and other attributes defined here:
          |
          |  braceidpattern = None
          |
          |  delimiter = '$'
          |
          |  flags = re.IGNORECASE
          |
          |  idpattern = '(?a:[_a-z][_a-z0-9]*)'
          |
          |  pattern = re.compile('\n            \\$(?:\n              ...identifie...
     
     FUNCTIONS
         capwords(s, sep=None)
             capwords(s [,sep]) -> string
     
             Split the argument into words using split, capitalize each
             word using capitalize, and join the capitalized words using
             join.  If the optional second argument sep is absent or None,
             runs of whitespace characters are replaced by a single space
             and leading and trailing whitespace are removed, otherwise
             sep is used to split and join the words.
     
     DATA
         __all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
         ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
         ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
         ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
         digits = '0123456789'
         hexdigits = '0123456789abcdefABCDEF'
         octdigits = '01234567'
         printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
         punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
         whitespace = ' \t\n\r\x0b\x0c'
     
     FILE
         d:\programming\python\python\interpreter\lib\string.py
     
     
     None
"""