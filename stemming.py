import nltk

# Download NLTK resources (do this only the first time)
nltk.download('punkt')
nltk.download('porter')  # Download Porter Stemmer resources

def stem_sentence(sentence):
 

  # Tokenize the sentence using NLTK's word_tokenize function
  words = nltk.word_tokenize(sentence)

  # Create a Porter stemmer object (used for stemming)
  simplifier = nltk.PorterStemmer()

  # Simplify each word (stemming)
  stemmed_words = [simplifier.stem(word) for word in words]

  return stemmed_words

# Example sentences
sentences = [
  "This is a sample sentence to test simplification.",
  "Here's another example with punctuation!",
  "We can explore different languages too!"
]

# Process each sentence
for sentence in sentences:
  stemmed_words = stem_sentence(sentence)
  print(f"Sentence: {sentence}")
  print(f"Stemmed Words: {stemmed_words}")
  print()  # Print an empty line for readability

print("Sentence simplification completed!")
