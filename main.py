def read_file_to_String(path):
    return open(path, "r", encoding="utf-8").read()

def count_words(text):
    return len(text.split())
    
def main():
    repository_path = "/Users/julian/Desktop/repos/boot.dev/bookbot/"
    path_to_file = "books/frankenstein.txt"
    book_path = repository_path + path_to_file
    book_text = read_file_to_String(book_path)
    print(count_words(book_text))

main()