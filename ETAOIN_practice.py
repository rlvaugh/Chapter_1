"""Map letters from string into dictionary & print histogram of frequency."""

import sys
import pprint
from collections import defaultdict

# Note: text should be only a sentence or 2 for histogram to fit in IDLE window
text = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# defaultdict module lets caller specify a default if a
# value doesn't exist when the container is initialized
mapped = defaultdict(list)

for letter in ALPHABET:
    for character in text:
        if character.lower() == letter.lower():
            mapped[letter].append(character)

# pprint lets you print stacked output
print()
print("You may need to stretch your console window if text wrapping occurs.\n")
print("text = ", end='')
print("{}".format(text), file=sys.stderr)
print()
pprint.pprint(mapped, width=110)

