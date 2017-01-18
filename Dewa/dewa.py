'''
Program managedata.py
Mengolah data yang didapat dari file lain (txt). data dioah, kemudian disimpan kembali dalam file txt.

dibuat oleh : Rian Irawan Hariadi , www.huskyin.com 

'''

import os

with open ('dewa_line.txt', 'r') as f:
	dewa = {}
	for line in f:
		personil,posisi = line.split('==')
		dewa[personil] = posisi.replace("\n","")
		print(line, end='')
	print('\n Personil Dewa: ')
	print(dewa)



# Memodifikasi File Dictionary
print('\n Menambah elemen dictionary (tambah Mulan Jamela)')
dewa['Mulan Jamela'] = 'Vocal'
print(dewa)

print('\n Menghapus dictionary (Mulan Jamela dihapus)')
dewa.pop('Mulan Jamela')
print(dewa)

print('\n Mengubah elemen value dictionary menjadi list')
dewa['Ahmad Dhani'] = ['Vocal', 'Keyboard']
print(dewa)


print('\n Mengubah elemen key dictionary (Ari Lasso diganti Once)')
dewa['Once'] = dewa.pop('Ari Lasso')
print(dewa)


print('\n PENCARIAN ELEMET TERTENTU')
print('\n Mencari value berdasarkan key')
print('Search: Apa posisi Andra Junaedi ?')
print('jawab:' , dewa['Andra Junaedi'])


print('\n Mencari key berdasarkan value')
print('Search: personil dengan posisi Drum')
for personil, posisi in dewa.items():
	if posisi == 'Drum':
		print ('jawab: ', personil)

print('\n Mencari key berdasarkan value')
print('Search: personil dengan posisi Vocal')
for personil, posisi in dewa.items():
	if posisi == 'Vocal':
		print ('jawab: ',personil)

print('\n Mencari key berdasarkan value (lebih seksama)')
print('Search: personil dengan posisi Vocal')
posisi =[]
for personil, posisi in dewa.items():
	posisi_list = set(posisi)
	if 'Vocal' in posisi_list or 'Vocal' == posisi :
		print ('jawab: ',personil)

print('\n Mencari key berdasarkan value secara detail 1')
print('Search: personil posisi Vocal')
for personil, posisi in dewa.items():
	# Data dicari dalam string
	if posisi == 'Vocal':
		print (personil)
	# Data dicara dalam list
	for pos in posisi:
		if pos.find('Vocal') != -1:
			print ('jawab: ',personil)

   
print('\n Mencari key berdasarkan value secara detail 2')
print('Search: posisi Vocal')
for personil,posisi in dewa.items():
	dewa1 = dewa[personil]

	# Semuanya dijadikan string terlebih dahulu (agar seragam karena string Lebih mudah dicari)
	str_dewa1 = ''
	# for pos_dewa1 in dewa1:
	# 	str_dewa1.replace(" ",",")
	# 	str_dewa1 += pos_dewa1 

	# Metode paling cepat join atau str
	str_dewa1 = str(dewa1 )
	# Setelah jadi string barulah dicari
	if 'Vocal' in str_dewa1:
		print ('jawab: ',personil)


print('\n Mencari daftar key (dalam bentuk list)')
listkey = list(dewa.keys())
print (listkey)

print('\n Mencari daftar value (dalam bentuk list)')
listvalues = list(dewa.values())
print (listvalues)




# Simpan dalam bentuk baris
with open ('dewa_line_new.txt' , 'w') as l: #AWAS, FILE TIDAK BOLEH SAMA, NANTI SEBELUMNYA TERTIMPA!
	listkey = list(dewa.keys())
	i = 0
	for line in listkey:
		personil = listkey[i]
		posisi = dewa[personil]
		posisi = str(posisi)
		str_dewa = personil+ '==' + posisi + '\n'
		# print(str_dewa)
		i += 1
		l.write(str_dewa)



# Simpan lagi bentuk dictionary ke file, jadi ubah lagi ke string
with open ('dewa_dict.txt' , 'w') as d:
	# diubah dulu ke string
	dewa= str(dewa)
	# Diubah ke double quotes kalo tidak JSON susah membacanya
	dewa = dewa.replace("'",'"')
	print('Hasil Akhir: ',dewa)
	d.write(dewa)


# Mengambil kembali data paling mudah yg dewa_dict, karena MIRIP dengan Object JSON
# Referensi: http://stackoverflow.com/questions/19110407/converting-json-objects-in-to-dictionary-in-python

import json
from collections import namedtuple

print ('Baca kembali data di dewa_dict.txt')
with open ('dewa_dict.txt', 'r') as j:
	dewa = {}
	for line in j:
		JSON_Datalist = line 
		the_dict = json.loads(JSON_Datalist)
	print('\n Personil Dewa: ')
	print(the_dict)
	print('\n Nah, sekian dan terima kasih, - Rian Irawan Hariadi')
	print('Special Credit to my Favorite Singer : Elfonda Michael alias Once sebagai ...', the_dict['Once'])






