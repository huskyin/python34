''' Program python donatur.py

'''

class Donasi:

	total_donasi = 0

	def __init__(self,donatur_str):
		nama,alamat,jenis,jumlah = donatur_str.split('==')
		self.nama = nama
		self.alamat = alamat
		self.jenis = jenis
		self.jumlah = jumlah

		Donasi.total_donasi += int(self.jumlah)

	def __str__(self):
		return '\n Pengirim: ' + str(self.nama) + '\n Alamat: ' + \
		str(self.alamat) + '\n Jenis: ' + str(self.jenis) + '\n Jumlah: ' + str(self.jumlah)

donatur_str_1 = 'Irfan==Jl. Sukarno Hatta No.20, Jepara==donasiuang==200000'
donatur_str_2  = 'Ardi==Jambutimur, Mlonggo Jepara==donasiuang==1000000'
donatur_str_3  = 'Indah==Tahunan, Jepara==donasiuang==50000'

print('===== Input : =========')
print(donatur_str_1)
print(donatur_str_2)
print(donatur_str_3)

print('=== Output: =======')
donasi_1 = Donasi(donatur_str_1)
donasi_2 = Donasi(donatur_str_2)
donasi_3 = Donasi(donatur_str_3)

print(donasi_1)
print(donasi_2)
print(donasi_3)

print ('\n Total donasi uang: ', Donasi.total_donasi)
