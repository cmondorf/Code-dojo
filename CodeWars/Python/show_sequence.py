# https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/python

def show_sequence(n):
    if n == 0:
        return "0=0"
    if n < 0:
        return str(n) + "<0"
    i = 0
    sums = ""
    sum_result = 0
    while i <= n:
        sum_result += i
        sums += str(i) + "+"
        i += 1
    sums = sums[:-1] + " = " + str(sum_result)
    return sums
