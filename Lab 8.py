class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    @staticmethod
    def tampilkan(nama, nilai):        # untuk menampilkan data
        tampil = {
            nama:nilai
        }
        print(tampil)

    @staticmethod
    def tambah(cls):     # untuk menambah data
        # a = data[nama] = nilai

    @staticmethod
    def hapus(nama):                        # untuk menghapus data berdasarkan nama
        # print('menghapus data', nama)
        # if nama in data.keys():
        #     del data[nama]
        # return nama, 'sudah dihapus'
        return

    @staticmethod
    def ubah(nama):                         # untuk mengubah data berdasarkan nama
        # print('mengubah data ', nama)
        # if data.keys():
        #     del data[nama]
        #     nama = input("Nama baru: ")
        #     nilai = input('Nilai baru: ')
        # data[nama] = nilai


mic = input('Tambah/Tampilkan/Hapus/Ubah : ')       # Expected indented block
# if mic=='Tambah':
#     Mahasiswa()


nama = input('Nama Anda: ')
nilai = str(input('Nilai Anda: '))

# a = Mahasiswa(nama,nilai)
# a.tampilkan()
