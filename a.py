SPECIAL_CHARACTERS = ["_", "(", "?", ".", ",", ";", ":", "!", "\"", "\\\\", "\n", ")", "�", " ", "“", "”"]

def count_occurrences_in_text(word_or_phrase, text):
    """
    Return the number of occurrences of the provided word or phrase (case-insensitive) in the given text.
    If the word_or_phrase contains multiple words, it checks if they occur consecutively.
    """
    word_or_phrase = word_or_phrase.lower()
    text = text.lower()
    
    # Remove consecutive double quotes at the beginning and end of the text
    text = re.sub(r"^''+", "", text)
    text = re.sub(r"''+$", "", text)

    _text = text.split(word_or_phrase)

    previous_item = _text[0]
    count = 0

    if len(_text) > 1:
        for item in _text[1:]:
            if (previous_item == ''  or previous_item[-1] in SPECIAL_CHARACTERS):
                if(item == '' or item[0] in SPECIAL_CHARACTERS):
                    count += 1
            previous_item = item 
    elif text == word_or_phrase:
        count = 1

    return count
