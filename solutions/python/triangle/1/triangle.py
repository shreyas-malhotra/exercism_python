def equilateral(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a == b == b:
        return True
    return False

def isosceles(sides):
    a, b, c = sides
    if a == b or b == c or a ==c:
        if a + b > c and a + c > b and b + c > a:
            return True
    return False

def scalene(sides):
    a, b, c = sides
    if a != b and a != c and b != c:
        if a + b > c and a + c > b and b + c > a:
            return True
    return False