#######################################################################################################
#   Universidad Nacional Autónoma de México - Facultad de Ingeniería
#   Materia Criptografía    Grupo: 02   Semestre:2025-2
#   Proyecto final - Cifrado simétrico AES
# 
#   Integrantes:
#       - Rivera González Frida Alison
#       - Frías Hernández Camille Emille Román
#       - Hernández Vázquez Daniela 
#       - Zamudio González Nathalia Danae
# 
#   Fecha de entrega: 18 de mayo de 2025
#######################################################################################################
#   El siguiente programa muestra el algoritmo de cifrado simétrico AES en Python.
#######################################################################################################

s_box = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,     # Substitution Box usada por AES para la transformación SubBytes.
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

r_con = [
    0x00000000, 0x01000000, 0x02000000, 0x04000000,             # Constantes de ronda usadas en la expansión de la clave AES.
    0x08000000, 0x10000000, 0x20000000, 0x40000000,
    0x80000000, 0x1b000000, 0x36000000
]

def sub_bytes(state):
    return [s_box[b] for b in state]   # Aplica la s_box a cada byte del estado.

def shift_rows(state):      
    return [
        state[0],  state[5],  state[10], state[15],            # Rota las filas de la matriz de estado (matriz de 4x4)
        state[4],  state[9],  state[14], state[3],             #    y esta función simula el desplazamiento de filas.
        state[8],  state[13], state[2],  state[7],
        state[12], state[1],  state[6],  state[11]
    ]

def xtime(a):
    return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)       

def mix_columns(state):                # Mezcla los datos de cada columna de la matriz de estado.
    result = []
    for i in range(4):
        col = state[i*4:(i+1)*4]
        t = col[0] ^ col[1] ^ col[2] ^ col[3]
        result.append(col[0] ^ t ^ xtime(col[0] ^ col[1]))
        result.append(col[1] ^ t ^ xtime(col[1] ^ col[2]))
        result.append(col[2] ^ t ^ xtime(col[2] ^ col[3]))
        result.append(col[3] ^ t ^ xtime(col[3] ^ col[0]))
    return result

def add_round_key(state, round_key):                            # XOR entre el estado y la clave de ronda.
    return [b ^ k for b, k in zip(state, round_key)]

def key_expansion(key):                 # Claves para cada ronda del cifrado, expande clave de 16 bytes a 176 bytes (11 rondas de 16 bytes).
    def rot_word(word):
        return word[1:] + word[:1]

    def sub_word(word):
        return [s_box[b] for b in word]

    key_symbols = [b for b in key]
    w = [key_symbols[i:i+4] for i in range(0, 16, 4)]

    for i in range(4, 44):
        temp = w[i-1]
        if i % 4 == 0:
            temp = sub_word(rot_word(temp))
            temp[0] ^= (r_con[i//4] >> 24) & 0xFF
        w.append([a ^ b for a, b in zip(w[i-4], temp)])

    return [b for word in w for b in word]

def aes_encrypt_block(block, key_schedule):                     # Cifra un solo bloque de 16 bytes: Aplica AddRoundKey inicial (9 rondas)

    state = list(block)
    state = add_round_key(state, key_schedule[:16])

    for r in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key_schedule[16*r:16*(r+1)])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_schedule[160:176])

    return state

def pad_pkcs7(data, block_size=16):                             # Aplica relleno para que su longitud sea múltiplo de 16 bytes.
    padding_len = block_size - (len(data) % block_size)
    return data + bytes([padding_len] * padding_len)

def aes_ecb_encrypt(message, key):
    # Expande la clave
    key_schedule = key_expansion(key)

    # Aplica padding
    padded = pad_pkcs7(message)

    # Divide en bloques de 16 bytes
    blocks = [padded[i:i+16] for i in range(0, len(padded), 16)]

    # Cifra cada bloque
    encrypted = []
    for block in blocks:
        encrypted_block = aes_encrypt_block(block, key_schedule)
        encrypted.extend(encrypted_block)

    return encrypted

# Pedir entrada al usuario
mensaje = input("Ingresa el texto a cifrar: ").encode('utf-8')

# Pedir clave al usuario y validar que tenga 16 caracteres
clave_input = input("Ingresa la clave (16 caracteres): ")
if len(clave_input) != 16:
    raise ValueError("La clave debe tener exactamente 16 caracteres.")

clave = clave_input.encode('utf-8')

# Cifrar mensaje completo en modo ECB
cifrado = aes_ecb_encrypt(mensaje, clave)

# Mostrar en hexadecimal
print("Mensaje cifrado (hex):", ''.join(f'{b:02X}' for b in cifrado))

'''
# Texto de entrada
mensaje = b"Hola como estas mundo"  # 21 bytes
clave = b"abcdefghijklmnop"         # 16 bytes

# Cifrar mensaje completo en modo ECB
cifrado = aes_ecb_encrypt(mensaje, clave)

# Mostrar en hexadecimal
print("Mensaje cifrado (hex):", ''.join(f'{b:02X}' for b in cifrado))
'''