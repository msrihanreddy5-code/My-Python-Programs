from difflib import get_close_matches

items = ["apple", "banana", "applaud", "orange", "pineapple"]
query = input("Search: ")

matches = get_close_matches(query, items, cutoff=0.3)
print("Matches:", matches)
