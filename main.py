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
Out:        Dictionary('char': 'number of occurences')
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
Action:     Calls count_letter, 
            Sorts Dictionary,
            Iterates over given Dictionary.
            Filters characters that are not in the alphabet.
            Prints a report of character occurences in human readable format.
In:         text -> String
Out:        -
'''
def print_report(text, book_path='undefined'):
    report_begin =  f"""
{'-'*3} Begin report of {book_path} {'-'*3}
{count_words(text)} words found in the document

"""
    report_end = f"{'-'*3} End report {'-'*3}"
    full_report = report_begin
    #Call counter_letter
    # -> use sorted() to create a sorted list
    # -> use items() to convert dictionary into a list of key-value tuples
    # -> use lambda x:x[1] to use the 2nd value of the k-v tuples
    # -> use reverse to sort in ascending order
    character_sorted_list = sorted(count_letter(text).items(), key=lambda x:x[1], reverse=True)
    #Convert back to a dictionary
    character_sorted_dict = dict(character_sorted_list)
    #Iterate over given Dictionary
    for char in character_sorted_dict:
        #Filter characters that are not in the alphabet
        if char.isalpha():
            full_report += (f"The '{char}' character was found {character_sorted_dict[char]} times\n")
    full_report += report_end
    #Prints a report of character occurences in human readable format.
    print(full_report)


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
    #count_letter(book_text)
    print_report(book_text, path_to_file)

## dont edit below ##

main()