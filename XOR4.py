# Données chiffrées en hexadécimal
data = bytes.fromhex(
    "73626960647f6b206821204f21254f7d694f766462066262127234f72629756d"
)

# Tester toutes les clés possibles (de 0 à 255)
for key in range(256):
    decoded = bytes(b ^ key for b in data)
    
    # Validation incluant l'ASCII imprimable (32-126) ainsi que \t, \n et \r
    if all(32 <= b <= 126 or b in (9, 10, 13) for b in decoded):
        print(f"Clé = {key} ({hex(key)}) -> {decoded.decode('ascii')}")