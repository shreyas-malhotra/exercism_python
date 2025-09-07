def rotate(text, key):
    encrypted_text = ''
    for i in range(len(text)):
        if text[i].isalpha() and text[i].islower():
            encrypted_text += chr(((ord(text[i]) - ord('a') + key) % 26) + ord('a'))
        elif text[i].isalpha() and text[i].isupper():
            encrypted_text += chr(((ord(text[i]) - ord('A') + key) % 26) + ord('A'))
        else:
            encrypted_text += text[i]
    return encrypted_text