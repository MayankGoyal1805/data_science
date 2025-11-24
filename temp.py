import os

p = os.path.abspath(__file__)   # Get absolute path
print(p)
print("Current Directory:", os.path.abspath("."))
print("Parent Directory:", os.path.abspath(".."))