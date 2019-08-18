# i = 99
# while True:
#     if int(str(i)[1]) == (i / 7):
#         print(str(i))
#         break
#     else:
#         i -= 1
i = 9999
while True:
    if int(str(i)[1:]) == (i / 57):
        print(str(i))
        break
    elif i == 10:
        print("10")
        break
    else:
        i -= 1
