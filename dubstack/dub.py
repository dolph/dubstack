"""Generates dubstep lyrics."""

import sys
import re


ALPHA_RE = re.compile('[a-zA-Z]')
SUFFIXES = ['ah', 'oh', 'oom', 'uh', 'eh', 'op', 'ueh', 'um', 'roow', 'omp']


def dubsteppify(text):
    """Deterministically converts a body of text to dubstep lyrics"""
    output = []
    prev = text[len(text) - 1]

    for char in [char for char in text if ALPHA_RE.search(char)]:
        womp = char_to_womp(prev, char)
        multiplier = (ord(prev) % 4) + 2
        line = " ".join([womp] * multiplier)
        output.append(line)
        output.append(line)

        prev = char

    return "\n".join(output)


def char_to_womp(entropy, char):
    """Converts a character to a word, based on entropy"""
    suffix = SUFFIXES[ord(entropy) % len(SUFFIXES)]
    suffix = suffix.upper() if char.upper() == char else suffix
    return str(char + suffix)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = locals()['__doc__']

    print dubsteppify(text)
