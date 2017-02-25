def square_or_square_root(arr):
    import math
    result = []
    for i in arr:
        if math.sqrt(i) % 1 == 0:
            result.append(math.sqrt(i))
        else:
            result.append(i**2)
    return result
