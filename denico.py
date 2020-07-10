"""
Task
Write a function deNico/de_nico() that accepts two parameters:

key/$key - string consists of unique letters and digits
message/$message - string with encoded message
and decodes the message using the key.

First create a numeric key basing on the provided key by assigning each letter position in which it is located after setting the letters from key in an alphabetical order.

For example, for the key crazy we will get 23154 because of acryz (sorted letters from the key).
Let's decode cseerntiofarmit on using our crazy key.

1 2 3 4 5
---------
c s e e r
n t i o f
a r m i t
  o n
After using the key:

2 3 1 5 4
---------
s e c r e
t i n f o
r m a t i
o n
Notes
The message is never shorter than the key.
Don't forget to remove trailing whitespace after decoding the message
Examples
deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
deNico("abc", "abcd") => "abcd"
deNico("ba", "2143658709") => "1234567890"
deNico("key", "eky") => "key"
"""


import numpy as np
import re
from math import floor

def de_nico(key,msg):
    key_len = len(key)
    msg_len = len(msg)
    chunk = []
    chunk_decode = []
    for i in range(floor(msg_len / key_len)):
        chunk.append(msg[i * key_len:(i + 1) * key_len])
    if msg_len % key_len != 0:
        chunk.append(msg[(i + 1) * key_len:])

    # fetch the order
    ord = np.argsort(np.argsort([i for i in key]))

    for w in chunk:
        for i in range(len(ord)):
            try:
                chunk_decode.append(w[ord[i]])  # if not out of range
            except:
                continue
        print(w)
        print(ord)
    out = ''.join(chunk_decode)
    out = re.search('(.*?)\s*$', out).group(1)  # remove trailing ' '
    return out



print(de_nico('fsmrpw', 'uvdvxlccwiyppremwbsbaq'))


def de_nico_answer(key, msg):
    ll = len(key)
    order = [sorted(key).index(c) for c in key]
    s = ''

    while msg:
        s = s + ''.join(msg[i] for i in order if i < len(msg))  # reorder a chunk
        msg = msg[ll:]  # move to the next chunk
    return s.strip()  # remove trailing ' '
