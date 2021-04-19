def Daftarkaryawan (nama,nomor,asal):
    print('==========Daftar Karyawan==========')
    for index in range (0,len(nama)):
        print('nama:',nama[index],'nomor:',nomor[index],'asal:',asal[index])

nama=['Ivan','Deon','Nico','Adel']
nomor=['714970','713454','622192']
asal=['Solo','Surabaya','jakarta']
Daftarkaryawan(nama,nomor,asal)
