def is_triangle(a, b, c):
    if (a < (b + c)) and (a > abs(b-c)):
        return True
    return False
