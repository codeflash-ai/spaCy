from ...attrs import LIKE_NUM

_num_words = [
    "lefela",
    "nngwe",
    "pedi",
    "tharo",
    "nne",
    "tlhano",
    "thataro",
    "supa",
    "robedi",
    "robongwe",
    "lesome",
    "lesomenngwe",
    "lesomepedi",
    "sometharo",
    "somenne",
    "sometlhano",
    "somethataro",
    "somesupa",
    "somerobedi",
    "somerobongwe",
    "someamabedi",
    "someamararo",
    "someamane",
    "someamatlhano",
    "someamarataro",
    "someamasupa",
    "someamarobedi",
    "someamarobongwe",
    "lekgolo",
    "sekete",
    "milione",
    "bilione",
    "terilione",
    "kwatirilione",
    "gajillione",
    "bazillione",
]


_ordinal_words = [
    "ntlha",
    "bobedi",
    "boraro",
    "bone",
    "botlhano",
    "borataro",
    "bosupa",
    "borobedi ",
    "borobongwe",
    "bolesome",
    "bolesomengwe",
    "bolesomepedi",
    "bolesometharo",
    "bolesomenne",
    "bolesometlhano",
    "bolesomethataro",
    "bolesomesupa",
    "bolesomerobedi",
    "bolesomerobongwe",
    "somamabedi",
    "someamararo",
    "someamane",
    "someamatlhano",
    "someamarataro",
    "someamasupa",
    "someamarobedi",
    "someamarobongwe",
    "lekgolo",
    "sekete",
    "milione",
    "bilione",
    "terilione",
    "kwatirilione",
    "gajillione",
    "bazillione",
]


def like_num(text):
    # Remove leading '+', '-', '±', or '~'
    if text and text[0] in "+-±~":
        text = text[1:]
    # Remove all ',' and '.' in a single pass
    if "," in text or "." in text:
        text = text.replace(",", "").replace(".", "")
    # Fast path for pure digits
    if text.isdigit():
        return True
    # Fast path for fractional numbers with one '/'
    if "/" in text:
        if text.count("/") == 1:
            num, denom = text.split("/")
            if num.isdigit() and denom.isdigit():
                return True

    text_lower = text.lower()
    # Use set lookup for faster membership test
    _num_words_set = getattr(like_num, "_num_words_set", None)
    if _num_words_set is None:
        # Lazy-initialize and cache
        from spacy.lang.tn.lex_attrs import _num_words

        like_num._num_words_set = set(_num_words)
        _num_words_set = like_num._num_words_set

    if text_lower in _num_words_set:
        return True

    # CHeck ordinal number
    _ordinal_words_set = getattr(like_num, "_ordinal_words_set", None)
    if _ordinal_words_set is None:
        from spacy.lang.tn.lex_attrs import _ordinal_words

        like_num._ordinal_words_set = set(_ordinal_words)
        _ordinal_words_set = like_num._ordinal_words_set

    if text_lower in _ordinal_words_set:
        return True

    # Fast check for digit-based ordinals
    if len(text_lower) > 2 and text_lower.endswith("th"):
        num_part = text_lower[:-2]
        if num_part.isdigit():
            return True

    return False


LEX_ATTRS = {LIKE_NUM: like_num}
