'''
Aplikasi Python UMKM : Tehnik Jugling structure data: membuat form dann memasukkan dictionary ke dalam list
Program ini dibuat atas pertanyaan dari salah satu member Grup Whats App Tanya Python () yaitu bagaimana cara 
memanggil, mencari, menyimpan data ke dalam file,... singkatnya: Mini CRUD begitulah..

Dan di program ini saya mencoba menjawab semuanya...

Pengantar:
Program ini selain berisi tutorial membuat APLIKASI FORM sederhana, kita juga belajar struktur data penyimpanannya
dalam struktur data di Python, terutama data kompleks, kita bisa menggunakan perpaduan list, dictionary , dan tuple
Misalnya: (1) kita bisa memasukkan list KE DALAM dictionary, seperti contoh Program Dewa saya (lihat Ahmad Dhani):

{'Tyo Nugros': 'Bass', 'Ari Lasso': 'Vocal', 'Andra Junaedi': 'Guitar', 'Wong Aksan': 'Drum', 'Ahmad Dhani': ['Vocal', 'Keyboard']}

Atau (2)kita bisa memasukkan dictionary KE DALAM list , seperti contoh:

umkm = [
		{"no" : "1" , "nama" : "Huskyin.com" , "pemilik" : "Rian Hariadi" , "alamat" : "Jl.Ahmad Yani 782 Bandung"},
		{"no" : "2" , "nama" : "CV. Maju Bersama" , "pemilik" : "Nandika" , "alamat" : "Jl.Sawangan 7 Depok" },
		{"no" : "3", "nama" : "PT. Cielo Sejahtera" , "pemilik" : "Alex Subaidi", "alamat" : "Jl. Empang 2 Bogor"}
		]

MANA YANG TERBAIK ? 
Sebenarnya dua-duanya baik, tapi jika dilihat dari struktur database, yang di mana merupakan MIRIP dengan JSON, 
memasukkan list KE DALAM dictionary adalah format terbaik untuk disimpan sebagai database. Sedangkan untuk setting,
di mana lebih merupakan hardcoding, bentuk dictionary KE DALAM list adalah yang terbaik,
 seperti file settings.py dalam framework Django 1.10 :

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

btw ingat satu hal: 
JSON mirip dictionary dan BISA mengolah dictionary, TETAPI INGAT di JSON tanda yg digunakan
 adalah petik dua (") bukan petik satu(')
Lihat file Dewa saya kemarin untuk mengubah tanda (') menjadi (")

Dan jika data itu sudah "jadi" maka kita akan melihat sebuah format data yang mirip sekali dengan query database:
DATA = {  
       "no" : ["1","2","3","4"], 
       "nama" : ["PT. Maju Gemilang","PT. Sinar Maju","PT. MNC","PT.Indofood"] ,
       "pemilik" : ["Surya Saputra", "Robert Hartanto" ,"Harry Tanoe","Liem Sie Liong"]
       }

Coba perhatikan, data di atas BISA dijadikan table database dengan 3kolom dan 4 baris, bukan begitu?

Dengan kata lain, apa kesimpulan dari dictionary? BETUL SEKALI, dictionary adalah salah satu format Database yang
paling bagus.. Dan hanya Python-lah satu-satunya bahasa yang memiliki dictionary , 

AHH!! INILAH INDAHNYA PYTHON!:-)

Demikian semoga jelas - Rian Irawan Hariadi , rianhariadi.com / huskyin.com

'''

class CheckInput:
	def __init__(self,*args,**kwargs):
		self.matcher = args[0]
		self.form_input = kwargs['form_input']
		self.form_name =  kwargs['form_name']
		# for key in kwargs:
		# print ("another keyword arg: %s: %s" % (key, kwargs[key]) )

	def Checking(self):
		the_dict = {}
		for arg in self.matcher:
			# print(arg)
			# print(self.matcher)
			# print(self.form_input)
			if self.form_input == arg:		
				success = True
				message = 'silahkan lanjutkan ...' 
				the_dict["result"] = success
				the_dict["message"] = message
				the_dict["option"] = self.form_input
				return the_dict
			else:
				success = False
				message = 'Pilihan SALAH, Anda hanya boleh memilih opsi:'+ str(self.matcher) 
				the_dict["result"] = success
				the_dict["message"] = message

		the_dict["Input Anda"] = self.form_input
		return the_dict


import os,sys




