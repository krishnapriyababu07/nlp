import nltk

# Download NLTK resources (do this only the first time)
nltk.download('punkt')
nltk.download('stopwords')  # Download stopwords corpus
nltk.download('porter')  # Download Porter Stemmer resources
nltk.download('wordnet')  # Download WordNet resources for lemmatization

def process_sentence(sentence, use_stemming=False, use_lemmatization=False):

  # Tokenize the sentence using NLTK's word_tokenize function
  words = nltk.word_tokenize(sentence)

  # Get a set of English stop words from NLTK
  stop_words = set(nltk.corpus.stopwords.words('english'))

  # Filter out stop words
  filtered_words = [word for word in words if word not in stop_words]

  # Apply stemming or lemmatization (optional)
  if use_stemming:
    # Create a Porter stemmer object
    stemmer = nltk.PorterStemmer()
    processed_words = [stemmer.stem(word) for word in filtered_words]
  elif use_lemmatization:
    # Create a WordNetLemmatizer object
    lemmatizer = nltk.WordNetLemmatizer()
    processed_words = [lemmatizer.lemmatize(word) for word in filtered_words]
  else:
    # No stemming or lemmatization applied, just remove stop words
    processed_words = filtered_words

  return processed_words

# Get user input
sentence = input("Enter a sentence to process: ")

# Process options (explained during execution)
print("\nProcessing options:")
print("1. Tokenization (split sentence into words)")
print("2. Tokenization + Stop Word Removal")
print("3. Tokenization + Stemming")
print("4. Tokenization + Lemmatization")

while True:
  try:
    choice = int(input("Enter your choice (1-4) or 0 to quit: "))
    if 0 <= choice <= 4:
      break
    else:
      print("Invalid choice. Please enter a number between 0 and 4.")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Process the sentence based on user choice
if choice == 0:
  print("Exiting...")
elif choice == 1:
  processed_words = process_sentence(sentence)
  print(f"\nOriginal Sentence: {sentence}")
  print(f"Processed Words (Tokenized): {processed_words}")
elif choice == 2:
  processed_words = process_sentence(sentence)
  print(f"\nOriginal Sentence: {sentence}")
  print(f"Processed Words (Tokenized & Stop Words Removed): {processed_words}")
elif choice == 3:
  processed_words = process_sentence(sentence, use_stemming=True)
  print(f"\nOriginal Sentence: {sentence}")
  print(f"Processed Words (Tokenized, Stop Words Removed & Stemmed): {processed_words}")
elif choice == 4:
  processed_words = process_sentence(sentence, use_lemmatization=True)
  print(f"\nOriginal Sentence: {sentence}")
  print(f"Processed Words (Tokenized, Stop Words Removed & Lemmatized): {processed_words}")

print("\nSentence processing completed!")
