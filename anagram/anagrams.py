def reversed_words(text):
    if not isinstance(text, str):
        raise TypeError
    text_list = text.split()
    reverse_text = []
    for word in text_list:
        word_list = list(word)
        letters_alpha = []
        for index, letter in enumerate(word_list):
            if letter.isalpha():
                letters_alpha.append(letter)
                word_list[index] = ''
        for index, letter in enumerate(word_list):
            if letter == '':
                word_list[index] = letters_alpha.pop()
        reverse_text.append(''.join(word_list))
    return ' '.join(reverse_text)
