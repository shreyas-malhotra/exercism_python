def is_valid(isbn):
    i = ''
    solve = 0
    int_stripped = []
    stripped = isbn.replace('-','').replace(' ','')
    len_stripped = len(stripped)
    if len_stripped != 10:
        return False
    for i in range(len_stripped):
        if i == (len_stripped - 1) and stripped[i] == 'X':
            int_stripped.append(10)
        elif str.isalpha(stripped[i]) == True:
            return False
        else:
            int_stripped.append(int(stripped[i]))
    for i in range(len(int_stripped)):
        solve += int_stripped[i] * (len(stripped) - i)
    if solve % 11 == 0:
        return True
    return False