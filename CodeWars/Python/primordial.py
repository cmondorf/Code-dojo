def check_primality(num_list, candidate):
    if len(num_list) == 0:
        return True
    for num in num_list:
        if candidate % num == 0:
            return False
    return True

def num_primorial(n):
    #your code here
    i = 2
    num_list = []
    if len(num_list) == 0:
        num_list.append(i)
    while len(num_list) <= n -1:
        i += 1
        if check_primality(num_list, i):
            num_list.append(i)
    result = 1
    for num in num_list:
        result *= num
    return result                
        
            
        





print(num_primorial(3))
print(num_primorial(4))
