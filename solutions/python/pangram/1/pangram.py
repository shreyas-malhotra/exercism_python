def is_pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    stripped = sentence.strip()
    stripped_and_lowered = stripped.lower()
    if stripped_and_lowered == '':
        return False
    if set(alphabets).issubset(set(stripped_and_lowered)):
        return True
    return False