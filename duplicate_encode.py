def duplicate_encode(word):
    """
    Encode the string by replacing each character with '(' if the character appears only once in the string,
    or ')' if the character appears more than once.

    Args:
        word (str): The input string to encode.

    Returns:
        str: The encoded string.
    """
    lowercase_word = word.lower()
    char_count = {}
    for char in lowercase_word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return "".join(["(" if char_count[char] == 1 else ")" for char in lowercase_word])


print(duplicate_encode("Success"))
print(duplicate_encode("recede"))
print(duplicate_encode("(( @"))
print(duplicate_encode("din"))
