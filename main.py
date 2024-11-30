def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_num_characters(text)
    print(characters)


def get_num_characters(text):
    characters = {}
    for char in text.lower():
        count = characters.get(char, 0) + 1
        characters[char] = count
    return characters


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
