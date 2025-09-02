import math
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1, number):
        if number % i == 0:
            aliquot += i
    if number == aliquot:
        return "perfect"
    if number < aliquot:
        return "abundant"
    if number > aliquot:
        return "deficient"