from Crypto.Util.number import long_to_bytes

# L'entier donné dans le défi
number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Conversion de l'entier long vers des octets
message_bytes = long_to_bytes(number)

# Décodage en chaîne de caractères ASCII/UTF-8
flag = message_bytes.decode('utf-8')

print(flag)
# Résultat : crypto{HEX_to_Base64_is_a_useful_tool}