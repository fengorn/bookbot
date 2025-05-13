from stats import get_book_text, count_words, count_chars, sort_by, sort_for_book_report
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    sorted_char_dict = sort_for_book_report(char_count)
    print(f"""============ BOOKBOT ============
          \nAnalyzing book found at {book_path}
          \n----------- Word Count ----------
          \nFound {word_count} total words words found
          \n--------- Character Count -------""")
    for c in sorted_char_dict:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("\n============= END ===============")
        


main()
