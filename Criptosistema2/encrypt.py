import numpy as np
from conversion import text_to_blocks, block_to_vector, blocks_to_text

def encrypt_cryptosystem2(text, T, b):
    blocks = text_to_blocks(text)
    encrypted_blocks = []
    for block in blocks:
        vector = block_to_vector(block)
        encrypted_vector = (np.dot(T, vector) + b) % 29
        encrypted_blocks.append(encrypted_vector)
    return encrypted_blocks
