def solution(number):
    multiples = []
    for i in range(1, number):
        if i%3 == 0 or i%5 == 0:
            if i not in multiples:
                multiples.append(i)
    return sum(multiples)


print(solution(10))
