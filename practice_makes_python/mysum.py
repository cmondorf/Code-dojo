# mysum
# takes in any number of args and sums them
# basically an implementation of sum()


def mysum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(mysum(1, 2, 3))
