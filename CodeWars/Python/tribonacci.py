# https://www.codewars.com/kata/tribonacci-sequence/train/python

def tribonacci(signature,n):
    # handle edge cases
    i = 0 # count number of repetitions

    if n == 0:
        return []

    if n < 3:
        addition = 0
        while i < n:
            addition += signature[i]
            i += 1
        return [addition]


    if n == 3:
        addition = 0
        while i < n:
            addition += signature[i]
            i += 1
        return signature.append(addition)

    while i < n-3: #repeat until you reach n
        signature.append(signature[-1] + signature[-2] + signature[-3])
        i += 1
    return signature

print(tribonacci([1,1,1],0))
