def string_to_binary(string):
    return ' '.join(format(ord(char), '08b') for char in string)
