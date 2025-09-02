def response(hey_bob):
    stripped_bob = hey_bob.strip()
    if stripped_bob == '':
        return "Fine. Be that way!"
    if stripped_bob[-1] == "?" and stripped_bob.isupper() == False:
        return "Sure."
    if stripped_bob[-1] != "?" and stripped_bob.isupper():
        return "Whoa, chill out!"
    if stripped_bob[-1] == "?" and stripped_bob.isupper():
        return "Calm down, I know what I'm doing!"
    else:
        return "Whatever."