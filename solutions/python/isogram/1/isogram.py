def is_isogram(string):
    stripped_hyphen = string.replace('-','').replace(' ','')
    stripped = stripped_hyphen.strip()
    lowered_stripped = stripped.lower()
    return len(set(lowered_stripped)) == len(lowered_stripped)