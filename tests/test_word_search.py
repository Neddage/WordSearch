import unittest
from word_search.word_search import WordSearch, UnableToPlaceWordError
from word_search.word_placement import WordPlacement

class TestWordSearch(unittest.TestCase):
    def test_initialise_grid(self):
        ws = WordSearch(3, 3)
        self.assertEqual(ws.width, 3)
        self.assertEqual(ws.height, 3)
        self.assertIsNotNone(ws._grid)

    def test_add_word_placement(self):
        ws = WordSearch(5, 5)
        wp = WordPlacement("test", {"0-0": "t", "0-1": "e", "0-2": "s", "0-3": "t"})
        ws.add_word_placement(wp)
        self.assertEqual(ws._grid[0][0:4], ["t", "e", "s", "t"])
        self.assertIn("test", ws._word_placements)

    def test_remove_word(self):
        ws = WordSearch(5, 5)
        wp = WordPlacement("test", {"0-0": "t", "0-1": "e", "0-2": "s", "0-3": "t"})
        ws.add_word_placement(wp)
        ws.remove_word("test")
        self.assertNotIn("test", ws._word_placements)

    def test_can_place(self):
        ws = WordSearch(5, 5)
        wp1 = WordPlacement("test", {"0-0": "t", "0-1": "e", "0-2": "s", "0-3": "t"})
        wp2 = WordPlacement("fail", {"0-0": "f", "0-1": "a", "0-2": "i", "0-3": "l"})
        self.assertTrue(ws.can_place(wp1))
        ws.add_word_placement(wp1)
        self.assertFalse(ws.can_place(wp2))

    def test_get_positions_in_use(self):
        ws = WordSearch(5, 5)
        wp1 = WordPlacement("test", {"0-0": "t", "0-1": "e", "0-2": "s", "0-3": "t"})
        wp2 = WordPlacement("word", {"1-0": "w", "1-1": "o", "1-2": "r", "1-3": "d"})
        ws.add_word_placement(wp1)
        ws.add_word_placement(wp2)

        expected_positions = ["0-0", "0-1", "0-2", "0-3", "1-0", "1-1", "1-2", "1-3"]
        self.assertEqual(sorted(ws.get_positions_in_use()), sorted(expected_positions))

    def test_add_word_placement_error(self):
        ws = WordSearch(5, 5)
        wp1 = WordPlacement("test", {"0-0": "t", "0-1": "e", "0-2": "s", "0-3": "t"})
        wp2 = WordPlacement("fail", {"0-0": "f", "0-1": "a", "0-2": "i", "0-3": "l"})
        ws.add_word_placement(wp1)

        with self.assertRaises(UnableToPlaceWordError):
            ws.add_word_placement(wp2)
            
    def test_words(self):
        ws = WordSearch(5, 5)
        wp1 = WordPlacement("test", {"0-0": "t", "0-1": "e", "0-2": "s", "0-3": "t"})
        wp2 = WordPlacement("word", {"1-0": "w", "1-1": "o", "1-2": "r", "1-3": "d"})
        ws.add_word_placement(wp1)
        ws.add_word_placement(wp2)
        
        self.assertEquals(sorted(ws.words), sorted(["test", "word"]))


if __name__ == "__main__":
    unittest.main()
