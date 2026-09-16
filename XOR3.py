# Les valeurs fournies par le challenge
key1 = bytes.fromhex(
    "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
)

key2_xor_key1 = bytes.fromhex(
    "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
)

key2_xor_key3 = bytes.fromhex(
    "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
)

encrypted_flag = bytes.fromhex(
    "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
)


# Fonction XOR entre deux tableaux d'octets
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


# On part de :
#
# encrypted_flag = FLAG ^ KEY1 ^ KEY3 ^ KEY2
#
# On fait :
#
# encrypted_flag
# ^ KEY1
# ^ (KEY2 ^ KEY3)
#
# Les clés s'annulent :
#
# KEY1 ^ KEY1 = 0
# KEY2 ^ KEY2 = 0
# KEY3 ^ KEY3 = 0
#
# Il reste donc FLAG.


temp = xor_bytes(encrypted_flag, key1)

flag = xor_bytes(temp, key2_xor_key3)


# Affichage
print("Flag en hexadécimal :", flag.hex())
print("Flag :", flag.decode())