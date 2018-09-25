# loop through numbers 1 through 20
# if number is 4 or 13 -> print "x is unlucky"
# if number is even -> print "x is even"
# in number is odd -> print "x is odd"


for x in range(21):
    # parity = ""
    luck = ""
    if x % 2 == 0:
        luck = f"{x} is even"
    if x % 2 != 0:
        luck = f"{x} is odd"
    if x == 4 or x == 13:
        luck = f"{x} is unlucky"

    print(luck)
