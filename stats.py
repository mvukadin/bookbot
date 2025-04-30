def num_words(all_text):
    words = all_text.split()
    return len(words)

def character_count(all_text):
    char_dict = {}
    all_text = all_text.lower()
    for char in all_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_char_count(dict_item):
    return dict_item['num']

def sort_characters(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        dict_list.append({'char':key, 'num':value})
    dict_list.sort(key=get_char_count, reverse=True)
    return dict_list