# Tugas Praktikum
class Mahasiswa:
    data = {}

    def __init__(self, nama, nilai) -> None:
        self.nama = nama
        self.nilai = nilai

    def tambah(nama, nilai):                # untuk menambah data
        a = Mahasiswa.data[nama] = nilai

    def tampilkan(a):                       # untuk menampilkan data
        return Mahasiswa.data

    def hapus(nama):                        # untuk menghapus data berdasarkan nama
        print('menghapus data', nama)
        if nama in Mahasiswa.data.keys():
            del Mahasiswa.data[nama]
        return nama, 'sudah dihapus'

    def ubah(nama):                         # untuk mengubah data berdasarkan nama
        print('mengubah data ', nama)
        if Mahasiswa.data.keys():
            del Mahasiswa.data[nama]
            nama = input("Nama baru: ")
            nilai = input('Nilai baru: ')
        Mahasiswa.data[nama] = nilai

print('Menambah data')
print(Mahasiswa.tambah('Davin', 18))
print(Mahasiswa.tambah('Ariel', None))
print()
print('menampilkan data')
print(Mahasiswa.tampilkan(Mahasiswa.data))
print()
print(Mahasiswa.ubah('Ariel'))
print()
print(Mahasiswa.hapus('Dani'))
print()
print('menampilkan data lagi')
print(Mahasiswa.tampilkan(Mahasiswa.data))