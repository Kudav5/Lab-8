

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def tampilkan(self):        # untuk menampilkan data
        tampil = {
            self.nama:self.nilai
        }
        print(tampil)

class data(Mahasiswa):
    def tambah(Mahasiswa):     # untuk menambah data
        a = data[nama] = nilai
    def hapus(nama):                        # untuk menghapus data berdasarkan nama
        print('menghapus data', nama)
        if nama in data.keys():
            del data[nama]
        return nama, 'sudah dihapus'
    def ubah(nama):                         # untuk mengubah data berdasarkan nama
        print('mengubah data ', nama)
        if data.keys():
            del data[nama]
            nama = input("Nama baru: ")
            nilai = input('Nilai baru: ')
        data[nama] = nilai


mic = input('Tambah/Tampilkan/Hapus/Ubah : ')
if mic=='Tambah':
    Mahasiswa()


nama = input('Nama Anda: ')
nilai = str(input('Nilai Anda: '))

a = Mahasiswa(nama,nilai)
a.tampilkan()
