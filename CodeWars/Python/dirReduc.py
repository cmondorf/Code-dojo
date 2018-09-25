# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python


def dirReduc(arr):
    direction_dictionary = {'North': 0, 'East': 0,  'South': 0, 'West': 0}
    for i in arr:
        direction_dictionary[i] += 1

    directions = []
    if (direction_dictionary['North'] - direction_dictionary['South']) > 0:
        directions[0] = 'N'
