# Función para calcular el inverso modular
def modular_inverse(a, mod):
    for i in range(mod):
        if (a * i) % mod == 1:
            return i
    return None

# Letra que más se repite en un texto
from collections import Counter
from char_utils import char_to_num
def char_repeated(text):
    filtered_text = [char for char in text if char in char_to_num]
    freq = Counter(filtered_text)
    most_common = freq.most_common(1)[0]
    positions = [idx for idx, char in enumerate(text) if char == most_common[0]]
    return most_common[0], most_common[1], positions
