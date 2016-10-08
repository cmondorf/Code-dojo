
def alphabet_position(text):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    counter = 0
    solution = ""
    for letter in text:
        if letter in alphabet:
            solution += str(alphabet.index(letter)+1) + " "
    solution = solution[:-1] # remove final trailing space
    return solution


print(alphabet_position("HHELLO"))
