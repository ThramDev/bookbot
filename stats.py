def get_word_count(book):
    words = []
    words = book.split()
    return len(words)

def get_characters_dict(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_character_list(characters_dict):
    sorted_list = []
    for character in characters_dict:
        if character.isalpha():
            num = characters_dict[character]
            sorted_list.append({"char": character, "num": num})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list