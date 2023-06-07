from wordsearch.word_placer_interface import WordPlacerInterface
from wordsearch.word_search import WordSearch, UnableToPlaceWordError
from wordsearch.word_placement import WordPlacement
import random


# Class for a horizontal word placer that places words horizontally onto the grid
class HorizontalWordPlacer(WordPlacerInterface):
    MAX_ATTEMPTS = 5

    def add_word(self, word: str, word_search: WordSearch) -> None:
        """Adds the supplied word to the supplied WordSearch

        Args:
            word (str): The word to add to the WordSearch
            word_search (WordSearch): The WordSearch object to add the word to

        Raises:
            ValueError: Word is too long to fit in the grid
            RuntimeError: Unable to place word on grid, maximum attempts reached
        """
        # Basic placement of the word on the grid only handles horizontal left-to-right words
        # We only need to check width for this method of placement
        if len(word) > word_search.width:
            raise ValueError("Word is too long to fit in the grid")

        # Make MAX_ATTEMPTS
        attempt = 0
        while attempt < self.MAX_ATTEMPTS:
            # Choose a random row for the word
            row = random.randint(0, word_search.height - 1)

            # Choose a random starting column so the the word fits
            start_col = random.randint(0, word_search.width - len(word))

            # work out the letter positions
            positions = {f"{row}-{start_col + index}": letter for index, letter in enumerate(word)}
            # create the placement and try to add this to the word search
            placement = WordPlacement(word, positions)

            try:
                word_search.add_word_placement(placement)
                return None
            except UnableToPlaceWordError:
                attempt += 1
                # do nothing so we loop again in the while and retry

        raise RuntimeError("Unable to place word on grid, maximum attempts reached")
