import sys
from stats import get_word_count, get_characters_dict, get_sorted_character_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    check_arguments(sys.argv)
    book_path = sys.argv[1]
    # book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path) 
    characters_dict = get_characters_dict(book_text)
    word_count = get_word_count(book_text)
    sorted_characters = get_sorted_character_list(characters_dict)
    print_report(book_path, word_count, sorted_characters)

def print_report(book_path, num_words, sorted_characters_list):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    for character in sorted_characters_list:
        print(f"{character["char"]}: {character["num"]}")
    print(f"============= END ===============")

def check_arguments(sys_argv):
    if len(sys_argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()