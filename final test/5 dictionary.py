# =========================================
#   Dictionary Produk Skincare (Moisturizer)
#   By: Muttia Zalzabila.S
# =========================================

moisturizer = {
    "nama_produk": "Moisturizer",
    "manfaat": "Melembabkan kulit",
    "isi": "50 ml",
    "harga": 100000
}

print("=== DATA MOISTURIZER ===")
for key, value in moisturizer.items():
    print(f"{key.replace('_', ' ').capitalize()} : {value}")
