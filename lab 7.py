
#http://pemrograman-sederhana.blogspot.com/2014/09/menghitung-singkatan
# huruf-dan-konsonan-di_99.html
'''
alex merupakan seorang artis nama panggungnya adalah Bang Tatap buatlah sebuah program dimana 
ketika alex menginput sebuah huruf maka akan keluar nama panggungnya dan hitunglah huruf sesuai inputan user


kalimat = kalimat inputan user
singkatan = nama singkatan user
dicari = singkatan yang akan di hitung jumlahnya 
huruf = string/huruf disimpan lalu dihitung

#input :kalimat = inputan user ; singkatan = nama singkatan ; dicari = huruf yang mau dihitung

#proses :
membuat inputan kalimat,singkatan dan dicari
melakukan perulangan kalimat,singkatan dan dicari
melakukan percabangan mengecek nama panggung sama menghitung huruf sesuai inputan 

#output :
menampilkan hasil nama panggung 
menampilkan jumlah huruf sesuai inputan 

'''

kalimat = str(input("masukkan kalimat :")).lower()
singkatan = str(input("masukkan singkatan :"))
dicari = str(input("huruf yang mau dihitung :"))
huruf =""
for jaja in kalimat:
    for zizi in singkatan:
        if zizi == singkatan:
            kalimat = kalimat.replace(zizi,"Bang Tatap")
        if jaja in dicari :
            huruf += jaja
print("hasilnya adalah",kalimat)
print(len(huruf))

