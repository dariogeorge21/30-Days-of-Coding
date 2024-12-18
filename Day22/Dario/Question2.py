def find_longest_word(sentence):
    words = sentence.split() 
    longest_word = max(words, key=len) 
    return longest_word, len(longest_word)

sentence = "The quick brown fox jumped over the lazy dog"
longest_word, length = find_longest_word(sentence)
print(f"The longest word is: '{longest_word}' with length {length}")
