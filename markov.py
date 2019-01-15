"""
This is the source code for Markov Chains.

This is a doc-string because it is a string at
the top of the file.

>>> m = Markov('ab')
>>> m.predict('a') # What character should follow 'a'?
'b'

"""
import random

class Markov:
    def __init__(self, data):
        ''' This is the constructor '''
        self.table = get_table(data)

    def predict(self, txt):
        options = self.table.get(txt, {})    
        if not options:
            raise KeyError(f'{txt} not found')

        possibles = []
        for key, count in options.items():
            for i in range(count):
                possibles.append(key)
        return random.choice(possibles)


def get_table(txt):
    """
    Returns a transition table for txt

    >>> get_table('ab')
    {'a': {'b': 1 }}
    """

    results = {}
    for idx in range(len(txt)):
        char = txt[idx]

        try:
            out = txt[idx + 1]
        except IndexError:
            break

        # These lines are replaced by the three lines below these blocks
        # if char in results:
        #     char_dict = results[char]
        # else:
        #     char_dict = {}

        # if out in char_dict:
        #     char_dict[out] += 1
        # else:
        #     char_dict[out] = 1

        char_dict = results.get(char, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[char] = char_dict
    return results
