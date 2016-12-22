#Person : measure and conclude whether OK, FAT, or thin

'''Penulisan Argument dan Pemanggilan dalam Fungsi SANGAT FLEKSIBLE dalam Python, sebaliknya
	Anda belajar mengenai penggunaan argument *args dan **kwargs 
sumur: http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/ '''

# ======================== BEGIN class CheckingInput ========================
class CheckingInput:
	def __init__(self, *args):
		self.checktype = args[0]
		self.inputtext = args[1]
		self.rules = args[2]
		if self.checktype == 'checksex':
			self.CheckSex()

	def __str__(self):
		return self.match


	def CheckSex(self):
		inputtext1 = str(self.inputtext)
		rules = self.rules
		# dicek satu-satu , inputtext harus COCOK dengan rules
		self.match = 'TIDAK COCOK'
		# print('Inputnya Jenis Kelamin: ' ,inputtext1)
		for rule in rules:
			if inputtext1 == rule:
				self.match = 'COCOK'
				return self.match
		return self.match
# ======================== ENDclass CheckingInput ========================


# ======================== BEGIN class Person ========================
class Person:
	#set the Class constructor
	def __init__(self,name,sex,age,weight,height):
		self.name = name 
		self.sex = sex
		self.age = str(age)
		self.weight = str(weight)
		self.height = str(height)

	
	def __str__(self):
		# huskyin.com : Mengakses fungsi dalam Kelas yang sama
		# sumur: http://stackoverflow.com/questions/5615648/python-call-function-within-class
		return 'Nama: '+ self.name + '\n' + \
			'Jenis Kelamin :' + self.sex + '\n' + 'Umur :' + self.age + ' tahun' + '\n' + 'Berat Badan :'  +  self.weight + ' kg' + \
			'\n' + 'Tinggi Badan :' + self.height + ' cm' + '\n' 

	def TambahBerat(self, amount):
		self.weight = self.weight + amount
		return self.weight

# ======================== END class Person ========================





# ======================== BEGIN class Check ========================
class Check:
	#set the Class Constructor
	def __init__(self,age,weight,height):
		self.age = age
		self.weight = weight 
		self.height = height 
		self.selisih = int(self.height) - int(self.weight)

	def CheckKondisi(self):
		self.selisih = int(self.selisih)
		if self.selisih > 120 :
			saran = self.Saran('KURUS')
			#PERHATIKAN !! Ini adalah cara memanggil fungsi dalam Kelas yang sama
			kondisi = 'KURUS! .. ' + saran
		elif self.selisih < 80 :
			kondisi = 'GEMUK!...' + self.Saran('GEMUK')
		else:
			kondisi = 'OK!...' + self.Saran()
		return kondisi 


	def Saran(self,kondisi = 'Ideal'):
		self.age = int(self.age)
		print('Kondisi si pasien:',kondisi)
		if kondisi == 'GEMUK':
			if self.age < 50 :
				saran = 'HARUS DIET! \n Usia KURANG DARI 50 tahun selisih tinggi-berat yang ideal adalah 100'
			else:
				saran = 'HARUS DIET! \n Usia LEBIH DARI 50 tahun selisih tinggi-berat yang ideal adalah 90'
		elif kondisi == 'KURUS':
			if self.age < 50 :
				saran = 'Berat badan HARUS DINAIKKAN! \n Usia KURANG DARI 50 tahun selisih tinggi-berat yang ideal adalah 100'
			else:
				saran = 'Berat badan HARUS DINAIKKAN!  \n Usia LEBIH DARI 50 tahun selisih tinggi-berat yang ideal adalah 90'
		else:
			saran = 'Berat badan PAS!! Pertahankan!'
		return saran

# ======================== END class Check ========================



# ======================== BEGIN class Main ========================

def PrintWeightCheck(name,**kwargs):
	#formal Argument:
	print('Nama Pasien: ',name)
	for key in kwargs:
		print ('Data - %s : %s' % (key, kwargs[key])    )


def InputData(*args):
	name = args[0]
	sex = args[1]
	# Coba PERHATIKAN! Argument berasal dari fungsi 'main'

	age = input('Data Pasien - Umur: ')
	weight = input('Data Pasien - Berat Badan (kg): ')
	height = input('Data Pasien - Tinggi Badan (cm): ')

	inputPerson = Person(name,sex,age,weight,height)
	import os
	os.system('cls')
	print('\n')
	print('========= Summary list ========')
	PrintWeightCheck(name , umur=age , berat = weight , tinggi = height)
	print('==============')
	print('\n')
	print('Data Pasien sebagian berikut: ')	
	print(inputPerson)
	
	

	Checking = Check(age,weight,height) 
	selisih = Checking.selisih
	print('Berdasarkan data pasien tersebut memiliki selisih tinggi-berat: ',selisih)
	kondisi = Checking.CheckKondisi()
	print('Kesimpulan dan Saran: \n', kondisi)
	print('==============')
	print('\n')




def main():
	print('Aplikasi menentukan apakah seseorang Kurus, Gemuk, atau OK (berat ideal)')
	name = input('Data Pasien - Masukkan Nama pasien: ')
	sex = input('Data Pasien - Jenis Kelamin(L/P): ')
	sex = sex.upper()
	checktype = 'checksex'
	rules = ['L','P']
	acheck = CheckingInput(checktype,sex,rules)
	
	print(acheck)
	if str(acheck) == 'COCOK':
		print('Input Cocok, silahkan lanjut!')
		argument = [name,sex]
		InputData(*argument)
	else:
		import os
		os.system('cls')
		print('Error!, Pengisian Jenis kelamin salah, kembali ke awal')
		print('=================================')
		print('\n')
		main()



if __name__ == '__main__':
	main()
