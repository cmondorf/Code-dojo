def filter_list(l):
    'return a new list with the strings filtered out'
    return_list = []
    for i in l:
        if type(i) != str:
            return_list.append(i)
    return return_list


print(filter_list([1,2,'a','b']))
