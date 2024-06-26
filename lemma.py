import nltk

# Download NLTK resources (do this only the first time)
nltk.download('punkt')
nltk.download('wordnet')  # Download WordNet resources for lemmatization

def lemmatize_sentence(sentence):
  """
  This function simplifies words in a sentence (lemmatization).

  Args:
      sentence: A string representing the sentence to lemmatize.

  Returns:
      A list of strings representing the simplified words in the sentence.
  """

  # Tokenize the sentence using NLTK's word_tokenize function
  words = nltk.word_tokenize(sentence)

  # Create a WordNetLemmatizer object (used for lemmatization)
  lemmatizer = nltk.WordNetLemmatizer()

  # Lemmatize each word (assuming nouns by default)
  lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

  return lemmatized_words

# Example sentences
sentences = [
  "This is a sample sentence to test lemmatization.",
  "Here's another example with punctuation!",
  "We can explore different languages too!"
]

# Lemmatize each sentence
for sentence in sentences:
  lemmatized_words = lemmatize_sentence(sentence)
  print(f"Sentence: {sentence}")
  print(f"Lemmatized Words: {lemmatized_words}")
  print()  # Print an empty line for readability

print("Sentence lemmatization completed!")
