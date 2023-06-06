from word_search.word_placer_interface import WordPlacerInterface
from word_search.word_search import WordSearch, UnableToPlaceWordError
from word_search.word_placement import WordPlacement
import random

class BasicWordPlacer(WordPlacerInterface):
    def add_word(self, word:str, word_search: WordSearch) -> WordSearch:
        # Basic placement of the word on the grid only handles horizontal left-to-right words
        # We only need to check width for this method of placement
        if len(word) > word_search.width:
            raise ValueError('Word is too long to fit in the grid')
        
        # we'll attempt things 3 times
        attempt = 0
        while attempt <= 3:
            attempt += 1
            # Choose a random row for the word
            row = random.randint(0, word_search.height - 1)

            # Choose a random starting column so the the word fits
            start_col = random.randint(0, word_search.width - len(word))

            # work out the letter positions
            positions = {}
            for index, letter in enumerate(word):
                positions[f"{row}-{start_col + index}"] = letter
            
            # create the placement and try to add this to the word search
            placement = WordPlacement(word, positions)
            
            try:
                word_search.add_word_placement(placement)
                return word_search
            except UnableToPlaceWordError:
                if attempt >= 3:
                    raise RuntimeError('Unable to place word on grid, maximum attempts reached')
                # do nothing so we loop again in the while and retry        