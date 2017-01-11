#Aljabar Linear , mencari nilai X, dibuat oleh Rian Irawan hariadi (www.rianhariadi.com)

'''
Cara termudah:
http://docs.sympy.org/0.7.1/modules/solvers/solvers.html
http://stackoverflow.com/questions/10499941/how-can-i-solve-equations-in-python

Operasi string:
http://stackoverflow.com/questions/8270092/python-remove-all-whitespace-in-a-string
'''
print("Fungsi ini untuk mencari Nilai 'X' pada persamaan aljabar linier \n seperti waktu di SD, dibuat oleh Rian Irawan Hariadi")
print (" Masukkan notasi aljabar dengan variabel X pangkat 1 \n (contoh: '4 - 3x = 28 - 5X ') ")
notasi = input('Masukkan notasi:')
notasi = notasi.strip()
notasi = notasi.replace(" ","")
PASS = True


def printnotasi(notasi):
	notasi = notasi.upper()
	for char in notasi:
		print (char)




def findNotNumber(notasi):
	notasi = notasi.upper()
	result = True
	for char in notasi:
		detect = char.isalpha()
		if detect == True :
			if char != 'X':
				result = False
				break	
	return result

# http://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python
def pisahkanTanda(notasi):
	index = 0 
	while index < len(notasi):
		index = notasi.find('+',index)
		if index == -1:
				break
		index_a = index + 1
		notasi = notasi[:index]+'aT'+ notasi[index_a:]
	index = 0
	while index < len(notasi):
		index = notasi.find('-',index)
		if index == -1:
				break
		index_a = index + 1
		notasi = notasi[:index]+'aK'+ notasi[index_a:]
	return notasi	


def PecahkanNotasi(notasi):
	pecah = notasi.split('a')
	return pecah



def TukarPosisi(notasi_kiri,notasi_kanan):
	i =0
	while (i < len(notasi_kiri) ):
		if notasi_kiri[i].find('X') == -1:
			#print('ruas kiri dihapus: ',notasi_kiri[i])
			if notasi_kiri[i].find('T') != -1 :
				notasi_kiri[i] = notasi_kiri[i].replace('T','-')
			else:
				notasi_kiri[i] = notasi_kiri[i].replace('K','')
			notasi_kanan.append(notasi_kiri[i])
			del (notasi_kiri[i])
		elif notasi_kiri[i] == '':
			del (notasi_kiri[i])
		else:
			i = i + 1
	i = 0
	while (i < len(notasi_kanan) ):
		if notasi_kanan[i].find('X') != -1:
			#print('ruas kanan dihapus:',notasi_kanan[i])
			if notasi_kanan[i].find('T') != -1 :
				notasi_kanan[i] = notasi_kanan[i].replace('T','-')
			else:
				notasi_kanan[i] = notasi_kanan[i].replace('K','')
			notasi_kiri.append(notasi_kanan[i])
			del (notasi_kanan[i])	
		elif notasi_kanan[i] == '':
			del (notasi_kanan[i])	
		else:
			i = i + 1
	#print ('Setelah dipindahkan,..Notasi kiri: ',notasi_kiri)
	#print ('Setelah dipindahkan,..Notasi_kanan: ',notasi_kanan)
	return notasi_kiri, notasi_kanan

def AtasiX(notasi_kiri):
	i = 0
	notasi_kiri = [a.replace('KX','K1X') for a in notasi_kiri]
	notasi_kiri = [a.replace('TX','T1X') for a in notasi_kiri]
	return notasi_kiri


def NilaiKiri(notasi_kiri):
	notasi_kiri = [a.replace('X','') for a in notasi_kiri]
	notasi_kiri = [a.replace('K','-') for a in notasi_kiri]
	notasi_kiri = [a.replace('T','') for a in notasi_kiri]
	nilai = 0
	nilai_kiri = ''
	for i in range (len(notasi_kiri)):
		nilai = int(notasi_kiri[i]) + nilai
		nilai_kiri = nilai_kiri  + notasi_kiri[i]+'X' + ' + '
	nilai_kiri = nilai_kiri[:-2]
	print ('Setelah dipindahkan, sisi kiri: ',nilai_kiri)
	return nilai

def NilaiKanan(notasi_kanan):
	notasi_kanan = [a.replace('K','-') for a in notasi_kanan]
	notasi_kanan = [a.replace('T','') for a in notasi_kanan]
	nilai = 0
	nilai_kanan = ''
	for i in range (len(notasi_kanan)):
		nilai = int(notasi_kanan[i]) + nilai
		nilai_kanan = nilai_kanan  + notasi_kanan[i] + ' + '
	nilai_kanan = nilai_kanan[:-2]
	print ('Setelah dipindahkan, sisi kanan: ',nilai_kanan)
	return nilai



#cek apakah ada tanda yang dilarang
if notasi.count('=') > 1 :
	print ("Error, tanda 'sama dengan / =' dengan hanya boleh ada 1")
	PASS = False
if notasi.count('^') != 0:
	PASS = False
	print ('Error, hanya boleh pangkat 1 !')
if notasi.count('/') != 0:
	PASS = False
	print ('Error, tidak boleh ada operator pembagian !')
if notasi.count('*') != 0:
	PASS = False
	print ('Error, tidak boleh ada operator perkalian !')	
if (notasi.count(' 0 ') != 0) or (notasi.count(' 0X ') != 0) :
	PASS = False
	print ('Error, tidak boleh ada angka nol sendirian !')		
if findNotNumber(notasi) == False:
	PASS = False
	print ('Error, tidak boleh ada huruf selain X !')	
if PASS != False:
	#print (findNotNumber(notasi))
	#print (printnotasi(notasi))
	#print('Fungsi dilanjutkan... besok ya... :-)')
	#print('Pisahkan tanda tambah , menjadi...')
	#print('Pisahkan ruas kiri dan ruas kanan')
	ruas_notasi = notasi.split('=')
	notasi_kiri = ruas_notasi[0]
	notasi_kanan = ruas_notasi[1]
	if notasi_kiri[0] != '-':
		notasi_kiri = '+' + notasi_kiri
	if notasi_kanan[0] != '-':
		notasi_kanan = '+' + notasi_kanan

	
	
	#print (pisahkanTandaTambah(notasi))

	notasi_kiri = pisahkanTanda(notasi_kiri)
	notasi_kanan = pisahkanTanda(notasi_kanan)

	#print('Notasi kiri setelah dipecah: ')
	notasi_kiri = PecahkanNotasi(notasi_kiri)
	notasi_kiri = AtasiX(notasi_kiri)
	#print(notasi_kiri)
	#print('...')
	#print('Notasi kanan setelah dipecah: ')
	notasi_kanan = PecahkanNotasi(notasi_kanan)
	notasi_kanan = AtasiX(notasi_kanan)
	#print(notasi_kanan)

	TukarPosisi(notasi_kiri,notasi_kanan)
	print('..................')
	#print('Notasi kiri: ',notasi_kiri)
	#print('Notasi kanan: ',notasi_kanan)
	nilaikiri = NilaiKiri(notasi_kiri)
	nilaikanan = NilaiKanan(notasi_kanan)
	
	print('Nilai di sisi kiri = ',str(nilaikiri)+'X')
	print('NIlai di sisi kanan =',nilaikanan)

	print('Solusi: X = ',float(nilaikanan/nilaikiri))


