class HippyEncryption:
    def __init__(self):
        self.encryption_tree = {1: "s", 2: "ox", 3: "hen", 4: "duck", 5: "chick", 6: "buffalo"}
        self.sample_plaintext = "haitim"
        self.sample_key = "jdilsm"
        self.division_factor = len(self.encryption_tree)

        self.alphabet_tree = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
                              'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                              'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    def encrypt_plain_text(self):
        key_sum = sum([self.alphabet_tree[letter] for letter in self.sample_key])
        plain_text_sum = sum([self.alphabet_tree[letter] for letter in self.sample_plaintext])
        system_key = self.encryption_tree[(key_sum + plain_text_sum) % self.division_factor]