def TambahData(DATA):
	data = {}
	if DATA != 'BELUM ADA DATA':
		data = DATA
		total = DATA["total"]
		print("\n Total UMKM sebelumnya: ", total )
		total = int(total)
		if total == 0:
			jumlah = input("Masukkan banyaknya data UMKM: >>>")
			jumlah = int(jumlah)
			total = 0
			data["total"] = str(jumlah)
			no = []
			nama = []
			pemilik = []
		else:	
			jumlah = input("Masukkan banyaknya data (tambahan): >>>")
			jumlah = int(jumlah)
			jumlah = jumlah + total
			data["total"] = str(jumlah)
			no = DATA["no"]
			nama = DATA["nama"]
			pemilik = DATA["owner"]


	else:
		jumlah = input("Masukkan banyaknya data UMKM: >>>")
		jumlah = int(jumlah)
		total = 0
		data["total"] = str(jumlah)
		no = []
		nama = []
		pemilik = []


	i = int()
	i = total
	
	# semua elemen value disimpan dalam bentuk list, karena itu inisialisasikan dahulu
		
	
		
	for i in range (i,jumlah) :		
		no_i = str(i)
		urutan = str(i+1)
		nama_i = input("\n Masukkan Nama Perusahaan UMKM ke- " + urutan + " : >>>")
		pemilik_i = input("Masukkan Nama Pemilik perusahaan ke-" + urutan + " : >>>")
		no_i = str(no_i)			
		nama_i = str(nama_i)
		pemilik_i = str(pemilik_i)
		
			# Sealu diingat untuk List, cara MEDAFTARKAN anggota adalah dengan fungsi append. !!
		no.append(no_i)
		nama.append(nama_i)
		pemilik.append(pemilik_i)
		print (no)
		print (nama)
		print (pemilik)
		# print (no)
		# print(nama)
		# print(pemilik)
		data["no"] = no
		data["nama"] = nama
		data["owner"] = pemilik

	return data


def EditData(DATA,no_urut): #0
	no_urut = int(no_urut)
	print('\n Opsi: ')
	print('(1) Edit "Nama UMKM"')
	print('(2) Edit "Nama Owner"')
	print('(3) Delete')
	print('(4) Keluar ke Menu Utama')
	opsi = input('Pilih Opsi: >>')
	opsi = int(opsi)
	if opsi == 1:
		print('Nilai sekarang: ', DATA["nama"][no_urut])
		new_value = input('Masukkan Nilai baru:')
		DATA["nama"][no_urut] = new_value
		print('\n DATA BERHASIL DI-EDIT! \n')
		TampilkanData(DATA,no_urut = no_urut + 1,hasil_search="NO") #1
	elif opsi == 2:
		print('Nilai sekarang: ', DATA["owner"][no_urut])
		new_value = input('Masukkan Nilai baru:')
		DATA["owner"][no_urut] = new_value
		print('\n DATA BERHASIL DI_EDIT! \n')
		TampilkanData(DATA,no_urut = no_urut + 1 ,hasil_search="NO") #1
	elif opsi == 3:
		listkey = list(DATA.keys())
		for each_list in listkey:
			# print('the list' ,DATA[each_list])
			if each_list != "total": #"total" tidak boleh ikutan karena elementnya cuman satu
				DATA[each_list].pop(no_urut)
		print('\n DATA BERHASIL DI-HAPUS! \n')
		total = int(DATA["total"]) #total harus dikurangi karena satu anggota dihapus
		total  -= 1
		DATA["total"] = total
		TampilkanData(DATA,no_urut = '',hasil_search="NO") #1
	else:
		print('Menu Utama...')
		main(DATA)

	


def TampilkanData(DATA,**kwargs):
	if kwargs["no_urut"] == '' :
		total = DATA["total"]
		print("\n Total UMKM: ", total )
		total = int(total)
		i = int()
		i = 0
		print('\n List UMKM: ')
		for i in range (i,total):
			urutan = int(DATA["no"][i]) + 1
			print("\nNo Urut   : ", urutan)
			print("Nama UMKM : " ,DATA["nama"][i]) 
			print("Nama Owner: " ,DATA["owner"][i]) 
			print("================= \n")
	else:
		no_urut = int(kwargs["no_urut"]) - 1 #0
		print("\nNo Urut   : ", no_urut + 1 ) #1
		print("Nama UMKM : " ,DATA["nama"][no_urut]) 
		print("Nama Owner: " ,DATA["owner"][no_urut]) 
		print("================= \n")
		if kwargs["hasil_search"] == 'YES':
			pass
		else:
			EditData(DATA,no_urut=no_urut ) #0





