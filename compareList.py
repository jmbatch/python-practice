def array_diff(a, b):
    d = []
    for i in a:
        if i not in b:
            d.append(i)
    print(d)

array_diff([1,2], [1])
array_diff([1,2,2], [1])
array_diff([1,2,2], [2])
array_diff([1,2,2], [])
array_diff([], [1,2])
array_diff([1,2,3], [1, 2])