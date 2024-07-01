def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()
    same_words = []
    for i in other_words:
        if root_word_lower in i.lower() or i.lower() in root_word_lower:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

