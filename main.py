'''
Action:     Reads a file at the specified path and returns its file content as String
In:         path -> String
Out:        String
'''
def read_file_to_String(path):
    return open(path, "r", encoding="utf-8").read()


'''
Action:     Takes a String, splits it into a list of words and 
            returns the number of words in the given String
In:         text -> String
Out:        Integer
'''
def count_words(text):
    return len(text.split())

'''
Action:     Takes a String, iterates over every character
            saves and counts the number to occurences per character
In:         text -> String
Out:        Integer
'''
def count_letter(text):
    text = text.lower()
    letter_dict = {}
    for char in text:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    #debug:
    return letter_dict

'''
Action:     Main function, dictates the flow of the program
In:         -
Out:        -
'''
def main():
    repository_path = "/Users/julian/Desktop/repos/boot.dev/bookbot/"
    path_to_file = "books/frankenstein.txt"
    book_path = repository_path + path_to_file
    book_text = read_file_to_String(book_path)
    count_letter(book_text)

## dont edit below ##

main()