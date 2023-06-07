import unittest
from wordsearch.word_search import WordSearch
from wordsearch.vertical_word_placer import VerticalWordPlacer

class TestVerticalWordPlacer(unittest.TestCase):
    
    def setUp(self):
        self.vertical_word_placer = VerticalWordPlacer()
        self.word_search = WordSearch(10, 10)

    def test_add_word_too_long(self):
        with self.assertRaises(ValueError):
            self.vertical_word_placer.add_word("abcdefghijklm", self.word_search)

    def test_add_single_word_successfully(self):
        try:
            self.vertical_word_placer.add_word("hello", self.word_search)
        except RuntimeError:  
            self.fail("add_word failed unexpectedly for a valid word")

    def test_add_multiple_words_successfully(self):
        try:
            self.vertical_word_placer.add_word("hello", self.word_search)
            self.vertical_word_placer.add_word("world", self.word_search)
        except RuntimeError:
            self.fail("add_word failed unexpectedly for multiple valid words")

    def test_maximum_attempts_reached(self):
        with self.assertRaises(RuntimeError):
            word_search_single_row = WordSearch(1, 6)
            self.vertical_word_placer.add_word("apple", word_search_single_row)
            self.vertical_word_placer.add_word("banana", word_search_single_row)

    def test_word_placements_are_vertical(self):
        self.vertical_word_placer.add_word("hello", self.word_search)
        placement = list(self.word_search.word_placements.values())[0]
        positions = list(placement.positions.keys())
        first_position = positions[0].split('-')
        row, col = int(first_position[0]), int(first_position[1])
        
        for position in positions[1:]:
            r, c = [int(i) for i in position.split('-')]
            self.assertEqual(c, col)
            self.assertEqual(r, row + 1)
            row = r

        


if __name__ == "__main__":
    unittest.main()
