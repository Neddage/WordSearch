from abc import ABC, abstractclassmethod
from word_search.word_search import WordSearch

class WordPlacerInterface(ABC):
    @abstractclassmethod
    def add_word(self, word:str, word_search: WordSearch) -> WordSearch:
        pass