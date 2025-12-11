import nltk
nltk.download('punkt')

text = input("Enter long text: ")
sentences = nltk.sent_tokenize(text)

summary = sentences[:3]
print("\nSummary:\n", " ".join(summary))
