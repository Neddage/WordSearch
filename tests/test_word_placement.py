import unittest
from word_search.word_placement import WordPlacement 

class TestWordPlacement(unittest.TestCase):

    def test_word_placement_initialization(self):
        word = "test"
        positions = {
            "0-0": "t",
            "0-1": "e",
            "0-2": "s",
            "0-3": "t"
        }
        word_placement = WordPlacement(word, positions)

        self.assertEqual(word_placement.word, word)
        self.assertDictEqual(word_placement.positions, positions)

    def test_word_placement_positions_validity(self):
        with self.assertRaises(TypeError):
            invalid_positions = [("0-0", "t"), ("0-1", "e")]
            WordPlacement("test", invalid_positions)

        with self.assertRaises(TypeError):
            invalid_positions = {
                0: "t",
                1: "e"
            }
            WordPlacement("test", invalid_positions)

    def test_word_placement_positions_format(self):
        with self.assertRaises(ValueError):
            invalid_positions = {
                "0_0": "t",
                "0_1": "e",
                "0_2": "s",
                "0_3": "t"
            }
            WordPlacement("test", invalid_positions)

    def test_word_placement_positions_letter_too_long(self):
        with self.assertRaises(ValueError):
            invalid_positions = {
                "0-0": "te",
                "0-1": "st",
                "0-2": "es",
                "0-3": "tt"
            }
            WordPlacement("test", invalid_positions)


if __name__ == "__main__":
    unittest.main()
