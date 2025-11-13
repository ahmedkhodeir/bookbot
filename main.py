from stats import count_words, count_characters, chars_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
     text = get_book_text(sys.argv[1])
     num_words = count_words(text)
     char_dict = count_characters(text)
     char_list = chars_sorted_list(char_dict)
     print("============ BOOKBOT ============")
     print(f"Analyzing book found at {sys.argv[1]}...\n")
     print("----------- Word Count ----------")
     print(f"Found {num_words} total words\n")
     print("--------- Character Count -------")
     for item in char_list:
        print(f"{item['char']}: {item['num']}")
     print("============= END ===============")

main()