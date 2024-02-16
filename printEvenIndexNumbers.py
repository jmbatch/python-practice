userInput = input('Please enter a string: ')
print(f'The original word is {userInput}')

x = list(userInput)
print(x)

for i in x[0::2]:
    print(i)
