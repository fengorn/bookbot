def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_words(book_text):
    word_list = book_text.split()
    return len(word_list)


def count_chars(book_text):
    chars = {}
    for c in book_text:
        c_lowered = c.lower()
        if c_lowered in chars:
            chars[c_lowered] = chars[c_lowered] + 1
        else:
            chars[c_lowered] = 1
    return chars


def sort_by(list_item):
    return list_item['num']


def sort_for_book_report(stat_dict):
    sorted_list = []
    for c in stat_dict:
        sorted_list.append({'char':c, 'num':stat_dict[c]})
    sorted_list.sort(key=sort_by, reverse=True)
    return sorted_list