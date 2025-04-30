from stats import num_words, character_count, sort_characters
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    book_text = get_book_text(path)
    word_count = num_words(book_text)
    char_count = character_count(book_text)
    sorted_char_count = sort_characters(char_count)
    print(f"{word_count} words found in the document")
    print(f"{char_count}")
    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {path}...\n"
        "----------- Word Count ----------\n"
        f"Found {word_count} total words\n"
        "--------- Character Count -------")
    for dict_item in sorted_char_count:
        if not dict_item['char'].isalpha():
            continue
        print(f"{dict_item['char']}: {dict_item['num']}")
    
    print("============= END ===============")

main()