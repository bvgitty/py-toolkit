"""Run with: python -m toolkit "some text here" """
import sys

from toolkit.textstats import char_count, top_words, word_count

if len(sys.argv) < 2:
    print('Usage: python -m toolkit "your text"')
    sys.exit(1)

text = " ".join(sys.argv[1:])
print(f"Words:      {word_count(text)}")
print(f"Characters: {char_count(text)}")
print(f"Top words:  {top_words(text)}")
