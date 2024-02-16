nmbrs = input('Enter a list of numbers separated by a comma: ')
nmbrList = nmbrs.split(",")

def compare_split():
    if nmbrList[0] == nmbrList[-1]:
        print('This is true')
    else:
        print('This is false')

compare_split()
