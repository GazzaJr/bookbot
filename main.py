def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    print(f"{num_words} words found in the document")
    print()
    print_letter_breakdown(letter_count)

def get_book_text(book_path):
    with open (book_path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    chars = {}
    
    for letter in text:
        lowered = letter.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def print_letter_breakdown(letters):
    sorted_letters = sorted(letters, key=letters.get, reverse=True)
    for letter in sorted_letters:
        if letter.isalpha():
            print(f"the letter {letter} was found {letters[letter]} times in the document")

main()