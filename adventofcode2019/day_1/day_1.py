import math

fuel_sum = 0
with open('input.txt', 'r') as masses_file:
    line = masses_file.readline()
    while line:
        mass = int(line)
        fuel = math.floor(mass / 3) - 2
        fuel_sum += fuel
        line = masses_file.readline()
print(fuel_sum)

