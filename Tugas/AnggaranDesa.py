''''
Program AnggaranDesa.py
menghitung anggaran berdasarkan desa

dibuat oleh Rian Irawan Hariadi , huskyin.com

Silahkan pelajari link ini buat referensi:
- http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops-in-python
- http://www.mkyong.com/python/python-how-to-loop-a-dictionary/
- https://learnpythonthehardway.org/book/ex32.html
- http://stackoverflow.com/questions/9138112/looping-over-a-list-in-python
- http://www.thegeekstuff.com/2013/06/python-list/?utm_source=feedly
- http://effbot.org/zone/python-list.htm
- http://pythoncentral.io/pythons-range-function-explained/
- http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops-in-python
- https://www.tutorialspoint.com/python/dictionary_get.htm
- https://developers.google.com/edu/python/sorting
- http://stackoverflow.com/questions/3496518/python-using-a-dictionary-to-count-the-items-in-a-list
- http://mastercode.online/unit/find-keys-values-python-dictionary/


'''


class Soal:

	def __init__(self,str_desa):
		no_id, nama_desa, kabupaten, kota , anggaran = str_desa.split('==')
		self.no_id = no_id
		self.nama_desa = nama_desa
		self.kabupaten = kabupaten
		self.kota = kota
		self.anggaran = anggaran
		

	def get_jumlah_anggaran(self):
		return self.anggaran

	def get_nama_desa(self):
		return self.nama_desa


#Main function




# listdesa = ['Ds. Jambu Timur','Ds. Jambu','Sekuro','Sinanggu']

a = 0


'''
jumlah = input('Berapa jumlah data ?')
for str_desa in range (jumlah):
	str_desa[a] = input('Masukkan string desa ke-' , (a+1) )
	a++ 
'''
# sementara tulis manual dulu
str_desa = []
str_desa.append('PPS01==Ds. Jambu Timur==Mlonggo==Jepara==100')
str_desa.append('PPS02==Ds. Jambu Timur==Mlonggo==Jepara==110')
str_desa.append('PPS03==Ds. Jambu Timur==Mlonggo==Jepara==75')
str_desa.append('PPS01==Ds. Jambu==Mlonggo==Jepara==100')
str_desa.append('PPS02==Ds. Jambu==Mlonggo==Jepara==75')
str_desa.append( 'PPS03==Ds. Jambu==Mlonggo==Jepara==100')
str_desa.append('PPS01==Sekuro==Mlonggo==Jepara==75')
str_desa.append('PPS02==Sekuro==Mlonggo==Jepara==85')
str_desa.append( 'PPS03==Sekuro==Mlonggo==Jepara==95')
str_desa.append('PPS01==Sinanggu==Mlonggo==Jepara==110')
str_desa.append('PPS02==Sinanggu==Mlonggo==Jepara==110')

s = 0
dict_anggaran = {}
listdesa = list()
for c in range (len(str_desa)):
	nama_desa = Soal(str_desa[c]).get_nama_desa()
	nama_desa = str(nama_desa)
	listdesa.append(nama_desa)

print ('List Nama Desa:' ,listdesa)

from collections import Counter
dict_desa = Counter(listdesa)
listdesaunik = list(dict_desa.keys())
print ('List Nama Desa secara UNIK:' ,listdesaunik)


for nama in listdesaunik:
	dict_anggaran[nama] = 0
	print(nama)
	print('Anggaran Awal: ' , dict_anggaran[nama] )

print('\n \n ======= MARI DIPROSES ======= ')

for s in range (len(str_desa)):
	print (str_desa[s])
	desa = Soal(str_desa[s])
	nama_desa = desa.get_nama_desa()
	print('Nama desa:' ,nama_desa)
	jumlah_anggaran = desa.get_jumlah_anggaran()
	jumlah_anggaran = int(jumlah_anggaran)
	print('jumlah anggaran:' ,jumlah_anggaran)

	for nama in listdesaunik:
		if nama == nama_desa:
			dict_anggaran[nama_desa] += jumlah_anggaran
	


print('\n \n ======= OUTPUT:  ======= ')
print(dict_anggaran)

for key, value in dict_anggaran.items():
	print ('Desa: {} , Total Anggaran: {}' . format(key, value)  )