def funnel(word1, word2):
    # return True if word2 can be obtained by eliminating a single letter from
    # word1
    for i in range(len(word1)):
        copy = word1
        if (copy[:i] + copy[i+1:]) == word2:
            return True
    return False
    # this returns None when the last index is reached


print("true")
print(funnel("leave", "eave"))
print("false")
print(funnel("eave", "leave"))
print("false")
print(funnel("skiff", "ski"))
print("true")
print(funnel("skiff", "skif"))
