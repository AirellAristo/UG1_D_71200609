#Nama : Airell Aristo Subagia 
#NIM  : 71200609



#70 90 85  // 90  30  60


def perulangan (): 
    tHarian = 0
    tUts = 0
    tUas = 0
    for i in range (1,3): 
        print("------- Nilai ke",i,"-------")
        mHarian = int(input("Nilai Harian : "))
        mUts = int(input("Nilai UTS : "))
        mUas = int(input("Nilai UAS : "))
        tHarian += mHarian
        tUts += mUts
        tUas += mUas
    return [tHarian/2,tUts/2,tUas/2]

def operator() : 
    hasil = perulangan()
    oHarian =  hasil[0] * 30/100
    oUts = hasil[1] * 30/100
    oUas = hasil[2] * 40/100
    total = oHarian + oUts + oUas
    return total

def percabangan() : 
    huruf = operator()
    if huruf >= 0 and huruf <= 19  :
        print("Total nilai yang didapat : ",huruf)
        print("Total Nilai Dalam Huruf : E")
    if huruf >= 20 and huruf <= 39 : 
        print("Total nilai yang didapat : ",huruf)
        print("Total Nilai Dalam Huruf : D")
    if huruf >= 40 and huruf <= 59 :
        print("Total nilai yang didapat : ",huruf)
        print("Total Nilai Dalam Huruf : C")
    if huruf >= 60 and huruf <= 79 :
        print("Total nilai yang didapat : ",huruf)
        print("Total Nilai Dalam Huruf : B")
    if huruf >= 80 and huruf <= 100 :
        print("Total nilai yang didapat : ",huruf)
        print("Total Nilai Dalam Huruf : A")
    

percabangan()