"""
A natural number is called k-prime if it has exactly k prime factors, counted with multiplicity. For example:

k = 2  -->  4, 6, 9, 10, 14, 15, 21, 22, ...
k = 3  -->  8, 12, 18, 20, 27, 28, 30, ...
k = 5  -->  32, 48, 72, 80, 108, 112, ...
A natural number is thus prime if and only if it is 1-prime.

Task:
Complete the function count_Kprimes (or countKprimes, count-K-primes, kPrimes) which is given parameters k, start, end (or nd) and returns an array (or a list or a string depending on the language - see "Solution" and "Sample Tests") of the k-primes between start (inclusive) and end (inclusive).

Example:
countKprimes(5, 500, 600) --> [500, 520, 552, 567, 588, 592, 594]
Notes:

The first function would have been better named: findKprimes or kPrimes :-)
In C some helper functions are given (see declarations in 'Solution').
For Go: nil slice is expected when there are no k-primes between start and end.
Second Task (puzzle):
Given a positive integer s, find the total number of solutions of the equation a + b + c = s, where a is 1-prime, b is 3-prime, and c is 7-prime.

Call this function puzzle(s).

Examples:
puzzle(138)  -->  1  because [2 + 8 + 128] is the only solution
puzzle(143)  -->  2  because [3 + 12 + 128] and [7 + 8 + 128] are the solutions
"""


from math import sqrt

def count_Kprimes(k, start, end):
    def find_prime_num(i):
        if i == 0:
            return 0
        p = []
        p_add = p.append
        while i % 2 == 0:
            i = i / 2
            p_add(2)
        for j in range(3, int(sqrt(i) + 1), 2):
            while i % j == 0:
                i = i / j
                p_add(j)
        if i > 1:
            p_add(i)
        return len(p)
    return [i for i in range(start, end + 1) if find_prime_num(i) == k]


def puzzle(s):
    if s < 138:
        return 0
    count = 0
    prime7 = count_Kprimes(7, 128, s - 10)
    for i in prime7:
        prime3 = count_Kprimes(3, 8, s - i)
        for j in prime3:
            prime1 = count_Kprimes(1, s - i - j, s - i - j)
            if prime1 != []:
                count += 1
    return count
    # your code

print(puzzle(138))




def count_Kprimes_answer(k, start, end):
    return [n for n in range(start, end+1) if find_k(n) == k]


def puzzle_answer(s):
    a = count_Kprimes_answer(1, 0, s)
    b = count_Kprimes_answer(3, 0, s)
    c = count_Kprimes_answer(7, 0, s)

    return sum(1 for x in a for y in b for z in c if x + y + z == s)


def find_k(n):
    res = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            res += 1
        i += 1
    if n > 1: res += 1
    return res
