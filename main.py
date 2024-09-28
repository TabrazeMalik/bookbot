def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    print(file_contents)
    count = count_words(file_contents)
    print(count)

    letter_counts = count_letters(file_contents)
    for letter, count in letter_counts.items():
        print(f"{letter}:{count}")

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    unique_letters = set(text)
    counts = {}
    
    for letter in unique_letters:
        counts[letter] = 0

    for letter in text:
        counts[letter] += 1

    return counts
    
main()
