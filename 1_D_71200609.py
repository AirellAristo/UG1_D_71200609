#Nama : Airell Aristo Subagia 
#NIM  : 71200609


harga = 0 
print("========== Kasir ==========")
tambah = int(input("Harga Barang : "))
harga += tambah
pilihan = input("Apakah anda membeli barang lagi [yes/no]: ")

if pilihan == "yes" or pilihan == "no" :
    while "yes" in pilihan or "no" in pilihan : 
        if "yes" in pilihan or "no" in pilihan :
            if "yes" in pilihan : 
                tambah = int(input("Harga Barang : "))
                harga += tambah
                pilihan = input("Apakah anda membeli barang lagi [yes/no]: ")
            if "no" in pilihan : 
                print("Total belanja : ",harga)
                break
        if pilihan != "yes" or pilihan != "no" : 
            print("INVALID INPUT")
            break
else :
    print("INVALID INPUT")
    


    
        
    