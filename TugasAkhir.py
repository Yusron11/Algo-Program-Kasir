import os
import json
from datetime import datetime


with open ('./DataTransaksi.json', 'r') as dt :
    laporan = json.load(dt)
with open ('./DataProduk.json', 'r') as dp :
    produk = json.load (dp)
with open ('./DataAkun.json', 'r') as da :
    akun = json.load (da)

def clear () : # FUNGSI MEMBERSIHKAN DATA SEBELUMNYA
    os.system('cls')

def beranda () : # FUNSI TAMPILAN AWAL
    clear ()
    while True :
        clear ()
        print ('='*50)
        print ('GROUP TENC STORE'.center(50))
        print ('='*50)
        print ('Menu : \n')
        print (f' 1. Masuk \n', '2, Daftar \n', '3. Keluar \n')
        pilih = input ('Pilih Menu Nomor ==>')
        if   pilih == '1' :
            masuk ()
        elif pilih == '2' :
            daftar ()
        elif pilih == '3' :
            break
        else :
            input ('Menu Tidak Tersedia')
            beranda ()
            break

def menu () : # FUNGSI PILIHAN MENU DAN MEMISAHKAN MENU BAGI ADMIN & PEMBELI
    global nama
    global user_
    global pass_
    global status 
    if status == 'admin' :
        while True :
            clear ()
            print ('='*50)
            print ('GROUP TENC STORE'.center(50))
            print ('='*50)
            print ('Menu : \n')
            print (f' 1. Data Produk \n', '2. Transaksi \n', '3. Kembali \n')
            pilih = input ('Pilih Menu Nomor ==>')
            if pilih == '1' :
                menu_produk ()
            elif pilih == '2' :
                menu_transaksi ()
            else :
                break
    elif  status == 'pembeli' :
        menu_transaksi ()


def daftar () : # FUNGSI MENDAFTAR ATAU MEMBUAT AKUN BARU
    clear ()
    print ('='*50)
    print ('DAFTAR'.center(50))
    print ('='*50)
    print ('\n')
    nama      = input ('Nama :')
    username  = input ('Username :')
    password  = input ('Password :')
    password2 = input ('Re-password :')
    for j in akun :
        i = j['username']
        if i == username :
            print ('\n')
            print ('USERNAME SUDAH DIGUNAKAN')
            input ('ENTER UNTUK MENGULANG PENDAFTARAN')
            break
        elif password2 != password :
            print ('\n')
            print ('PASSWORD TIDAK SAMA')
            input ('ENTER UNTUK MENGULANG PENDAFTARAN')
            break
    else :
        frmt = {'nama': nama, 'username' : username, 'password' : password, 'status' : 'pembeli'}
        akun.append(frmt)
        data = json.dumps(akun, indent = 2)
        with open ('./DataAkun.json', 'w') as tulis :
            tulis.write(data)
        print ('\n')
        print ('PENDAFTARAN BERHASIL')
        input ('ENTER UNTUK MASUK')
        
def masuk () : # FUNGSI Log In
    clear ()
    print ('='*50)
    print ('MASUK'.center(50))
    print ('='*50)
    print ('\n')
    global nama
    global user_
    global pass_
    global status
    username = input ('Username :')
    password = input ('Password :')
    if len(akun) != 0 :
        coba = False
        for i in akun :
            if i['username'] == username and i['password'] == password :
                coba   = True
                nama   = i['nama']
                user_  = i['username']
                pass_  = i['password']
                status = i['status']
            elif i['username'] == username and i['password'] != password :
                print ('\nPASSWORD SALAH, HARAP ULANG KEMBALI')
                input ('ENTER UNTUK KEMBALI')
            else :
                input ('ENTER UNTUK KEMBALI')
            break
    else :
        print ('BELUM ADA AKUN TERDAFTAR, SILAHKAN DAFTAR TERLEBIH DAHULU')
        input ('ENTER UNTUK KEMBALI')

    if coba :
        clear ()
        print ('BERHASIL MASUK')
        input ('ENTER UNTUK MELANJUTKAN')
        menu  ()


