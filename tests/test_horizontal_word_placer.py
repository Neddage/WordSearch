import unittest
from word_search.word_search import WordSearch
from word_search.horizontal_word_placer import HorizontalWordPlacer

class TestHorizontalWordPlacer(unittest.TestCase):
    
    def setUp(self):
        self.horizontal_word_placer = HorizontalWordPlacer()
        self.word_search = WordSearch(10, 10)

    def test_add_word_too_long(self):
        with self.assertRaises(ValueError):
            self.horizontal_word_placer.add_word("abcdefghijklm", self.word_search)

    def test_add_single_word_successfully(self):
        try:
            self.horizontal_word_placer.add_word("hello", self.word_search)
        except RuntimeError:  
            self.fail("add_word failed unexpectedly for a valid word")

    def test_add_multiple_words_successfully(self):
        try:
            self.horizontal_word_placer.add_word("hello", self.word_search)
            self.horizontal_word_placer.add_word("world", self.word_search)
        except RuntimeError:
            self.fail("add_word failed unexpectedly for multiple valid words")

    def test_maximum_attempts_reached(self):
        with self.assertRaises(RuntimeError):
            word_search_single_row = WordSearch(6, 1)
            self.horizontal_word_placer.add_word("apple", word_search_single_row)
            self.horizontal_word_placer.add_word("banana", word_search_single_row)

    def test_word_placements_are_horizontal(self):
        self.horizontal_word_placer.add_word("test", self.word_search)
        placed_word =  self.word_search.word_placements["test"]
        positions = list(placed_word.positions.keys())
        row_values = set([pos.split('-')[0] for pos in positions])

        self.assertEqual(len(row_values), 1, "Word was not placed horizontally")


if __name__ == "__main__":
    unittest.main()
