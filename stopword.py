import nltk

# Download NLTK resources (do this only the first time)
nltk.download('punkt')
nltk.download('stopwords')  # Download stopwords corpus

def remove_common_words(sentence):
  """
  This function removes very common words from a sentence.

  Args:
      sentence: A string representing the sentence to process.

  Returns:
      A string representing the sentence with common words removed.
  """

  # Tokenize the sentence using NLTK's word_tokenize function
  words = nltk.word_tokenize(sentence)

  # Get a set of English stop words from NLTK (simplified explanation)
  common_words = set(nltk.corpus.stopwords.words('english'))

  # Filter out common words
  filtered_words = [word for word in words if word not in common_words]

  # Join the filtered words back into a sentence
  filtered_sentence = ' '.join(filtered_words)

  return filtered_sentence

# Example sentence (simpler)
sentence = "This sentence has some common words."

# Process the sentence
filtered_sentence = remove_common_words(sentence)
print(f"Original Sentence: {sentence}")
print(f"Sentence without Common Words: {filtered_sentence}")

print("Common word removal completed!")
