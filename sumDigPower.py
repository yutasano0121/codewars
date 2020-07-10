"""
The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared). Eighty one (81), is the first number in having this property (not considering numbers of one digit). The next one, is 512. Let's see both cases with the details

8 + 1 = 9 and 92 = 81

512 = 5 + 1 + 2 = 8 and 83 = 512

We need to make a function, power_sumDigTerm(), that receives a number n and may output the n-th term of this sequence of numbers. The cases we presented above means that

power_sumDigTerm(1) == 81

power_sumDigTerm(2) == 512

Happy coding!
"""


def power_sumDigTerm(n):
    #your code here
    count = 0
    num = 81
    while num:
        sumDig = sum([int(i) for i in str(num)])
        if sumDig in (0, 1):
            num += 1
        else:
            num_sub = num
            while num_sub % sumDig == 0:
                num_sub = num_sub / sumDig
            if num_sub == 1:
                count += 1
                if count == n:
                    return num
            num += 1

# Return a runtime error when big numbers are fed.


# model answer
series = [0]
for a in range(2, 99):
    for b in range(2, 42):
        c = a**b
        if a == sum(map(int, str(c))):
            series.append(c)
power_sumDigTerm = sorted(series).__getitem__
