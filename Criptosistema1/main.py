from cryptosistem1 import encrypt_cryptosystem1, decrypt_cryptosystem1
from math_utils import char_repeated

if __name__ == "__main__":
    # Criptosistema 1
    original_text_2 = "LA CULPA ES DE CATARINA"
    original_text_1 = "A Maglis Mujica y Armando Hernandez les gusta este proyecto y le ponen nota maxima saludos besos abrazos"
    a, b = 11, 19

    # Encriptar
    encrypted_text_1 = encrypt_cryptosystem1(original_text_1, a, b)
    # Desencriptar
    decrypted_text_1 = decrypt_cryptosystem1(encrypted_text_1, a, b)

    # Resultados
    print("Criptosistema 1:")
    print("Texto Original:", original_text_1)
    print("Texto Encriptado:", encrypted_text_1)
    print("Texto Desencriptado:", decrypted_text_1)

# Resultado para el texto
print("")
most_common_original = char_repeated(original_text_1)
print("Letra más repetida (original):", most_common_original)
print("")
most_common_original = char_repeated(encrypted_text_1)
print("Letra más repetida (encriptado):", most_common_original)
print("")