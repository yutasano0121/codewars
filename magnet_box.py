"""
Professor Chambouliard hast just discovered a new type of magnet material. He put particles of this material in a box made of small boxes arranged in K rows and N columns as a kind of 2D matrix K x N where K and N are postive integers. He thinks that his calculations show that the force exerted by the particle in the small box (k, n) is:

v(k, n) = \frac{1}{k(n+1)^{2k}}

The total force exerted by the first row with k = 1 is:

u(1, N) = \sum_{n=1}^{n=N}v(1, n) = \frac{1}{1.2^2} + \frac{1}{1.3^2}+...+\frac{1}{1.(N+1)^2}

We can go on with k = 2 and then k = 3 etc ... and consider:

S(K, N) = \sum_{k=1}^{k=K}u(k, N) = \sum_{k=1}^{k=K}(\sum_{n=1}^{n=N}v(k, n)) \rightarrow (doubles(maxk, maxn))

Task:
To help Professor Chambouliard can we calculate the function doubles that will take as parameter maxk and maxn such that doubles(maxk, maxn) = S(maxk, maxn)? Experiences seems to show that this could be something around 0.7 when maxk and maxn are big enough.

Examples:
doubles(1, 3)  => 0.4236111111111111
doubles(1, 10) => 0.5580321939764581
doubles(10, 100) => 0.6832948559787737
Notes:
In u(1, N) the dot is the multiplication operator.

Don't truncate or round: Have a look in "RUN EXAMPLES" at "assertFuzzyEquals".
"""

def assertFuzzyEquals(actual, expected, msg=""):
    merr = 1e-6
    inrange = abs(actual - expected) <= merr
    if (inrange == False):
        msg = "At 1e-6: Expected value must be {:0.6f} but got {:0.6f}"
        msg = msg.format(expected, actual)
    return Test.expect(inrange, msg)



def doubles(maxk, maxn):
    out = 0
    for k in range(1, maxk + 1):
        for n in range(1, maxn + 1):
            out_add = 1 / (k * ((n + 1) ** (2 * k)))
        if out_add < 1e-100:  # without this causes RTE
            return out
        out += out_add
    return out
    # your code

print(doubles(1, 100000))


def doubles_answer(maxk, maxn):
    out = sum([
        sum([
            (n+1)**(-2*k) for n in range(1, maxn+1)
        ]) / k for k in range(1, maxk+1)
    ])  # sum and inline list seems much faster than nested for loops
