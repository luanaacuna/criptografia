import numpy as np
from encrypt import encrypt_cryptosystem2
from decrypt import decrypt_cryptosystem2
from conversion import blocks_to_text

# Ejemplo de uso para el Criptosistema 2
T = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1]
])  # Determinante = 1
b_vector = np.array([[2], [3], [4]])  # Vector constante

# Verificar que T es válida
if np.linalg.det(T) % 29 != 1:
    raise ValueError("La matriz T no tiene determinante 1. Por favor, elige otra matriz.")

# Encriptar
original_text_2 = "LA CULPA ES DE CATARINA"
encrypted_blocks_2 = encrypt_cryptosystem2(original_text_2, T, b_vector)
encrypted_text_2 = blocks_to_text(encrypted_blocks_2)

# Desencriptar
encrypted_vectors = [np.array(block) for block in encrypted_blocks_2]
decrypted_blocks_2 = decrypt_cryptosystem2(encrypted_vectors, T, b_vector)
decrypted_text_2 = blocks_to_text(decrypted_blocks_2)

# Remover espacios de relleno adicionales
decrypted_text_2 = decrypted_text_2[:len(original_text_2)]

# Resultados
print("Criptosistema 2:")
print("Texto Original:", original_text_2)
print("Texto Encriptado:", encrypted_text_2)
print("Texto Desencriptado:", decrypted_text_2)
