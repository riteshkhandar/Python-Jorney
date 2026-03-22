def is_unique(text):
    # Using a dictionary to track characters we've seen
    char_counts = {}

    for char in text:
        if char in char_counts:
            # If the character is already in the dictionary, it's not unique
            return False
        # Add the character to the dictionary
        char_counts[char] = 1
        
    # If the loop finishes without finding a duplicate, it is unique
    return True

# Examples:
print(is_unique("apple"))  # Output: False
print(is_unique("world"))  # Output: True
