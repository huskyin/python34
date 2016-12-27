''' Program Kalkulator Sederhana , diperuntukan bagi Pemula Python 3.4
Fungsi program ini adalah untuk menunjukkan kegunaan "decorator" dalam bahasa Python.

dibuat oleh : Rian Irawan Hariadi (www.rianhariadi.com)
'''


def Fungsi_luar():
	pesan = 'Pesan 1 - Sebelum Anda memahami deocrators dalam Python 3.4, tolong pahami dulu tentang "Fungsi di dalam fungsi". \n Gampangnya silahkan lihat source code di mana pesan ini berada!'
	def Fungsi_dalam():
		print(pesan)
	return Fungsi_dalam()

Fungsi_luar()

print('\n ============== www.huskyin.com -2016 ================')

def Fungsi_luar2():
	pesan = 'Pesan 2 - Ini sama dengan pesan sebelumnya, tapi ada perbedaannya, \n TOLONG perhatikan comment bertanda ">>>" di source code!'
	def Fungsi_dalam2():
		print(pesan)
	return Fungsi_dalam2 #>>>


ayo_jalankan = Fungsi_luar2()#>>> Bandingkan dengan Fungsi_luar 
ayo_jalankan()


print('\n ============== www.huskyin.com -2016 ================')
def Fungsi_luar3(pesanluar):
	pesan = ' Pesan 3 - Sekarang lihat, saya mem-passin argumen variable ke dalam fungsi!'
	def Fungsi_dalam3():
		print(pesan)
		print(pesanluar)
	return Fungsi_dalam3 #>>>

pesanku = 'Halo, apa kabar?'
pakai_pesan = Fungsi_luar3(pesanku)
pakai_pesan()


print('\n ============== www.huskyin.com -2016 ================')
def Fungsi_luar4(pesanluar,fungsi_perintahluar,fungsi_pesanluar):
	pesan = ' Pesan 4 - Dan bagaimana jika argument itu berupa fungsi juga??'
	def Fungsi_dalam4():
		print(pesan)
		print(pesanluar)
		fungsi_perintahluar()
		fungsi_pesanluar() #lihat hasil keluaran dari ini
		print(fungsi_pesanluar) #lihat juga ini
		hasil_fungsiluar = fungsi_pesanluar()
		print(hasil_fungsiluar) 
	return Fungsi_dalam4 #>>>

def fungsi_perintahluar():
	print('PERHATIKAN INI!!')

def fungsi_pesanluar():
	pesanku = ' NAH, INILAH KONSEP DASAR DARI DECORATOR dalam PYTHON!'
	return pesanku


pesanku = 'Anda paham?'
pakai_fungsiluar= Fungsi_luar4(pesanku,fungsi_perintahluar,fungsi_pesanluar)
pakai_fungsiluar()


print('\n ============== www.huskyin.com -2016 ================')
def Fungsi_luar5(fungsi_input):
	pesan = ' Pesan 5 - Tanda anotation @ berarti: "Tolong masukkan fungsi di bawah ke fungsi yg ada tanda-@ nya!'	
	def Fungsi_dalam5(*args,**kwargs):
		print(pesan)
		print('.. memiliki fungsi input yaitu: {} , yg berada di bawah tanda @'.format(fungsi_input.__name__) )
		output_f = fungsi_input(*args,**kwargs)
		print (output_f)
		return output_f
	return Fungsi_dalam5


@Fungsi_luar5
def fungsi_perintahluar5(perintahnya):
	print(perintahnya)
	return '' #--> kenapa saya harus menulis ini?? coba pikirkan

@Fungsi_luar5
def fungsi_pesanluar5(*args):
	pesanku = '  OK, inilah cara menulis decorator , dengan tanda @ \n '+ args[0]
	return pesanku


perintahnya = 'PERHATIKAN INI JUGA!'
fungsi_perintahluar5(perintahnya)
print ('dan,.....')

pesanku5 = 'Ada bagusnya Anda membaca lagi konsep argumen *args dan **kwargs (ada juga di file saya: WeightCheck.py)' 
fungsi_pesanluar5(pesanku5)