def daftar_produk () : # FUNNSI YANG MENAMPILKAN DAFTAR PRODUK
    clear ()
    print ('='*46)
    print ('GROUP TENC STORE'.center(46),'\n')
    print ('='*46)
    print ('%-2s | %-14s | %-12s | %-8s |'%( 'NO', 'NAMA', 'HARGA', 'STOK'))
    print ('='*46)
    for no, j in enumerate (produk) :
        print ('%-2s | %-14s | %-2s %-9s | %-4s %-3s |'%(no, j['nama'], 'Rp', j['harga'], j['stok'] , 'Pcs'))
    print ('='*46)

def tambah_produk () : # FUNGSI MENAMBAHKAN PRODUK DI TOKO
    clear ()
    print ('='*50)
    print ('TAMBAH PRODUK'.center(50))
    print ('='*50)
    print ('\n')
    nama    = input('Nama Produk :')
    harga   = int(input('Harga Produk : Rp.'))
    stok    = int(input('Stok Produk :'))
    frmt    = {'nama': nama, 'harga': harga, 'stok': stok}
    produk.append(frmt)
    daftar_produk()

def hapus_produk () : # FUNGSI MENGHAPUS / MENGURANGI PRODUK
    clear ()
    daftar_produk ()
    no    = int(input ('Pilih nomor data :'))
    produk.pop(no)
    daftar_produk ()

def simpan () : # FUNGSI MENYIMPAK PERUBAHAN SETELAH ADANYA PENAMBAHAN ATAU PENGHAPUSAN PRODUK
    data = json.dumps(produk, indent = 2)
    with open ('./Dataproduk.json', 'w') as tulis :
        tulis.write(data)
    daftar_produk()

def laporan_penjualan () :
    clear ()
    print ('='*76)
    print ('LAPORAN PENJUALAN'.center(76))
    print ('TENC STORE'.center(76))
    print ('='*76)
    print ('%-2s | %-16s | %-10s | %-12s | %-8s | %-12s |'%( 'NO', 'TANGGAL', 'NAMA', 'HARGA', 'JUMLAH', 'TOTAL HARGA'))
    print ('='*76)
    for no,j in enumerate (laporan) :
        print ('%-2s | %-16s | %-10s | %-2s %-9s | %-8s | %-2s %-9s |'%(no, j['tanggal'], j['nama'], 'Rp', j['harga'], j['jumlah'], 'Rp', j['total']))
    print ('='*76)


def menu_produk () : # FUNGSI UNTUK MENYATUKAN MENU-MENU TERKAIN PRODUK
    clear ()
    print ('='*50)
    print ('GROUP TENC STORE'.center(50))
    print ('='*50)
    print ('Menu : \n')
    while True :
        print (f' 1. Daftar Produk \n', '2. Tambah Produk \n', '3. Hapus Produk \n', '4. Simpan Data Produk \n', '5. laporan penjualan \n', '6. Kembali \n')
        pilih = input ('Pilih Menu Nomor ==>')

        if   pilih == '1':
            daftar_produk ()
        elif pilih == '2' :
            tambah_produk ()
        elif pilih == '3' :
            hapus_produk  ()
        elif pilih == '4' :
            simpan()
        elif pilih == '5' :
            laporan_penjualan ()
        else :
            clear()
            break


transaksi = []
total     = []
def keranjang () : # FUNGSI UNTUK MENAMPILKAN DAFTAR PRODUK YANG DITAMBAHKAN DI KERANJANG
    clear ()
    print ('='*62)
    print ('%-2s | %-10s | %-8s | %-12s | %-17s |'%( 'NO', 'NAMA', 'JUMLAH', 'HARGA', 'TOTAL HARGA'))
    print ('='*62)
    for no, j in enumerate (transaksi) :
        print ('%-2s | %-10s | %-3s %-4s | %-2s %-9s | %-2s %-14s |'%(no, j['nama'], j['jumlah'], 'Pcs', 'Rp', j['harga'], 'Rp', j['total']))
    print ('='*62)
    print ('%-41s : %-2s %-14s |'%('TOTAL BELANJA'.center(40), 'Rp', sum(total)))
    print ('-'*62)

