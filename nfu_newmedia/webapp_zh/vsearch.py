# -*- coding: utf-8 -*-

def search4prepositions_zhs(phrase: str) -> set:
    """Return any prepositions found in a supplied phrase."""
    # Source http://xh.5156edu.com/page/z3033m4876j18636.html
    # Source https://resources.allsetlearning.com/chinese/grammar/Preposition
    PREPOSITION_zhs = set('干将莫邪,东皇太一,太乙真人,妲己,程咬金')
    return PREPOSITION_zhs.intersection(set(phrase))

def search4letters(phrase: str, letters: str='神装') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
