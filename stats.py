def word_counter_funct(text_a):
    word_list = text_a.split()
    return len(word_list)

def get_chars_dict(text):
    char_dict = {}
    for l in text:
        lowercase_t = l.lower()
        if lowercase_t in char_dict:
            char_dict[lowercase_t] += 1
        else:
            char_dict[lowercase_t] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def make_dict_list(dict_of_char):
    sorted_dict_list = []
    for a in dict_of_char:
        sorted_dict_list.append({"char": a, "num": dict_of_char[a]})
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list