# WordPlacement class that holds the position of where the words letters should be placed on the grid
class WordPlacement:
    def __init__(self, word: str, positions: dict[str,str]) -> None:
        """_summary_

        Args:
            word (str): The word this placement relates to
            positions (dict[str,str]): a dictionary where the key is a string representation of the position in the grid and the value the letter
        """
        self.word = word
        self.positions = positions
        
    @property
    def positions(self):
        """ Returns a dictionary with the key as a string representation of the row and column and the value the letter

        Returns:
            dict[str, str]: dictionary of position to letter ie. { "0-1": "t", "0-2": "e", "0-3": "s", "0-4": "t"}
        """
        return self._positions
    
    @positions.setter
    def positions(self, positions: dict[str, str]) -> None:
        """ Setter for positions. Validates the positions before storing.

        Args:
            positions (dict[str, str]): dictionary of position to letter. ie. { "0-1": "t", "0-2": "e", "0-3": "s", "0-4": "t"}
        """
        self.validate_positions(positions)
        self._positions = positions
        
    @staticmethod
    def validate_positions(positions: dict[str, str]) -> None:
        """ Validates the supplied positions dict 

        Args:
            positions (dict[str, str]): dictionary of position to letter. ie. { "0-1": "t", "0-2": "e", "0-3": "s", "0-4": "t"}

        Raises:
            ValueError: Both key and value in positions should be strings
            ValueError: The key should be a string of two numbers separated by -
            ValueError: The value should be a single letter
        """
        # TODO: Should probably expand validation in the future/move to own class to allow more flexibility
        if type(positions) is not dict:
            raise TypeError("Positions must be a dict")
        
        for key, value in positions.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise TypeError("Both key and value in positions should be strings")

            row, column = key.split("-")
            if not row.isdigit() or not column.isdigit():
                raise ValueError("The key should be a string of two numbers separated by -")

            if len(value) != 1 or not value.isalpha():
                raise ValueError("The value should be a single letter")
    