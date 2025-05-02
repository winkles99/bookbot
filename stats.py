def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1           
        else:
            char_count[char] = 1

    return char_count

def chars_to_sorted_list(char_dict):
    chars_list = []
    for character, count in char_dict.items():
        char_data = {"char": character, "num": count}
        chars_list.append(char_data)
    
    def sort_on(dict): 
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
