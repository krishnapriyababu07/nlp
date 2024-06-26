import nltk

# Download NLTK resources (do this only the first time)
nltk.download('punkt')

def split_sentence(sentence):
  
  # Tokenize the sentence using NLTK's word_tokenize function
  words = nltk.word_tokenize(sentence)
  return words

# Example sentences
sentences = [
  "This is a simple sentence.",
  "Here's another example with punctuation!",
  "We can explore different languages too!"
]

# Tokenize each sentence
for sentence in sentences:
  words = split_sentence(sentence)
  print(f"Sentence: {sentence}")
  print(f"Words: {words}")
  print()  # Print an empty line for readability

print("Sentence splitting completed!")
