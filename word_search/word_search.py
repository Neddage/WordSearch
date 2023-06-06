# from word_search.word_placer_interface import WordPlacerInterface
import random
from word_search.word_placement import WordPlacement

class WordSearch:
    CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyz'
    
    def __init__(self, width: int, height: int) -> None:
        """ Class constructor

        Args:
            width (int): The desired width of the word search (ie. columns)
            height (int): The desired height of the word search (ie. rows)
        """
        self._width = width
        self._height = height
        # initialise the grid
        self._initialise_grid()
        # initialise the dict to hold the word objects
        self._word_placements = {}
    
    def can_place(self, placement: WordPlacement) -> bool:
        """ Checks to see if the supplied WordPlacement can be added to the word search without overlapping an existing word
            
        Args:
            placement (WordPlacement): The WordPlacement object to check

        Returns:
            bool: True if it can be placed on the WordSearch False otherwise
        """
        # TODO: Could refactor to remove need for get_all_positions_in_use but feel it might be useful later on so keeping for now
        all = self.get_positions_in_use()
        if not all:
            # if no words placed, then nothing to check
            return True
        
        # TODO: Should allow cases where the letter being overwritten is the same as the existing one so words can overlap when suitable
        for position in placement.positions:
            if position in all:
                # return False as soon as we find a clash, no point continuing to check
                return False
            
        return True
    
    def get_positions_in_use(self) -> list[str]:
        """ Returns an array of string representations of all the WordSearch grid positions currently being used

        Returns:
            list[str]: array of string representations of positions. ie. ["1-0", "1-1", "1-2"]
        """
        in_use = []
        # I feel there is a more pythonic way of doing this but for right now we loop through and build the positions array
        for placement in self._word_placements:
            in_use.extend(self._word_placements[placement].positions)
        return in_use
    
    def remove_word(self, word: str) -> None:
        """ Removes a word from the WordSearch object and grid

        Args:
            word (str): The word to remove
        """
        if word in self._word_placements:
            # get each of the positions and "reset" them to a random character
            for position in self._word_placements[word].positions:
                row, col = position.split("-")
                self._grid[int(row)][int(col)] = random.choice(self.CHARACTER_SET)
            # remove the word placement object out the list
            del self._word_placements[word]
        
    def add_word_placement(self, placement: WordPlacement) -> None:
        """ Adds a WordPlacement into the WordSearch

        Args:
            placement (WordPlacement): The WordPlacement object to add

        Raises:
            UnableToPlaceWordError: Raised if we cannot place the word on the grid with the current positions
        """
        # remove existing word if it already exists
        self.remove_word(placement.word)
        # verify that none of the positions in the placement have already been used
        if not self.can_place(placement):
            raise UnableToPlaceWordError('Unable to place the word on the grid')
        # update the word search grid with the letters
        for position in placement.positions:
            row, column = position.split("-")
            self._grid[int(row)][int(column)] = placement.positions[position]
        # Add it to the dictionary of words placements
        self._word_placements[placement.word] = placement
    
    def _initialise_grid(self) -> None:
        """ Initialise the WordSearch grid based on the width/height and fills it with random characters
        """
        # Build the grid, inserting random characters into the slots
        self._grid = [["" for _ in range(self._width)] for _ in range(self._height)]
        # TODO: Probably don't need to use a separate method here now
        self._fill_empty()
    
    def _fill_empty(self):
        """ Replaces any blank entries in the grid with a random character
        """
        # Fill any empty spaces with a random letter
        for row in range(self._height):
            for col in range(self._width):
                if not self._grid[row][col]:
                    self._grid[row][col] = random.choice(self.CHARACTER_SET)
                    
    @property
    def width(self) -> int:
        """ Width property

        Returns:
            int: The width
        """
        return self._width
    
    @property
    def height(self) -> int:
        """ Height property

        Returns:
            int: The Height
        """
        return self._height
    
    @property
    def word_placements(self) -> dict:
        return self._word_placements
    
    @property
    def words(self) -> list[str]:
        """ Returns a list of the words current on the WordSearch

        Returns:
            list[str]: _description_
        """
        return [self._word_placements[placement].word for placement in self._word_placements]
    
    @property
    def grid(self) -> list[list]:
        """ Returns the word search grid

        Returns:
            list[list]: The Word Search grid
        """
        return self._grid
    
# Custom error to indicate word placement failed
class UnableToPlaceWordError(RuntimeError):
    pass