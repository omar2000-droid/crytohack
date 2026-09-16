from pwn import xor

# pwn.xor applique l'opération directement sur des chaînes ou octets
result_bytes = xor("label", 13)
new_string = result_bytes.decode('utf-8')

print(f"crypto{{{new_string}}}")
# Résultat : crypto{alnao}