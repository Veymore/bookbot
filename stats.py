def count_words(text):
    """
    Action:     Takes a String, splits it into a list of words and
                returns the number of words in the given String
    In:         text -> String
    Out:        Integer
    """
    return len(text.split())


def count_letter(text):
    """
    Action:     Takes a String, iterates over every character
                saves and counts the number to occurences per character
    In:         text -> String
    Out:        Dictionary('char': 'number of occurences')
    """
    text = text.lower()
    letter_dict = {}
    for char in text:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    # debug:
    return letter_dict
