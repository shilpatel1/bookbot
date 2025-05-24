from stats import get_text_count, get_char_count, sorted_list_by_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main(path_to_file):
    
    # './books/frankenstein.txt'
    book_text = get_book_text(path_to_file)
    num_of_words = get_text_count(book_text)
    count_of_char = get_char_count(book_text)
    sorted_dictionary_list = sorted_list_by_count(count_of_char)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dictionary_list:
        print(item['char']+":",item['count'])
    
    print("============= END ===============")

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    main(sys.argv[1])