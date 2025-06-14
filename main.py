import sys

from stats import (
    word_counter_funct, 
    get_chars_dict,
    make_dict_list)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book> ")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_counter_funct(text)
    dict_of_char = get_chars_dict(text)
    chars_in_sorted_list = make_dict_list(dict_of_char)
    print_report(book_path, num_words, chars_in_sorted_list)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_in_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_in_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



main()