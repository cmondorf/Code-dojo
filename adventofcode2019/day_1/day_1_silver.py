import math


def fuel_calc(mass):
    return math.floor(mass / 3) - 2

fuel_sum = 0
with open('input.txt', 'r') as masses_file:
    line = masses_file.readline()
    while line:
        mass = int(line)
        #print(f'line mass: {mass}')
        while mass > 0:
            fuel = fuel_calc(mass)
            #print(f'fuel: {fuel}')
            if fuel > 0:
                fuel_sum += fuel
            mass = fuel
        line = masses_file.readline()
print(fuel_sum)

