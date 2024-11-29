import numpy as np
# Tabla de conversión: caracteres a números

char_to_num = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
    'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
    'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
}

num_to_char = {v: k for k, v in char_to_num.items()}

def text_to_blocks(text, block_size=3):
    text = text.upper()
    while len(text) % block_size != 0:
        text += " "
    return [text[i:i+block_size] for i in range(0, len(text), block_size)]

def block_to_vector(block):
    return np.array([char_to_num[char] for char in block]).reshape(-1, 1)

def vector_to_block(vector):
    return ''.join([num_to_char[int(round(num))] for num in vector.flatten()])

def blocks_to_text(blocks):
    return ''.join([vector_to_block(block) for block in blocks])
