from toolkit.textstats import char_count, top_words, word_count


def test_word_count():
    assert word_count("the quick brown fox") == 5


def test_word_count_empty():
    assert word_count("") == 0


def test_char_count_without_spaces():
    assert char_count("a b c", include_spaces=False) == 3


def test_top_words():
    assert top_words("git push git pull git", n=1) == [("git", 3)]
