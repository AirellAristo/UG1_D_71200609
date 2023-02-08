#Nama : Airell Aristo Subagia 
#NIM  : 71200609

count = 0
kalimat = str(input("Kalimat Yang Ingin Diteliti : "))
cari  = str(input("Kata Yang Ingin Dicari : "))

kKecil = kalimat.lower()
cKecil = cari.lower()
sCari = cKecil.strip(" ")

kList = kKecil.split(" ")
for i in kList :
    if i == sCari : 
        count += 1
print("Jumlah Kata Yang Dicari : ",count)