from report import print_report
from filesystem_interactions import read_file_to_String
import sys


def main():
    """
    Action:     Main function, dictates the flow of the program
    In:         -
    Out:        -
    """
    if len(sys.argv) > 1:
        path_to_file = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    try:
        book_text = read_file_to_String(path_to_file)
    except FileNotFoundError:
        print(f"File not found at {path_to_file}")
        sys.exit(1)
    # count_letter(book_text)
    print_report(book_text, path_to_file)


## dont edit below ##

if __name__ == "__main__":
    main()
