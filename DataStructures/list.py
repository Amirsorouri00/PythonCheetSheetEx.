# 1
print([(x, y) for x in [1,2,3] for y in [3,1,4,5] if x != y])

#2
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
fruits.append('grape')
fruits.sort()
fruits.pop()

#3
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[x for x in vec if x >= 0]
[(x, x**2) for x in range(6)]
[abs(x) for x in vec]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

#4 
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
#transpose rows and columns
[[row[i] for row in matrix] for i in range(4)]

list(zip(*matrix))

#5 del
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]
del a
