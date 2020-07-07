def justify(text, width):
    words = text.split()
    line = []
    lines = ''
    length = 0
    for i in range(len(words)):
        w = words[i]
        if line == []:  # first word in the line
            length += len(w)
            if length < width:
                line.append(w)
            else:  # long word
                lines = lines + w + '\n'
                length = 0
        else:
            length += len(w) + 1  # + 1 for a space
            if length < width:
                line.append(w)
            else:
                space = width - len(''.join(line))  # space to fill
                num_words = len(line)  # num of words in the line
                if num_words == 1:
                    lines = lines + line[0] + '\n'
                else:
                    num_space = [int(space / (num_words - 1))] * (num_words - 1)  # spaces per word
                    count = space % num_words
                    while count > 0:
                        for j in range(len(num_space)):
                            num_space[j] += 1
                            count -= 1
                    num_space += [0]  # make it the same length as num_words
                    for j in range(num_words):
                        lines = lines + line[j] + ' ' * num_space[j]
                    lines += '\n'

                length = len(w)
                if length < width:
                    line = [w]
                else:  # long word
                    lines = lines + w + '\n'
                    length = 0

        if i == len(words) - 1:  # last word
            lines += ' '.join(line)

    print(lines)
    return lines

justify('123 45 6', 7)


def justify_answer(text, width):
    length = text.rfind(' ', 0, width+1)
    if length == -1 or len(text) <= width:
        return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) / spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)
