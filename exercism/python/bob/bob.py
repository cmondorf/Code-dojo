def hey(phrase):

    if len(phrase.replace(" ", "")) == 0 or phrase.strip() == 0:
        return "Fine. Be that way!"
    elif phrase[-1] == "?" and phrase.isupper():
        return "Calm down, I know what I'm doing!"
    elif phrase.strip()[-1] == "?":
        return "Sure."
    elif phrase.isupper():
        return "Whoa, chill out!"
    return "Whatever."
