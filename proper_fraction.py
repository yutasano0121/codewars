from math import sqrt
def proper_fractions(n):
    if n <= 1:
        return 0

    def find_prime_factors(i):
        p = []
        p_add = p.append
        if i % 2 == 0:  # if even
            p_add(2)
            while i % 2 == 0:
                i = i / 2
        if i == 1:
            return p
        for j in range(3, round(sqrt(i)) + 1, 2):
            if i % j == 0:
                p_add(j)
                while i % j == 0:
                    i = i / j
        if i > 2:
            p_add(i)
        return p
    p = find_prime_factors(n)
    if n % 2 == 0:
        d = [i for i in range(1, n, 2) if sum(map(lambda x: i % x == 0, p)) == 0]
    else:
        d = [i for i in range(1, n) if sum(map(lambda x: i % x == 0, p)) == 0]

    return(len(d))
    #your code here
print(proper_fractions(15))
# returns RTE


def proper_fractions_answer(n):
    phi = n > 1 and n  # assign n if condition else assign False
    for p in range(2, int(n ** .5) + 1):  # ** .5 equals sqrt()
        if not n % p:  # if n % p == 0
            phi -= phi // p
            while not n % p:
                n //= p
    if n > 1:
        phi -= phi // n
    return phi

# Euler's totient formula?
