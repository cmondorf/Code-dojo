# sum of positive array items
def positive_sum(arr):
    sum = 0
    for element in arr:
        if element > 0:
            sum += element
    return sum
