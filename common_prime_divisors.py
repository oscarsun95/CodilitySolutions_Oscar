def gcd(a, b):
    if b % a == 0:
        return a
    else:
        return gcd(b%a, a)

def check(a, b):
    while a != 1:
        d = gcd(a, b)
        if d == 1:
            break
        a = a // d
    return a

def has_common_divisor(a, b):
    d = gcd(a, b)
    if (check(a, d) == 1) and (check(b, d) == 1):
        return True
    else:
        return False



def solution(A, B):
    # write your code in Python 3.6
    count = 0
    for a, b in zip(A, B):
        # if not is_prime(b):
        if has_common_divisor(a, b):
            count += 1
    return count