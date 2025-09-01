def is_armstrong_number(number):
    str_number = str(number)
    len_number = len(str_number)
    sum_of_power = 0
    for i in range(0,len_number):
        sum_of_power += int(str_number[i]) ** len_number
    if sum_of_power == number:
        return True
    return False
