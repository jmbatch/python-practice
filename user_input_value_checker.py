while True:
    try:
        fname, lname = input('Please enter you first and last name: ').split(" ")
        print(f'Hello {fname} {lname}')
        break
    except:
        print('\nPlease enter a first and last name.\n')
        continue

def num():
    invalid_input = True
    while invalid_input == True:
        number = input('\nPlease enter your 10 digit phone number: \n')
        if len(number) > 10 or len(number) < 10:
            print('\nPlease enter a 10-Digit Number.\n')
            continue
        else:
            invalid_input == False
        break
    print(f'\nYour telephone number is +1{number}\n')

num()
