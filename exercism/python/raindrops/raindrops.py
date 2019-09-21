#  has 3 as a factor, add 'Pling' to the result.
# - has 5 as a factor, add 'Plang' to the result.
# - has 7 as a factor, add 'Plong' to the result.
# - _does not_ have any of 3, 5, or 7 as a factor

def convert(number):
    return_string = ""
    if number % 3 == 0:
        return_string += 'Pling'
    if number % 5 == 0:
        return_string += 'Plang'
    if number % 7 == 0:
        return_string += 'Plong'
    if len(return_string) == 0:
        return_string = str(number)
    return return_string
