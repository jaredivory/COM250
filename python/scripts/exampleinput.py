# ... student evaluation time
name = input('Who is the best teacher?? ')
print('I agree', name)

num1 = input('What is the first number? ')
num2 = input('What is the last number? ')

# it is necessary to convert the string input into an integer
# We can cast the string to an integer using int()
nn1 = int(num1)
nn2 = int(num2)

for i in range(nn1, nn2):
    print(i, end=" ")
