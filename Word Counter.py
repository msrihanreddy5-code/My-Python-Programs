text = input("Enter a paragraph:\n")

words = text.split()
num_words = len(words)
num_chars = len(text)
num_sentences = text.count('.') + text.count('!') + text.count('?')

print("Words:", num_words)
print("Characters:", num_chars)
print("Sentences:", num_sentences)
