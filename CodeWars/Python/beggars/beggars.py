def beggars(values, n):
    #your code here
    beggars = [0] * n
    if len(beggars) == 0:
        return beggars
    beggar_tracker = 0
    for i in range(len(values)):
        if beggar_tracker == n:
            beggar_tracker = 0
        beggars[beggar_tracker] += values[i]
        beggar_tracker += 1
    return beggars

beggars([1,2,3,4,5],0)