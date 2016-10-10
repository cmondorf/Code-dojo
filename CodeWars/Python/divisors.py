def divisors(integer):
    currentDivisor = integer - 1
    divisorList = []
    while currentDivisor > 1:
        if integer%currentDivisor == 0:
            divisorList.append(currentDivisor)
        currentDivisor -= 1
    if len(divisorList) == 0:
        return str(integer) + " is prime"
    else:
        return sorted(divisorList)


print(divisors(15))

print(divisors(12))

print(divisors(13))
