import time

print("Printing current value, previous value, and the sum in a range(10)")
prev_num = 0

for i in range(1, 11):
    x_sum = prev_num + i
    print(f'Current Number {i} Previous Number {prev_num} Sum: {x_sum + prev_num}')
    prev_num = i
    time.sleep(1)
