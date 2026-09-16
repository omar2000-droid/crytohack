label_string = "label"

# XOR de chaque caractère (converti en ordinal ASCII) avec 13
res_chars = [chr(ord(char) ^ 13) for char in label_string]

# Assemblage des caractères en chaîne
new_string = "".join(res_chars)

print(f"crypto{{{new_string}}}")
# Résultat : crypto{alnao}