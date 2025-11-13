from ...attrs import LIKE_NUM

_num_words = [
    "sifir",
    "yek",
    "du",
    "sê",
    "çar",
    "pênc",
    "şeş",
    "heft",
    "heşt",
    "neh",
    "deh",
    "yazde",
    "dazde",
    "sêzde",
    "çarde",
    "pazde",
    "şazde",
    "hevde",
    "hejde",
    "nozde",
    "bîst",
    "sî",
    "çil",
    "pêncî",
    "şêst",
    "heftê",
    "heştê",
    "nod",
    "sed",
    "hezar",
    "milyon",
    "milyar",
]

_ordinal_words = [
    "yekem",
    "yekemîn",
    "duyem",
    "duyemîn",
    "sêyem",
    "sêyemîn",
    "çarem",
    "çaremîn",
    "pêncem",
    "pêncemîn",
    "şeşem",
    "şeşemîn",
    "heftem",
    "heftemîn",
    "heştem",
    "heştemîn",
    "nehem",
    "nehemîn",
    "dehem",
    "dehemîn",
    "yazdehem",
    "yazdehemîn",
    "dazdehem",
    "dazdehemîn",
    "sêzdehem",
    "sêzdehemîn",
    "çardehem",
    "çardehemîn",
    "pazdehem",
    "pazdehemîn",
    "şanzdehem",
    "şanzdehemîn",
    "hevdehem",
    "hevdehemîn",
    "hejdehem",
    "hejdehemîn",
    "nozdehem",
    "nozdehemîn",
    "bîstem",
    "bîstemîn",
    "sîyem",
    "sîyemîn",
    "çilem",
    "çilemîn",
    "pêncîyem",
    "pênciyemîn",
    "şêstem",
    "şêstemîn",
    "heftêyem",
    "heftêyemîn",
    "heştêyem",
    "heştêyemîn",
    "notem",
    "notemîn",
    "sedem",
    "sedemîn",
    "hezarem",
    "hezaremîn",
    "milyonem",
    "milyonemîn",
    "milyarem",
    "milyaremîn",
]


def like_num(text):
    # Optimize by minimizing repeated work, and using sets for O(1) lookups.
    # Precompute lookup sets out of globals only once at function level.
    # text.replace/startswith are already optimized, so only use them as needed.
    # Inline `is_digit` since it's only used here.

    # Pull lookup sets into function attributes to avoid repeated global lookups.
    if not hasattr(like_num, "_num_words_set"):
        like_num._num_words_set = set(_num_words)
        like_num._ordinal_words_set = set(_ordinal_words)
        like_num._endings = ("em", "yem", "emîn", "yemîn")

    # Remove initial sign/approx chars for later logic
    if text and text[0] in "+-±~":
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/", 1)
        if num.isdigit() and denom.isdigit():
            return True
    text_lower = text.lower()
    if text_lower in like_num._num_words_set:
        return True
    # Ordinal number
    if text_lower in like_num._ordinal_words_set:
        return True

    # Inline and optimize original is_digit
    for ending in like_num._endings:
        to = len(ending)
        if text_lower.endswith(ending) and text_lower[:-to].isdigit():
            return True

    return False


def is_digit(text):
    endings = ("em", "yem", "emîn", "yemîn")
    for ending in endings:
        to = len(ending)
        if text.endswith(ending) and text[:-to].isdigit():
            return True

    return False


LEX_ATTRS = {LIKE_NUM: like_num}
