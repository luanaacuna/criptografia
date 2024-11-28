# Función para calcular el inverso modular
def modular_inverse(a, mod):
    for i in range(mod):
        if (a * i) % mod == 1:
            return i
    return None
