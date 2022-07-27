def prime(n):
    if n < 2:
        return False
    if n==2 or n==3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0:
            return False
        if (i+2)<=n and  n%(i+2) == 0:
            return False
        i+=6
    return True


def prime_greater_than(n):
    if n<2:
        return 2
    if n==2:
        return 3
    if n==3:
        return 5
    i = n//6
    p = i*6
    if p+1>n and prime(p+1):
        return p+1
    p+=6
    if p-1<=n:
        if prime(p+1):
            return p+1
        p+=6

    while True:
        if prime(p-1):
            return p-1
        elif prime(p+1):
            return p+1
        p += 6
