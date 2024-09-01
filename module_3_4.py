def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.startswith(root_word):
            same_words.append(i)
    return same_words


result = single_root_words("при", 'приход', 'прилагательное', "купить", "прием", "первый")
print(result)
