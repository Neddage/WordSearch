# from word_search.word_placer_interface import WordPlacerInterface
import random
from word_search.word_placement import WordPlacement

class WordSearch:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        # initialise the grid
        self._initialise_grid()
        # initialise the dict to hold the word objects
        self._word_placements = {}
        
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    def can_place(self, placement: WordPlacement):
        all = self.get_positions_in_use()
        if not all:
            return True
        
        for position in placement.positions:
            if position in all:
                return False
            
        return True
    
    def get_positions_in_use(self) -> list[str]:
        in_use = []
        for placement in self._word_placements:
            in_use.extend(self._word_placements[placement].positions)
        return in_use
    
    def remove_word(self, word: str) -> None:
        if word in self._word_placements:
            # get each of the positions and "reset" them to a random character
            for position in self._word_placements[word].positions:
                print(position)
                row, col = position.split("-")
                self._grid[int(row)][int(col)] = random.choice('abcdefghijklmnopqrstuvwxyz')
            del self._word_placements[word]
        
    def add_word_placement(self, placement: WordPlacement) -> None:
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
        # Build the grid, inserting random characters into the slots
        self._grid = [["" for _ in range(self._width)] for _ in range(self._height)]
        self._fill_empty()
    
    def _fill_empty(self):
        # Fill any empty spaces with a random letter
        for row in range(self._height):
            for col in range(self._width):
                if not self._grid[row][col]:
                    self._grid[row][col] = random.choice('abcdefghijklmnopqrstuvwxyz')
    
class UnableToPlaceWordError(RuntimeError):
    pass