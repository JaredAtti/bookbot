def main():
    book_path = "books/frankenstein.txt"

    print_report(book_path)

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

def print_report(path):
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_dict = get_chars(text)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")

    listed_chars = dictToList(char_dict)
    listed_chars.sort(reverse=True, key=sort_on)
    
    for i in listed_chars:
        print(f"The '{i['char']}' character was found {i['count']} times")

    print(f"--- End Report ---")


def dictToList(dict):
    converted = []
    for i in dict:
        if i.isalpha():
            converted.append({"char": i, "count": dict[i]})
    
    return converted

def sort_on(dict):
    return dict["count"]

main()