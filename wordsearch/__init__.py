"""
wordsearch

A Python module to generate and solve word searches.
"""
__all__ = ["WordSearch", "WordPlacerInterface", "WordPlacement", "HorizontalWordPlacer", "VerticalWordPlacer"]
__version__ = "0.0.1"
__author__ = 'Ian Shaw'
__credits__ = ''

# Importing the necessary modules and classes
from wordsearch.word_search import WordSearch
from wordsearch.word_placer_interface import WordPlacerInterface
from wordsearch.word_placement import WordPlacement
from wordsearch.horizontal_word_placer import HorizontalWordPlacer
from wordsearch.vertical_word_placer import VerticalWordPlacer