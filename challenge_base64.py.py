import base64

hex_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# 1. Conversion hexadécimal -> octets
bytes_data = bytes.fromhex(hex_str)

# 2. Encodage octets -> Base64
b64_bytes = base64.b64encode(bytes_data)

# 3. Conversion en chaîne de caractères ASCII
b64_str = b64_bytes.decode('utf-8')

print(b64_str)
# Résultat : cTypto/Basi+6+Ek3Knang+qz5Z+f