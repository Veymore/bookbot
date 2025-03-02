def read_file_to_String(path):
    """
    Action:     Reads a file at the specified path and returns its file content as String
    In:         path -> String
    Out:        String
    """
    return open(path, "r", encoding="utf-8").read()
