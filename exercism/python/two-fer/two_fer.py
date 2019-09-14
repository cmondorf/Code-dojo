def two_fer(name=None):
    if name != None or name == 'you':
        return "One for " + name + ", one for me."
    elif name == None:
        return "One for you, one for me."

    pass
print('running')