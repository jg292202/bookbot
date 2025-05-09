import re

def get_book_text(filepath):
    """Reads the contents of the file and returns it as a string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def count_words(text):
    """Returns the number of words in a given string."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_characters(text):
    """Returns a dictionary with the count of each character in the text."""
    char_count = {} # Initializes an empty dictionary
    for char in text.lower():  # Convert all character to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count # Returns dictionary {'p': 6121, 'r': 20818, ...}

def sort_characters(text):
    """Returns a dictionary with the characters arranged in order"""
    char_count = count_characters(text)
    # convert dictionary into list of dicts and filter non-alpha char
    sorted_list = [{"char": char, "num": count} for char, count in char_count.items() if char.isalpha()]
    # Sort the list by count in descending order
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list 



