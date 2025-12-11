from collections import Counter

text = input("Enter message: ").lower().split()
word_counts = Counter(text)

print("Most common words:", word_counts.most_common(3))
print("Total words:", len(text))
