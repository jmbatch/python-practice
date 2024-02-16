print('Input two numbers')
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
num3 = num1 * num2
x = 1000

def sumOrProd():
    if num3 <= x:
        print('The result is ', + num3)
    else:
        print('The result is ', num1 + num2)

sumOrProd()
