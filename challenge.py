def word_counter(text):
    words = text.split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Example usage:
input_text = "This is a sample text. This text will be used for word counting."
counts = word_counter(input_text)

# Display word counts
for word, count in counts.items():
    print(f"'{word}' occurs {count} time(s)")
