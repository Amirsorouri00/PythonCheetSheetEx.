# Dictionaries are indexed by keys, which can be any immutable type; strings and numbers 
# can always be keys. Tuples can be used as keys if they contain only strings, numbers, 
# or tuples; if a tuple contains any mutable object either directly or indirectly, it 
# cannot be used as a key. You can’t use lists as keys, since lists can be modified 
# in place using index assignments, slice assignments, or methods like append() and extend().

# 1
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# 2
{x: x**2 for x in (2, 4, 6)}
dict(sape=4139, guido=4127, jack=4098)

