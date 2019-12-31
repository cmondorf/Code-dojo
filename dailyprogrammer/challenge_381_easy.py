
def yahtzee_upper(dice):
    results = List()
    for i in range(1, 7):
        results[i-1] = sum(dice)
        print(i)



yahtzee_upper([2, 3, 5, 5, 6]) #=> 10
yahtzee_upper([1, 1, 1, 1, 3]) #=> 4
yahtzee_upper([1, 1, 1, 3, 3]) #=> 6
yahtzee_upper([1, 2, 3, 4, 5]) #=> 5
yahtzee_upper([6, 6, 6, 6, 6]) #=> 30