import numpy as np


def test(n, start_index=0):
    if start_index == 0:
        global a
        a = np.zeros((n, n))
    start = start_index
    end = start + n - 1  # index

    if n == 1:
        a[start, start] = 1
    elif n == 2:
        a[start, start:end + 1] = 1
        a[end, end] = 1
    elif n == 3:
        a[start, start:end + 1] = 1
        a[start:end + 1, end] = 1  # right
        a[end, start:end + 1] = 1  # bottom
    elif n == 4:
        a[start, start:end + 1] = 1
        a[start:end + 1, end] = 1  # right
        a[end, start:end + 1] = 1  # bottom
        a[start + 2, start] = 1  # left
    else:
        a[start, start:end + 1] = 1  # top
        a[start + 2:end + 1, start] = 1  # left
        a[start:end + 1, end] = 1  # right
        a[end, start:end + 1] = 1  # bottom
        a[start + 2, start + 1] = 1
        test(n - 4, start + 2)

    return a

print(test(13))
