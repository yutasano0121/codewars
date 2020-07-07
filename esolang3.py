def interpreter(code, iterations, width, height):
    grid = [[0] * width for x in range(height)]
    w = 0
    h = 0  # height and width
    count = 0
    valid_chars = ['n', 'e', 's', 'w', '*', '[', ']']
    operation = {
        'n': [-1, 0],
        'e': [0, 1],
        's': [1, 0],
        'w': [0, -1]
    }
    slide = 0  # activate when bracket is present
    skip = False
    for i in range(len(code)):
        if count < iterations:
            cursor = i - slide
            char = code[cursor]
            if not skip:
                if not char in valid_chars:
                    continue
                elif char == '[':
                    bracket_loc = i
                    if grid[h][w] == 0:
                        skip = True
                    count += 1
                elif char == ']':
                    if grid[h][w] == 1:
                        slide = i - bracket_loc
                    count += 1
                elif char == "*":
                    if grid[h][w] == 1:
                        grid[h][w] = 0
                    else:
                        grid[h][w] = 1
                    count += 1

                else:
                    move = operation[char]
                    w = (w + move[1]) % width
                    h = (h + move[0]) % height
                    count += 1
            else:
                if char == "]":
                    skip = False
    out = '\r\n'.join(
        [''.join([str(i) for i in grid[j]]) for j in range(len(grid))]
    )
    return out

out = interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9)
print(out)


def interpreter_answer(code, iterations, width, height):
    code = "".join(c for c in code if c in "[news]*")
    canvas = [ [0] * width for _ in range(height) ]
    row = col = step = count = loop = 0

    while step < len(code) and count < iterations:
        command = code[step]

        if loop:
            if   command == "[": loop += 1
            elif command == "]": loop -= 1

        elif command == "n": row = (row - 1) % height
        elif command == "s": row = (row + 1) % height
        elif command == "w": col = (col - 1) % width
        elif command == "e": col = (col + 1) % width
        elif command == "*": canvas[row][col] ^= 1
        elif command == "[" and canvas[row][col] == 0: loop += 1
        elif command == "]" and canvas[row][col] != 0: loop -= 1

        step += 1 if not loop else loop // abs(loop)
        count += 1 if not loop else 0

    return "\r\n".join("".join(map(str, row)) for row in canvas)
