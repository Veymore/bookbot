from stats import count_letter, count_words


def print_report(text, book_path="undefined"):
    """
    Action:     Calls count_letter,
                Sorts Dictionary,
                Iterates over given Dictionary.
                Filters characters that are not in the alphabet.
                Prints a report of character occurences in human readable format.
    In:         text -> String
    Out:        -
    """
    report_begin = f"""
{'-'*3} Begin report of {book_path} {'-'*3}
{count_words(text)} words found in the document

"""
    report_end = f"{'-'*3} End report {'-'*3}"
    full_report = report_begin
    # Call counter_letter
    # -> use sorted() to create a sorted list
    # -> use items() to convert dictionary into a list of key-value tuples
    # -> use lambda x:x[1] to use the 2nd value of the k-v tuples
    # -> use reverse to sort in ascending order
    character_sorted_list = sorted(
        count_letter(text).items(), key=lambda x: x[1], reverse=True
    )
    # Convert back to a dictionary
    character_sorted_dict = dict(character_sorted_list)
    # Iterate over given Dictionary
    for char in character_sorted_dict:
        # Filter characters that are not in the alphabet
        if char.isalpha():
            full_report += f"The '{char}' character was found {character_sorted_dict[char]} times\n"
    full_report += report_end
    # Prints a report of character occurences in human readable format.
    print(full_report)
