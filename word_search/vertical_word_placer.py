import random
from word_search.word_placer_interface import WordPlacerInterface
from word_search.word_search import WordSearch, UnableToPlaceWordError
from word_search.word_placement import WordPlacement

class VerticalWordPlacer(WordPlacerInterface):
    MAX_ATTEMPTS = 5
    
    def add_word(self, word: str, word_search: WordSearch) -> None:
        """
        Adds the supplied word to the supplied WordSearch vertically.

        Args:
            word (str): The word to add to the WordSearch.
            word_search (WordSearch): The WordSearch object to add the word to.

        Raises:
            ValueError: Word is too long to fit in the grid.
            RuntimeError: Unable to place word on grid, maximum attempts reached.
        """
        word_length = len(word)

        if word_length > word_search.height:
            raise ValueError('Word is too long to fit in the grid')
        
        attempt = 0
        while attempt < self.MAX_ATTEMPTS:
            col = random.randint(0, word_search.width - 1)
            start_row = random.randint(0, word_search.height - word_length)
              
            positions = {f"{start_row + index}-{col}": letter for index, letter in enumerate(word)}
            placement = WordPlacement(word, positions)
            
            try:
                word_search.add_word_placement(placement)
                return None
            except UnableToPlaceWordError:
                attempt += 1
        
        raise RuntimeError('Unable to place word on grid, maximum attempts reached.')
