def find_outlier(integers):
    # decide if list is odd or even
    d = 0
    for i in integers[:3]:
        d += i%2
    if d >= 2: # odd list
        for i in integers:
            if i%2 == 0:
                return i
    else:
        for i in integers:
            if i%2 == 1:
                return i

print(find_outlier([2,6,8,10,3]))

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
