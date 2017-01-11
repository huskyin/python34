''' Program contoh penerapan class di Python
Program ini dibuat untuk mengerti konsep OOP di Python 

# OOP in Python, mempelajari Object Oriented Programming  di Python . Method = class
 untuk bahan pembelajaran... dibuat oleh Rian Irawan Hariadi


Program ini menentukan berapa jumlah akhir gaji yang diterima berdasarkan kondisi berikut:

DAN MARI KITA BUAT PROGRAMNYA...

'''
from PotonganGaji.Potongan import Pajak,Tunjangan
import Bonus
from gajikaryawan import *

class Karyawan:

	def __init__(self,first,last,sex,rank,age,exp):
		self.first = first
		self.last = last
		self.sex = sex
		self.rank = rank
		self.age = age
		self.exp = exp #experience

	def __str__(self):
		return 'Nama: ' + str(self.first) + str(self.last) + ' , email: ' + str(self.set_email())
		
	def set_email(self):
		self.email = self.first + self.last + '@perusahaan.com' 
		return self.email

	# Classmethod bisa ebagai 'alternative constructor', menghemat penulisan daripada harus menulis self.*'
	@classmethod
	def from_string(cls,emp_str):
		first,last,sex,rank,age,exp = emp_str.split('-')
		return cls(first,last,sex,rank,age,exp)

	@classmethod
	def buat_email(cls,emp_str):
		first,last,sex,rank,age,exp = emp_str.split('-')
		# cls.buat_email = first + last + '@perusahaan.com'
		main_class = cls(first,last,sex,rank,age,exp)
		cls.buat_email = main_class.set_email()

	@staticmethod
	def shift_kerja(day):
		if day.weekday() == 5 or day.weekday() ==6 :
			return 'Hari ini Libur'
		return 'Hari Kerja'


class Gaji(Karyawan):

	def __init__(self,first,last,sex,rank,age,exp,pay):
		super().__init__(self,first,last,sex,rank,age)
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

	def set_NaikGaji(self,kenaikan):
		gaji = self.GajiKotor()
		gaji += ( kenaikan * gaji )
		self.pay = gaji
		return self.pay
		
	def get_NaikGaji(self,kenaikan):
		gaji = self.GajiKotor()
		gaji += ( kenaikan * gaji )
		return gaji
		'''di sini terlihat bahwa Python BERBEDA dengan Java, dia TIDAK MEMBEDAKAN metode get atau set , 
		asalkan tidak merubah isi variable self, maka dia akan 'hanya' sebatas get '''

	@classmethod
	def set_uanglembur(cls,fee):
		cls.set_uanglembur = fee




# Diimport dari modul Potongan


gaji_manager = StandarGaji('Manager') + 1000000

print('Gaji Manager di mark-up' ,gaji_manager)


pajak = Pajak().PotonganPPN()
print('Pajak PPN module:' ,pajak)

emp_1 = Karyawan('Rian','Hariadi','L','Manager',34,5)
emp_2 = Karyawan('Budi','Santorso','L','Staff',31,3)
print(emp_1.set_email())
print(emp_2)

# print ('Class dict:' , GajiKaryawan.__dict__)
# print('List Dict:' , emp_1.__dict__)

print('======== pelajaran Classmethod di bawah ini =========')
emp_str1 = 'Vina-Marwatie-P-Staff-28-3'
new_emp1 = Karyawan.from_string(emp_str1)
print(new_emp1)
print(Karyawan.from_string('Edi-Brokoli-L-Satpam-32-4'))
print(Karyawan.from_string('Rina-Murdiani-P-Staff-28-3'))


Karyawan.buat_email('Rina-Murdiani-P-Staff-28-3')
print('Email buatan @classmethod: ', Karyawan.buat_email)


print('======== pelajaran Staticmethod di bawah ini =========')
import datetime
my_date = datetime.date(2017,1,14)
print('Shit kerja:', Karyawan.shift_kerja(my_date))


print('============================')

gaji_emp_1 = Gaji('Rian','Hariadi','L','Manager',34,5,StandarGaji('Manager'))
gaji_emp_2 = Gaji('Budi','Santorso','L','Staff',31,3,StandarGaji('Staff'))

print('Gaji Manager Bersih: ' ,gaji_emp_1.GajiBersih())
print('Gaji Staff Bersih: ' ,gaji_emp_2.GajiBersih())

print("APABILA Gaji Manager dinaikkan 10% .. (metode get): " , gaji_emp_1.get_NaikGaji(0.1))
print('Gaji Manager Gak jadi dinaikkan + Angka Unik 212: ' , gaji_emp_1.GajiBersih() + 212)

print("Sekarang Gaji Manager dinaikkan 20% .. (metode Set): " , gaji_emp_1.set_NaikGaji(0.2) )
print('Gaji Manager skr, setelah pajak:' ,gaji_emp_1.GajiBersih())

Gaji.set_uanglembur(150000)
#bisa juga begini:
# Gaji.set_uanglembur = 150000 

print('Uang lembur:' , gaji_emp_1.set_uanglembur ) # perhatikan tidak ada () untuk classmethod
