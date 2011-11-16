"""Generates dubstep lyrics."""

import re


ALPHA_RE = re.compile('[a-zA-Z]')
SUFFIXES = ['ah', 'oh', 'oom', 'uh', 'eh', 'op', 'ueh', 'um', 'roow', 'omp']


def dubstuppify(text):
    prev = text[len(text) - 1]

    for char in [char for char in text if ALPHA_RE.search(char)]:
        suffix = SUFFIXES[ord(prev) % len(SUFFIXES)]
        suffix = suffix.upper() if char.upper() == char else suffix
        multiplier = (ord(prev) % 4) + 2
        line = " ".join([str(char + suffix)] * multiplier)
        print "\n".join([line] * 2)
        print

        prev = char


if __name__ == '__main__':
    dubstuppify(locals()['__doc__'])
