from char_utils import char_to_num, num_to_char
from math_utils import modular_inverse

# Función de encriptado del Criptosistema 1
def encrypt_cryptosystem1(text, a, b):
    encrypted_text = ""
    for char in text.upper():
        if char in char_to_num:
            x = char_to_num[char]
            encrypted_value = (a * x + b) % 29
            encrypted_text += num_to_char[encrypted_value]
    return encrypted_text

# Función de desencriptado del Criptosistema 1
def decrypt_cryptosystem1(encrypted_text, a, b):
    decrypted_text = ""
    a_inv = modular_inverse(a, 29)
    if a_inv is None:
        raise ValueError("No existe inverso modular para 'a'.")
    
    for char in encrypted_text.upper():
        if char in char_to_num:
            y = char_to_num[char]
            decrypted_value = (a_inv * (y - b)) % 29
            decrypted_text += num_to_char[decrypted_value]
    return decrypted_text
