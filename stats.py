def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    char_count = {}

    for ch in text:
        ch = ch.lower()
        if ch  not in char_count:
            char_count[ch] = 1
        else:
            char_count[ch] += 1

    return char_count

def get_sorted_list_of_alpha_chars(text):
    char_count = {}

    for ch in text:
        if not ch.isalpha():
            continue
        ch = ch.lower()
        if ch  not in char_count:
            char_count[ch] = 1
        else:
            char_count[ch] += 1

    return char_count

def get_sorted_list(char_count_dict):
    char_dict = [{"char": k, "num": v} for k,v in char_count_dict.items() if k.isalpha() ]
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict


def sort_on(items):
    return items["num"]