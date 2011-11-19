"""Generates dubstep lyrics."""


import re


ALPHA_RE = re.compile('[a-zA-Z]')
SUFFIXES = ['ah', 'oh', 'oom', 'uh', 'eh', 'op', 'ueh', 'um', 'roow', 'omp']

# This is in-memory storage for previously computed lyrics
LYRICS_BY_TENANT = {}


class DeterministicDubstep(object):
  def __init__(self, options, suffixes=None):
    if suffixes is not None:
      self.suffixes = suffixes
    else:
      self.suffixes = SUFFIXES

  def generate(self, tenant_id, text):
    """Deterministically converts a body of text to dubstep lyrics"""
    output = []
    prev = text[len(text) - 1]

    for char in [char for char in text if ALPHA_RE.search(char)]:
      womp = self._char_to_womp(prev, char)
      multiplier = (ord(prev) % 4) + 2
      line = " ".join([womp] * multiplier)
      output.append(line)
      output.append(line)

      prev = char

    # persist the computed lyrics so they can be played back
    LYRICS_BY_TENANT[tenant_id] = "\n".join(output)

    return LYRICS_BY_TENANT[tenant_id]

  def play(self, tenant_id):
    """Playback lyrics for the tenant in context"""
    return LYRICS_BY_TENANT[tenant_id]

  def _char_to_womp(self, entropy, char):
    """Converts a character to a word, based on entropy"""
    suffix = self.suffixes[ord(entropy) % len(self.suffixes)]
    suffix = suffix.upper() if char.upper() == char else suffix
    return str(char + suffix)
