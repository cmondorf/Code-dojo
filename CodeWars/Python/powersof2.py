def powers_of_two(n):
    powers_of_two = list()
    counter = 0
    while counter <= n:
        powers_of_two.append(2**counter)
        counter += 1
    return powers_of_two


print powers_of_two(4)

# 
# def powers_of_two(n):
#     return [2**x for x in range(n+1)]
