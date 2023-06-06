from abc import ABC, abstractclassmethod
from word_search.word_search import WordSearch

# Interface for word "placers" to implement.
class WordPlacerInterface(ABC):
    @abstractclassmethod
    def add_word(self, word:str, word_search: WordSearch) -> None:
        """ Should accept a word and a word search and return a new wordsearch object with the word added

        Args:
            word (str): The word to add to the WordSearch object
            word_search (WordSearch): The WordSearch object to add the word to
        """
        pass