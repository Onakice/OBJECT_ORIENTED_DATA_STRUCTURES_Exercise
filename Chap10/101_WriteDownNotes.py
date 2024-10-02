# Initial word dictionary
unordered_words_and_meanings = {
    'watermelon': 'A Large fruit',
    'nectarine': 'Similar to a peach.',
    'mango': 'Tropical fruit.',
    'kiwi': 'Small fruit.',
    'vanilla': 'Used in baking.',
    'fig': 'Chewy skin.',
    'pear': 'Sweet fruit.',
    'cherry': 'Red fruit.',
    'strawberry': 'Tiny seeds.',
    'quince': 'Tart flavor.',
    'ugli fruit': 'Hybrid citrus.'
}

# Default meaning if the word is not found
default_meaning = '(Default) A fruit.'

# Function to search the words
def search_words(words):
    word_list = list(unordered_words_and_meanings.keys())
    word_meanings = list(unordered_words_and_meanings.values())
    
    index_changes = {}
    
    for word in words:
        word = word.lower().strip()  # Convert input to lowercase and strip any extra spaces
        found = False
        time_taken = 0  # Initialize time for each search
        
        # Search for the word in the list
        for i in range(len(word_list)):
            time_taken += 1  # Each lookup takes 1 second
            if word_list[i] == word:
                found = True
                meaning = word_meanings[i]
                
                # Add 1 second for returning the meaning
                time_taken += 1
                
                print(f"(1) Word '{word}' found ({time_taken} seconds): {meaning}")
                
                # Record index change
                if word not in index_changes:
                    index_changes[word] = f"{i} -> {i-1 if i > 0 else i}"
                
                # Swap with the previous word (Transposition)
                if i > 0:
                    word_list[i], word_list[i-1] = word_list[i-1], word_list[i]
                    word_meanings[i], word_meanings[i-1] = word_meanings[i-1], word_meanings[i]
                
                break
        
        # If word not found, add to the end of the list
        if not found:
            time_taken += len(word_list)  # Time taken to search the entire list
            time_taken += 1  # Add 1 second for adding the new word
            unordered_words_and_meanings[word] = default_meaning
            word_list.append(word)
            word_meanings.append(default_meaning)
            
            print(f"(2) Word '{word}' added ({time_taken} seconds): {default_meaning}")
            
            # Record index change for the new word
            index_changes[word] = f"None -> {len(word_list) - 1}"
    
    print("(END) Updated dictionary:")
    updated_dict_str = ', '.join([f"{idx}: {word}" for idx, word in enumerate(word_list)])
    print(updated_dict_str)

    print("(SUMMARY OF INDEX CHANGES):")
    for word, change in index_changes.items():
        print(f"{word}: {change}")

if __name__ == "__main__":
    input_words = input("Enter a word to search for: ").split(',')
    search_words(input_words)