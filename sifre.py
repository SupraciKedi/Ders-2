import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

soru = int(input("Parola uzunluğunu girin: "))

parola = ""

for _ in range(soru):
    parola += random.choice(karakter)

print("Oluşturulan Parola:", parola)
