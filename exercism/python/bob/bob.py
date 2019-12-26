def hey(phrase):

    if len(phrase.replace(" ", "")) == 0 or len(phrase.strip()) == 0:
        return "Fine. Be that way!"
    elif phrase[-1] == "?" and phrase.isupper():
        return "Calm down, I know what I'm doing!"
    try:
        if phrase.strip()[-1] == "?":
            return "Sure."
    except:
        pass
    if phrase.isupper():
        return "Whoa, chill out!"
    return "Whatever."
