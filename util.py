A_ORD = 97

def print_separator():
    print('--------------')

def index_to_char(i):
    return chr(i + A_ORD)

def char_to_index(char):
    return ord(char) - A_ORD
