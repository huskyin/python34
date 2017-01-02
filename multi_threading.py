''' fungsi multi_threading '''

import time
import threading
from math import *


def Memasak(progress,waktu):
	print('Aktivitas Memasak')
	for n in progress:
		time.sleep(0.2)
		print('Pekerjaan Memasak selesai : %s' % str(n*10) + '%')

def MengasuhAnak(progress,waktu):
	print('Aktivitas Mengasuh Anak')
	for n in progress:
		time.sleep(0.2)
		print('Pekerjaan Mengasuh Anak selesai : %s' % str(n*10) + '%')

def MembereskanRumah(progress,waktu):
	print('Aktivitas Membereskan Rumah')
	for n in progress:
		time.sleep(0.2)
		print('Pekerjaan Membereskan Rumah selesai : %s' % str(n*10) + '%')
	HitungWaktu(waktu)


arr = [1,2,3,4,5,6,7,8,9,10]


def Tanpa_Multi_Threading():
	waktu = time.time()
	Memasak(arr,waktu)
	MengasuhAnak(arr,waktu)
	MembereskanRumah(arr,waktu)
	# durasi = (time.time()-waktu)
	# durasi = int(durasi*100) + 0.5 /100.0
	# print ('TANPA PROSES MULTI THREADING SEMUA PEKERJAAN SELESAI DALAM: ', durasi  , 'detik' )
	JalankanProses()



def Dengan_Multi_Threading():
	waktu = time.time()
	t1 = threading.Thread(target=Memasak, args=(arr,waktu))
	t2 = threading.Thread(target=MengasuhAnak, args=(arr,waktu))
	t3 = threading.Thread(target=MembereskanRumah, args=(arr,waktu))

	t1.start()
	t2.start()
	t3.start()
	# durasi = (time.time()-waktu)
	# durasi = int(durasi*100) + 0.5 /100.0
	# print ('DENGAN PROSES MULTI THREADING, SEMUA PEKERJAAN SELESAI DALAM: ', durasi , 'detik' )
	# JalankanProses()


def HitungWaktu(waktu):
	durasi = (time.time()-waktu)
	durasi = int(durasi*100) + 0.5 /100.0
	print ('\n SEMUA PEKERJAAN SELESAI DALAM: ', durasi , 'detik' )
	print('================ www.huskyin.com ================= \n')
	JalankanProses()


def JalankanProses():
	cara = input('\n Ini adalah proses simulasi program Python "Multi Threading" atas 3 aktivitas: \n '+
		'Memasak, Mengasuh Anak, Membereskan Rumah \n' + 'Tentukan dengan jalan apa proses dilakukan:  \n \
	    (1) Cara Biasa (TANPA Multi Threading)  \n \
	    (2) DENGAN Multi Threading... \n \
	    (3) Akhiri dan lihat kesimpulan \n \ >>> ')
	if cara == '1':
		Tanpa_Multi_Threading()
	elif cara == '2':
		Dengan_Multi_Threading()
	elif cara == '3':
		LihatKesimpulan()	
	else:
		print('Maaf pilihan Anda Salah! Pilih antara (1,2 atau 3)')
		JalankanProses()

def LihatKesimpulan():
	print("\n============ www.huskyin.com ================= \n " + 
		 "\n KESIMPULAN: \n Anda sudah melihat perbedaan, beberapa pekerjaan yang dilakukan secara \n " + 
		"Multi-Threading, akan LEBIH JAUH LEBIH CEPAT! Anda lihat sendiri bagaimana \n " + 
		 "pekerjaan-pekerjaan Tanpa Multi Threading, semua dikerjakan secara SERIAL, \n " +  
	    "sedangkan pekekerjaan-pekerjaan dengan Multi Threading dikerjakan PARAREL \n \n " +
	    "Pesan filosofis: \n " +
	    "Omong-omong, tahukah Anda analogi yang pas buat proses Multi Threading ini? \n" +
	    "BETUL SEKALI! WANITA! Mereka adalah makhluk Multi-Threading! Coba lihat! \n" +
	    "mereka 'multi Threading' dalam beberapa pekerjaan sekaligus di kesehariannya: \n" + 
	    "Mencuci, membersihkan rumah, mengasuh anak, dan tentu saja: melayani suami \n  " +
	    "Karena itu marilah kita menghormati wanita terutama Ibu dan istri kita!  \n" +
	    "\n SALAM SUPER - Rian Irawan Hariadi \n " + 
	    "================ www.huskyin.com ================= \n  ")
	JalankanProses()

if __name__ == "__main__" :
	JalankanProses()

