def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_chars(text)

    # print(f"{num_words} words found in the document")
    print(char_dict)



def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars(text):
    dict = {}
    for i in text:
        c = i.lower()
        dict[c] = dict.get(c, 0) + 1
    return dict

main()