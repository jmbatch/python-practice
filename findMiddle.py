def narcissistic(value):
    sum = 0
    digits = len(value)
    for i in value:
        sum = sum + int(i) ** digits
    number = int(value)
    if number == sum:
        return True
    else:
        return False


print(narcissistic(153))
