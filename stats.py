def get_text_count(file_contents):
    words = file_contents.split()
    num_of_words = len(words)
    return num_of_words

def get_char_count(file_content):
    dict = {}
    for char in file_content:
        if char.lower() in dict:
            dict[char.lower()] += 1
        else:
            dict[char.lower()] = 1
    return dict

def sort_on(count_of_char):
    return [{'char':char, 'count':count} for char, count in count_of_char.items() if char.isalpha()]


def sorted_list_by_count(count_of_char):
    list_of_dicts = sort_on(count_of_char)
    return sorted(list_of_dicts, key= lambda x: x['count'], reverse=True)
    
    