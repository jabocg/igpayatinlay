#!/usr/bin/env python3.6
"""Translate things to Pig Latin or something."""


_VOWELS = 'a e i o u'.split()
_CONSONANTS = 'b c d f g h j k l m n p q r s t v w x y z'.split()
_CAPITALS = 'B C D F G H J K L M N P Q R S T Y V W X Y Z'.split()
_PUNCTUATION_MARKS = ', . : ! " ?'.split()


def _split_into_parts(string):
    first_vowel = -1
    punctuation = -1
    for i, c in enumerate(string):
        if c in _VOWELS and first_vowel == -1:
            first_vowel = i
        elif c in _PUNCTUATION_MARKS and punctuation == -1:
            punctuation = i
            break
    if first_vowel == -1:
        first_vowel = 0
    if punctuation == -1:
        punctuation = len(string)
    return (string[:first_vowel],
            string[first_vowel:punctuation],
            string[punctuation:])


class IgpayAtinlayAsephray:
    """Store a phrase to be retrieved as Pig Latin.

    Utilizes lazy translation.
    """

    def __init__(self, phrase=None):
        """Construct an IgpayAtinlay object.  """
        self.pig_phrase = None
        self.pig_words = []
        if phrase is None:
            self.words = []
        elif type(phrase) is list:
            self.words = phrase
        elif type(phrase) is str:
            self.words = phrase.split()

    def asay_ingstray(self):
        """Return a translated phrase as a string."""
        return str(self)

    def asay_ormalnay_ingstray(self):
        """Return an untranslated string."""
        return ' '.join(self.words)

    def asay_istlay(self):
        """Return a list of translated words."""
        if self.pig_phrase is None:
            self._set_pig_phrase()

        return self.pig_phrase.split()

    def _set_pig_phrase(self):
        """Set the internal pig phrase."""
        for i, word in enumerate(self.words):
            split_words = word.split()
            for j, v in enumerate(split_words):
                pre, rest, punc = _split_into_parts(v)
                if len(pre) > 0 and pre[0] in _CAPITALS:
                    pre = pre.lower()
                    rest = rest[0].upper() + rest[1:]
                if len(pre) == 0 and rest[-1] in _VOWELS:
                    suffix = 'say'
                else:
                    suffix = 'ay'
                split_words[j] = '{}{}{}{}'.format(rest, pre, suffix, punc)
            self.pig_words.append(' '.join(split_words))
        self.pig_phrase = ' '.join(self.pig_words)

    def __str__(self):
        """Return a string version of the Pig Latin phrase."""
        if self.pig_phrase is None:
            self._set_pig_phrase()

        return self.pig_phrase