def pesan () : # FUNGSI MENAMBAH BARANG YANG AKAN DIMASUKKAN KE DALAM KERANJANG
    clear ()
    daftar_produk ()
    no      = int (input('Pesan Barang Nomor :'))
    jumlah  = int (input('Jumlah Pesanan :'))
    nama    = produk[no]['nama']
    harga   = produk[no]['harga']
    stok    = produk[no]['stok']
    tanggal = datetime.today().strftime('%d-%B-%Y')
    if jumlah>= stok :
        print('STOK ', produk[no]['nama'], 'HABIS / KURANG DARI', jumlah)
    else:
        jm = {'stok' : stok - jumlah}
        produk[no].update(jm)
        frmt = {'tanggal': tanggal, 'nama': nama, 'harga': harga, 'jumlah': jumlah, 'total': jumlah*harga}
        transaksi.append(frmt)
        laporan.append(frmt)
        total.append(jumlah*harga)
        keranjang()

def hapus_pesanan () : # FUNGSI MENGHAPUS / MENGURANGI BARANG DALAM KERANJANG
    clear ()
    keranjang ()
    no = int(input('Hapus Pesanan Nomor :'))
    transaksi.pop(no)
    laporan.pop(no)
    total.pop(no)
    keranjang ()

def bayar () : # FUNGSI MELAKUKAN PEMBAYARAN BARANG-BARANG YANG ADA DALAM KERANJANG, SEKALIGUS MENYIMPANNYA SEBAGAI LAPORAN PEMBELIAN
    clear ()
    keranjang ()
    while True :
        bayar = int(input('Bayar : Rp.'))
        if bayar >= sum(total) :
            clear ()
            print ('GROUP TENC'.center(62))
            print ('LOCAL STREETWEAR STORE'.center(62))
            print ('\n')
            print ('='*62)
            print ('%-2s | %-10s | %-8s | %-12s | %-17s |'%( 'NO', 'NAMA', 'JUMLAH', 'HARGA', 'TOTAL HARGA'))
            print ('='*62)
            for no, j in enumerate (transaksi) :
                print ('%-2s | %-10s | %-3s %-4s | %-2s %-9s | %-2s %-14s |'%(no, j['nama'], j['jumlah'], 'Pcs', 'Rp', j['harga'], 'Rp', j['total']))
            print ('='*62)
            print ('%-41s : %-2s %-14s |'%('TOTAL BELANJA'.center(40), 'Rp', sum(total)))
            print ('-'*62)
            print ('%-41s : %-2s %-14s |'%('BAYAR'.center(32), 'Rp', bayar))
            print ('%-41s : %-2s %-14s |'%('KEMBALIAN'.center(36), 'Rp', bayar - sum(total)))
            print ('='*62)
            print ('\n')
            print ('THANK YOU'.center(62))
            print ('HAVE A NICE DAY'.center(62))
            print ('\n')
            data = json.dumps(laporan, indent= 2)
            with open ('./DataTransaksi.json', 'w') as tulis :
                tulis.write(data)
            p    = len(transaksi)
            q    = len(total)
            del transaksi [0:p]
            del total [0:q]
            input('ENTER UNTUK LANJUT')
            clear()
            break
        else :
            print('Uang Anda Kurang, Anda harus membayar sebesar Rp.', sum(total))

def menu_transaksi () : # FUNGSI MENYATUKAN MENU-MENU TRANSAKSI
    global nama
    clear ()
    print ('='*50)
    print ('GROUP TENC STORE'.center(50))
    print ('='*50)
    print ('SELAMAT DATANG |', nama, '\n')
    print ('Menu : \n')

    while True :
        print (f' 1. Keranjang \n', '2. Tambah Pesanan \n', '3. Hapus Pesanan \n', '4. Bayar \n', '5. Kembali \n')
        pilih = input ('Pilih Menu Nomor ==>')

        if   pilih == '1':
            keranjang ()
        elif pilih == '2' :
            pesan ()
        elif pilih == '3' :
            hapus_pesanan ()
        elif pilih == '4' :
            bayar ()
        else :
            break

beranda()
