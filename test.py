from wordsearch import WordSearch, HorizontalWordPlacer, VerticalWordPlacer
import random

# Create a WordSearch 20 x 20 letters
ws = WordSearch(7, 7)

# Get an instance  HorizontalWordPlacer
horizontalPlacer = HorizontalWordPlacer()
verticalPlacer = VerticalWordPlacer()
# A list of some words to add
words = [
    "this",
    "is",
    "an",
    "example"
]

# Add each word using the placer
for word in words:
    # Randomly use either horizontal or vertical placements
    if bool(random.randint(0,1)):
        horizontalPlacer.add_word(word, ws)
    else:
        verticalPlacer.add_word(word, ws)

# Dump out the grid
for row in ws.grid:
    print(row)