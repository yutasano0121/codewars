"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
"""

import re

def mix(str1, str2):
    lower_dict = {}
    ids = ['1', '2', '=']

    # make a dict{letter: (count, id)}
    for i in (0, 1):
        str = (str1, str2)[i]
        lowers = re.findall(r'[a-z]', str)
        lower_set = set(lowers)

        for c in lower_set:
            if lowers.count(c) > 1:
                try:
                    if lowers.count(c) > lower_dict[c][0]:
                        lower_dict[c] = (lowers.count(c), i)  # replace
                    elif lowers.count(c) == lower_dict[c][0]:
                        lower_dict[c] = (lowers.count(c), 2)  # '='
                except:
                    lower_dict[c] = (lowers.count(c), i)


    # reverse the dict to dict{count: (letter, id)}
    dict_rev = {}
    for key in lower_dict:
        c = lower_dict[key][0]
        id = lower_dict[key][1]
        try:
            dict_rev[c][key] = id  # if dict has 'c' entry
        except:
            dict_rev[c] = {key: id}

    out = []

    for num in dict_rev:
        out_sub = []
        for c in dict_rev[num]:
            out_sub.append('{}:{}'.format(ids[dict_rev[num][c]], c * num))
        out_sub.sort()
        out.append((num, out_sub))
    out.sort(reverse=True)
    out = [j for i in out for j in i[1]]
    print(out)
    out = '/'.join(out)
    return(out)

print(mix("Are they here", "yes, they are here"))



def mix_answer1(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))


from collections import Counter

def mix_answer2(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1.keys() + c2.keys()):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))
