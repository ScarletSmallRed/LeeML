def max_cutting(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    
    max = 0
    for i in range(1, (length // 2) + 1):
        product = max_cutting(i) * max_cutting(length - i)
        if product > max:
            max = product
    return max

print(max_cutting(4))