def dashatize(input):
    if input == None:
        return 'None'
    num = str(input)
    if num[0]=='-':
        num = num[1:]
    result = ''
    for i in range(len(num)):
        current = int(num[i])
        if current%2 == 0:
            result += str(current)
        if current%2 != 0:
            if i == 0:
                result += str(current) + "-"
            elif result[-1] == '-':
                result += str(current) + "-"
            else:
                result += "-" + str(current) + "-"
    if result[-1] == '-':
        result = result[:-1]           

    return result

            




print(dashatize(None))