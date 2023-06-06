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