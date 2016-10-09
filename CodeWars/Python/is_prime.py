
def is_prime(num):
    num = abs(num)
    if num == 1:
        return False
    if num == 0:
        return False
    if num == 2:
        return True
    i = num - 1
    while i > 1:
        if num%i == 0:
            return False
        i -= 1
    return True


print(is_prime(0))

print(is_prime(1))

print(is_prime(2))

print(is_prime(3))

print(is_prime(4))
