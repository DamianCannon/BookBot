def main():
    # Open book and print to console
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    # Open book and print to console
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return len(file_contents.split())

print(f"Number of words in document: {count_words()}")
