
# Importar las funciones necesarias del criptosistema
from cryptosistem1 import encrypt_cryptosystem1, decrypt_cryptosystem1
if __name__ == "__main__":
    # Criptosistema 1
    original_text_1 = "LA CULPA ES DE CATARINA"
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
