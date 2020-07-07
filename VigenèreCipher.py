from math import ceil


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        text_len = len(text)
        pass_len = len(self.key)
        password2 = self.key * ceil(len(text) / len(self.key))

        new_word = []
        for i in range(len(text)):
            try:
                shifted = self.alphabet.index(text[i]) + self.alphabet.index(password2[i])
                shifted = shifted % len(self.alphabet)
                new_word.append(self.alphabet[shifted])
            except ValueError:
                new_word.append(text[i])
        return(''.join(new_word))

    def decode(self, text):
        text_len = len(text)
        pass_len = len(self.key)
        password2 = self.key * ceil(len(text) / len(self.key))

        new_word = []
        for i in range(len(text)):
            try:
                shifted = self.alphabet.index(text[i]) - self.alphabet.index(password2[i])
                shifted = shifted % len(self.alphabet)
                new_word.append(self.alphabet[shifted])
            except ValueError:
                new_word.append(text[i])
        return(''.join(new_word))