def SearchEngine(keyword,DATA):
	#buat list dari key dictionarynya
	
	index_found = []

	if DATA == "BELUM ADA DATA" :
		print ('Ditemukan: 0 hasil, untuk kata: "', keyword,'" \n')
		return index_found

	listkey = list(DATA.keys())
	indi = ''
	ind = int()
	ind = 0
	
	for each_list in listkey:
		# print('At: ',each_list)
		# Cari SEMUA 'penampakan' di setiap list value
		# sumur; http://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
		for sentence in DATA[each_list]:
			# print(DATA[each_list])
			# print('Kalimat: ', sentence)
			# Cari indexnya dahulu
			# print('Index:', ind)
			
			# index = FindIndex(DATA[each_list],sentence)
			sentence = str(sentence)
			word = sentence.find(keyword)
			if word != -1 :
				index_found.append(ind) 
			ind += 1
		ind = 0

		print(indi)
		jum = len(index_found)
	print ('Ditemukan: ' , jum, 'hasil, untuk kata: "', keyword,'" \n')
	return index_found



def SaveData(DATA):
	if DATA == "BELUM ADA DATA":
		print("Data masih kosong, tidak ada yang bisa disimpan")
	else:
		with open ('result.txt' , 'w') as d:
		# diubah dulu ke string
			DATA = str(DATA)
		# Diubah ke double quotes kalo tidak JSON susah membacanya
			DATA = DATA.replace("'",'"')
			d.write(DATA)
			print(DATA)
		print("\n \n ======= DATA BERHASIL DISIMPAN DI result.txt =========== ")

import json
from collections import namedtuple

def LoadData(namafile):
	print ('Baca data di result.txt')
	with open ('result.txt', 'r') as j:
		# DATA = {}
		for line in j:
			JSON_Datalist = line 
			the_dict = json.loads(JSON_Datalist)
	print('\n \n ======= DATA DI-UNDUH DARI result.txt =========== ')
	print(the_dict)
	the_listkey = list(the_dict.keys())
	print(the_listkey)
	
	return the_dict







def main(DATA):
	#PROGRAM APLIKASI PENCATATAN DATA UMKM
	
	print ("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print ("PROGRAM PENCATATAN DATA UMKM (MINI CRUD)")
	print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print ("Data Sementara: " , DATA)
	form_utama = 'Form Tampilan Utama'
	print ("\n| 1. Tambah Data |")
	print ("| 2. Tampil / Edit / Hapus Data |")
	print ("| 3. Cari Data Berdasarkan Kata kunci |")
	print ("| 4. Simpan Data di result.txt (AWAS! Data yg sebelumnya akan tertimpa!)|")
	print ("| 5. Ambil (unduh) Data dari file result.txt |")
	print ("| 6. Exit |")
	print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print(" Rian Irawan Hariadi : rianhariadi.com /  huskyin.com \n \n ")
	user_input = (input("Masukan Pilihan Anda :>>>"))
	option =['1','2','3','4','5','6']
	check = CheckInput(option,form_input = user_input,form_name = form_utama )
	check = check.Checking()
	# print(check.Checking())

	if check["result"] == True:
		print(check["message"])
		option = check["option"]
		if option == '1':
			DATA = TambahData(DATA)
			print (DATA)
			main(DATA)
		elif option == '2':
			print("Data sekarang: " ,DATA)
			if DATA == "BELUM ADA DATA" :
				print ('Tidak ada data yg bisa ditampilkan')
				main(DATA)
			else:
				opsi = int(input("\n \n Pilih Opsi: \n (1) Tampilkan semua \n (2)Tampilkan /Edit/Hapus Data No tertentu >>>"))
				opsi = int(opsi)
				if opsi == 1:
					TampilkanData(DATA,no_urut='',hasil_search="NO")
					main(DATA)
				else:
					no = input("Ketik No. Urut UMKM yg ingin ditampilkan / diedit (1,2,3,dst) >>> ")
					TampilkanData(DATA,no_urut=no,hasil_search="NO")
					main(DATA)
			


		elif option == '3':
			print("Pencarian data berdasarkan kata kunci (keyword)")
			keyword = input("Masukkan Keyword: >>> ")
			search = SearchEngine(keyword,DATA)
			for x in search:
				x = int(x) + 1
				TampilkanData(DATA,no_urut=x,hasil_search="YES")
			main(DATA)
		elif option == '4':
			SaveData(DATA)
			main(DATA)
		elif option == '5':
			print ("Ambil (unduh) data dari file result.txt")
			DATA = LoadData('result.txt')
			main(DATA)	
		else:
			os.system('cls')
			print('ANDA KELUAR, TERIMA KASIH! \n - Rian Hariadi (rianhariadi.com / huskyin.com)')
			sys.exit()

	else:
		os.system('cls')
		print(check["message"])
		print('=================================')
		print('\n')
		main(DATA)		

	return DATA




if __name__ == '__main__':
	DATA = "BELUM ADA DATA"
	main(DATA)


