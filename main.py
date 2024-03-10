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
            if char.isalpha():
                if char in results:
                    results[char] += 1
                else:
                    results[char] = 1

        return results

def sort_on(dict):
    return dict["num"]

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count_words()} words found in the document")
print("")

output = []
letters = count_letters()
for letter in letters:
    output.append({"name": letter, "num": letters[letter]})

output.sort(reverse=True, key=sort_on)

for value in output:
    print(f"The '{value["name"]}' character was found {value["num"]} times")
print("--- End report ---")