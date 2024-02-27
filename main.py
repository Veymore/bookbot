repository_path = "/Users/julian/Desktop/repos/boot.dev/bookbot/"
path_to_file = "books/frankenstein.txt"
def print_file(path):
    f = open(path, "r", encoding="utf-8")
    print(f.read())

def main():
    print("debug main:")
    print_file(repository_path + path_to_file)

if __name__ == "__main__":
    main()