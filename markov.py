"""
This is the source code for Markov Chains.

This is a doc-string because it is a string at
the top of the file.

>>> m = Markov('ab')
>>> m.predict('a') # What character should follow 'a'?
'b'

"""
import random
import urllib.request as req

class Markov:
    def __init__(self, data, size=1):
        ''' This is the constructor '''
        # self.table = get_table(data)
        self.tables = []
        for i in range(size):
            self.tables.append(get_table(data, size=i+1))

    def predict(self, txt):
        # options = self.table.get(txt, {})
        table = self.tables[len(txt)-1]
        options = table.get(txt, {})
        if not options:
            raise KeyError(f'{txt} not found')

        possibles = []
        for key, count in options.items():
            for i in range(count):
                possibles.append(key)
        return random.choice(possibles)

def fetch_url(url, fname):
    fin = req.urlopen(url)
    data = fin.read()
    with open(fname, mode='wb') as fout:
        fout.write(data)
    # context mgr closes file

def get_table(txt, size=1):
    """
    Returns a transition table for txt

    >>> get_table('ab')
    {'a': {'b': 1 }}
    """

    results = {}
    for idx in range(len(txt)):
        chars = txt[idx:idx+size]

        try:
            out = txt[idx + size]
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

        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results

def from_file(fname, size=1):
    with open(fname) as fin:
        data = fin.read()
    m = Markov(data, size=size)
    return m

def repl(m):
    print('Welcome to the Markov REPL')
    while True:
        txt = input('>')
        try:
            result = m.predict(txt)
        except IndexError:
            print('Try again')
        except KeyError:
            print(f'"{txt}" not found')
        else:
            print(result)

if __name__ == '__main__':
    book = from_file('heart_of_darkness.txt', size=4)
    repl(book)
