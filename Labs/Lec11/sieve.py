# Sieve of Eratosthenes

def getprimes(n):

    L = list(range(n+1))
    p = 2

    while p**2 <= n:
        for m in range(p, n//p+1):
            L[m*p] = 0
        q = p + 1
        while (q <= n) and (L[q] == 0):
            q = q + 1
        if q <= n:
            p = q
        else:
            break

    return list(filter(lambda x: x > 0, L))
