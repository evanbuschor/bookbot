

def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    total_words = count_words(book_text)
    letters_dict = count_letters(book_text)
    display_report(book_path, total_words, letters_dict)

def read_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    words = text.split(" ")
    return len(words)

def count_letters(text):
    text = text.lower()
    letters_dict = {}

    for char in text:
        if char in letters_dict:
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1

    return letters_dict

def display_report(book_path,word_count, letters):
    letters_list = []

    for letter in letters:
        letters_list.append({"name": letter, "count": letters[letter]})

    def sort_on(letter_dict):
        return letter_dict["count"]
    
    letters_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for letter_dict in letters_list:
        if letter_dict["name"].isalpha():
            print(f"The '{letter_dict["name"]}' character was found {letter_dict["count"]} times")
    print("--- End report ---")

main()