from stats import count_words, count_letter
from report import print_report
from filesystem_interactions import read_file_to_String


def main():
    """
    Action:     Main function, dictates the flow of the program
    In:         -
    Out:        -
    """
    repository_path = "/Users/julian/Desktop/repos/boot.dev/bookbot/"
    path_to_file = "books/frankenstein.txt"
    book_path = repository_path + path_to_file
    book_text = read_file_to_String(book_path)
    # count_letter(book_text)
    print_report(book_text, path_to_file)


## dont edit below ##

if __name__ == "__main__":
    main()
