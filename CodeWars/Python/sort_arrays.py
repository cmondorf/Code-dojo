def get_length_of_missing_array(array_of_arrays):
    total_lengths = []
    for i in array_of_arrays:
        total_lengths += len(i)
    for i in total_lengths:
        if i





test_array = [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]

print(get_length_of_missing_array(test_array))


# what if the first or last value is missing?
# how to handle empty lists?
