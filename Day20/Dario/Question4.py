def word_count(sentence):
    """
    Function to count the occurrences of each word in a sentence.
    :param sentence: A string containing words.
    :return: A dictionary with words as keys and their counts as values.
    """
    word_freq = {}  # Initialize an empty dictionary
    
    # Convert the sentence to lowercase and split it into words
    words = sentence.lower().split()
    
    # Iterate through the words
    for word in words:
        # Remove punctuation (optional step)
        word = word.strip(".,!?\"'")
        
        # Update word frequency in dictionary
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

# Input: A sentence from the user
sentence = input("Enter a sentence: ")

# Count word occurrences
result = word_count(sentence)

# Display the word frequencies
print("\nWord Count:")
for word, count in result.items():
    print(f"'{word}': {count}")
