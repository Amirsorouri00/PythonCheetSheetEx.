# A tuple consists of a number of values separated by commas, for instance:
t = 12345, 54321, 'hello!'
print(t)
print(t[0])

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
# t[0] = 88888 #this gets runtime error

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

#2
# Constructing tuples containing 0 or 1 items
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)

len(singleton)


