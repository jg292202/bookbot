
# Execute the program
import sys
from stats import get_book_text, count_words, count_characters, sort_characters

def main():
    """Reads the book text and prints the word count."""
    
    
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path dynamically

    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        sys.exit(1) # Exit with error code if file is missing

    # Read the book text

    book_text = get_book_text(book_path)
    # num_words = count_words(book_text)
    #char_counts = count_characters(book_text) # Get word count
    #print("Character Frequencies:")
    # num_words = count_words(book_text)
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {book_path}... \n")
    num_words = count_words(book_text)
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words\n")

# Character count

    sorted_chars = sort_characters(book_text)
    print("------------ Character Count ------------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============ END ============")


    #for char, count in sorted(char_counts.items()):
        #print(f"'{char}': {count}")

if __name__ == "__main__":
    main()
