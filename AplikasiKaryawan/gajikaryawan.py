''' Program contoh penerapan class di Python
Program ini dibuat untuk mengerti konsep OOP di Python 

# OOP in Python, mempelajari Object Oriented Programming  di Python . Method = class
 untuk bahan pembelajaran... dibuat oleh Rian Irawan Hariadi


Program ini menentukan berapa jumlah akhir gaji yang diterima berdasarkan kondisi berikut:

  - Angka UMR ditentukan
1 - Gaji berdasarkan posisi jabatan (OB, staff, supervisor, manager) dan/atau lama pengalaman (experience)
  - Gaji OB HARUS dibawah UMR
2 - Gaji kotor dipotong pajak 10% , untuk gaji di atas UMR
3 - Gaji bersih akan dipotong tunjangan pensiun : 
- jika usia < 30 pemotongan tunjangan 10% gaji
- jika usia 30-40 pemotongan tunjangan 15% gaji
- jika usia di atas 40, pemotongan 20% gaji
4 - Terakhir, jika karyawan Pria, maka dari hasil akhir masih dipotong lagi 5% , untuk tunjangan keluarga

DAN MARI KITA BUAT PROGRAMNYA...

'''
from PotonganGaji.Potongan import Pajak,Tunjangan

class Karyawan:

	def __init__(self,first,last,sex,rank,age,exp,pay):
		self.first = first
		self.last = last
		self.sex = sex
		self.rank = rank
		self.age = age
		self.exp = exp #experience
		self.pay = pay
		self.pajak = Pajak().PotonganPPN()

	def GajiKotor(self):
		return self.pay 

	def GajiBersih(self):
		self.paynow = self.GajiKotor()
		pajak = self.pajak
		# pajak = int(pajak)
		if self.paynow < 4000000:
			GajiBersih = self.paynow
		else:
			GajiBersih = self.paynow - ( pajak * self.paynow)
		return GajiBersih 

	def set_NaikGaji(self):
		gaji = self.GajiKotor()
		gaji += ( 0.2 * gaji )
		self.pay = gaji
		return self.pay
		
	def get_NaikGaji(self):
		gaji = self.GajiKotor()
		gaji += ( 0.2 * gaji )
		return gaji
		'''di sini terlihat bahwa Python BERBEDA dengan Java, dia TIDAK MEMBEDAKAN metode get atau set , 
		asalkan tidak merubah isi variable self, maka dia akan 'hanya' sebatas get '''

# Diimport dari modul Potongan
pajak = Pajak().PotonganPPN()
print('Pajak PPN module:' ,pajak)

emp_1 = GajiKaryawan('Rian','Hariadi','L','Manager',34,5,6500000)
emp_2 = GajiKaryawan('Budi','Santorso','L','Staff',31,3,3500000)

# print ('Class dict:' , GajiKaryawan.__dict__)
# print('List Dict:' , emp_1.__dict__)

print('Gaji skr: ' ,emp_1.GajiBersih())
print(emp_2.GajiBersih())

print("Apabila Gaji dinaikkan .. (metode get) ")
print(emp_1.get_NaikGaji())
print('Gaji skr: ' , emp_1.GajiBersih())



print("Sekarang Gaji dinaikkan .. (metode Set) ")

print('Gaji skr:', emp_1.set_NaikGaji())
print('Gaji skr, setelah pajak:' ,emp_1.GajiBersih())
