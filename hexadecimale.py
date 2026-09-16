hex_str = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Conversion de l'hexadécimal vers les octets
bytes_data = bytes.fromhex(hex_str)

# Affichage du texte (décodé en ASCII/UTF-8)
print(bytes_data.decode('utf-8'))
# Résultat : crypto{You_will_be_working_with_hex_strings_a_lot}