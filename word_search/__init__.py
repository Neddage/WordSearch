"""
word_search

A Python module to generate and solve word searches.
"""
__all__ = ["WordSearch", "WordPlacerInterface", "WordPlacement", "HorizontalWordPlacer", "VerticalWordPlacer"]
__version__ = "0.0.1"
__author__ = 'Ian Shaw'
__credits__ = ''

# Importing the necessary modules and classes
from word_search.word_search import WordSearch
from word_search.word_placer_interface import WordPlacerInterface
from word_search.word_placement import WordPlacement
from word_search.horizontal_word_placer import HorizontalWordPlacer
from word_search.vertical_word_placer import VerticalWordPlacer