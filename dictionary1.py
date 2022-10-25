# liste = list[] veya []
# sozluk dict() veya {}

# key - value
sozluk = {"merhaba":"hello","çıkış":"exit"}
print(len(sozluk))
print("Sözlükte {} eleman var.".format(len(sozluk)))

# Sözlükteki elemanlara ulaşmak
print(sozluk["çıkış"])

#Sözlüğe eleman eklemek
sozluk["makarna"] = "spagetti" # Mantık hatası
print(sozluk)

# Sözlükte olmayan bir eleman ?
#print(sozluk)["kayıt"]) ----HATALI KULLANIM----
# Bulunamayan veriler None döndürür.
print(sozluk.get("kayıt"))

# Sözlükte eleman düzenlemek
sozluk["makarna"] = "pasta"
print(sozluk)

# Sözlükten eleman silmek
del sozluk["çıkış"]
print(sozluk)

# Sözlüğün içerisini silmek
sozluk.clear()
print(sozluk)