def main():
    # Open book and print to console
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    # Open book and count words
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return len(file_contents.split())
        
def count_letters():
    # Open book and count letters
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_file_contents = file_contents.lower()

        results = {}
        for char in lower_file_contents:
            if char in results:
                results[char] += 1
            else:
                results[char] = 1

        return results

print(f"Number of words in document: {count_words()}")
print(f"Number of letters in document: {count_letters()}")
