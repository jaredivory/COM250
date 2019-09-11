import math;
# Or you can do from math import sqrt to grab a specific method


# NOTE! Python does not use semicolons nor does it use brackets!
a = 3
b = 2
print(a + b)

# to get the last variable on the stack use underscore in idle, '_'

# You can use either double or single quotes to define string
mm = "The moose is blue."
mm = 'The rain in spain is green on tuesday.'
print(mm)

nn = "Pluto is a 'dwarf' planet."
# Or
nn = 'Pluto is a "dwarf" planet'

# To define a list you use []
list = []
print(list)

# Lists can take any type into the same list
list2 = ['String', 64, 42.0] # Valid list

words = mm.split(" ", ) # Returns a list with split regex selector
print(words)

for i in mm:
    print( i, end="|")
print('\n')
'''
This is a multi-line comment
'''

# To do a standard for loop
# i.e. (int i = 1; i < 10; i++)
for i in range(1, 10):
    print (i, end=' ')

print('\n')

list +=['1', 2, 3.0]
print(list)

# You can use insert to put a object into the list at a position
list.insert(1, 1.5)
print(list)

for i in list:
    print(type(i))

