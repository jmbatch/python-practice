nmbrs = input('Input a list of numbers separated by a comma: ')
nmbrList = nmbrs.split(',')
intList = [eval(i) for i in nmbrList]
print(intList)

def divideFive(x):
    for i in x:
        if i % 5 == 0:
            print(i)

divideFive(intList)
