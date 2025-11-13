from ...attrs import LIKE_NUM

_num_words = [
    "zero",
    "un",
    "dos",
    "tres",
    "quatre",
    "cinc",
    "sis",
    "set",
    "vuit",
    "nou",
    "deu",
    "onze",
    "dotze",
    "tretze",
    "catorze",
    "quinze",
    "setze",
    "disset",
    "divuit",
    "dinou",
    "vint",
    "trenta",
    "quaranta",
    "cinquanta",
    "seixanta",
    "setanta",
    "vuitanta",
    "noranta",
    "cent",
    "mil",
    "milió",
    "bilió",
    "trilió",
    "quatrilió",
    "gazilió",
    "bazilió",
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if "/" in text:
        parts = text.split("/")
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return True
    # Using a set lookup for O(1) instead of O(n) list lookup
    # _num_words_set is a memoized static attribute to avoid recreating
    # the set on every function call
    if not hasattr(like_num, "_num_words_set"):
        from spacy.lang.ca.lex_attrs import _num_words

        like_num._num_words_set = set(_num_words)
    if text in like_num._num_words_set:
        return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
