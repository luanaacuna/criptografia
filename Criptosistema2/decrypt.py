import numpy as np
from math_utils import modular_inverse
from conversion import blocks_to_text
# Desencriptar

def decrypt_cryptosystem2(encrypted_blocks, T, b):
    T_inv = np.linalg.inv(T)  # Inversa de la matriz T
    T_inv_mod = np.round(T_inv * np.linalg.det(T)).astype(int) % 29
    T_inv_mod = (T_inv_mod * modular_inverse(int(np.linalg.det(T)), 29)) % 29
    decrypted_blocks = []
    for block in encrypted_blocks:
        decrypted_vector = np.dot(T_inv_mod, (block - b)) % 29
        decrypted_blocks.append(decrypted_vector)
    return decrypted_blocks
