"""Generates dubstep lyrics."""


import re


ALPHA_RE = re.compile('[a-zA-Z]')
SUFFIXES = ['ah', 'oh', 'oom', 'uh', 'eh', 'op', 'ueh', 'um', 'roow', 'omp']


class DeterministicDubstep(object):
  def __init__(self, options, suffixes=None):
    if suffixes is not None:
      self.suffixes = suffixes
    else:
      self.suffixes = SUFFIXES

  def generate(self, text):
    """Deterministically converts a body of text to dubstep lyrics"""
    output = []
    prev = text[len(text) - 1]

    for char in [char for char in text if ALPHA_RE.search(char)]:
      womp = self.char_to_womp(prev, char)
      multiplier = (ord(prev) % 4) + 2
      line = " ".join([womp] * multiplier)
      output.append(line)
      output.append(line)

      prev = char

    return "\n".join(output)

  def char_to_womp(self, entropy, char):
    """Converts a character to a word, based on entropy"""
    suffix = self.suffixes[ord(entropy) % len(self.suffixes)]
    suffix = suffix.upper() if char.upper() == char else suffix
    return str(char + suffix)
