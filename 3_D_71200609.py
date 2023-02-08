#Nama : Airell Aristo Subagia 
#NIM  : 71200609

angka = int(input("Masukkan Angka : "))

for i in range(angka*2-1): 
    for j in range(i-1):
        print("* ",end="")
    print(" ")