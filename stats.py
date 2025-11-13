def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char = {}
    for c in text:
        if c in char:
            char[c] += 1
        else:
            char[c] = 1
    return char

def sort_characters(item):
    return item["num"]

def chars_sorted_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(key=sort_characters, reverse=True)
    return char_list
