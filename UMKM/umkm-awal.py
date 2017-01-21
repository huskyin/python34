i=0
nama=[]
pemilik=[]
alamat=[]
#PROGRAM APLIKASI PENCATATAN DATA UMKM
print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print ("PROGRAM PENCATATAN DATA UMKM")
print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print ("| 1. Tambah Data |")
print ("| 2. Tampil Data |")
print ("| 3. Cari Data |")
print ("| 4. Exit |")
print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
pilih=int (input("Masukan Pilihan Anda "))
print ("^^^^^^^^^^^^^^^^^^^^^^")
while True:
 nama.append(raw_input('Nama\t: '))
 pemilik.append(raw_input('Pemilik\t: '))
 if len(pemilik[i])==0:
 print
 nama.pop(i)
 pemilik.pop(i)
 continue
 alamat.append(raw_input('Alamat\t: '))
 if len(alamat[i])==0:
 print
 nama.pop(i)
 pemilik.pop(i)
 alamat.pop(i)
 continue
 lagi=''
 while lagi!='Y' and lagi!='T':
 lagi=raw_input('INPUT LAGI [Y/T] : ')
 i+=1
 if lagi=='T':
 break
print ' Daftar UMKM '
print
'=====================================================
==================='
print '| No. | Nama | Pemilik | Alamat |'
print
'=====================================================
==================='
for n in range(i):
 print '| ',n+1,' | ',nama[n],' | ',pemilik[n],' | ',alamat[n],' |'
ing=''
while ing!='Y' and ing!='T':
 ing=raw_input('Apakah anda ingin mencari data [Y/T]? ')
if ing=='Y':
 cari=raw_input('Cari berdasarkan Nama : ')
 for n in range(i):
 if cari==nama[n]:
 print
 print 'Nama\t:',nama[n]
 print 'Kelas\t:',pemilik[n]
 print 'Alamat\t:',alamat[n]
 break
 else:
 print 'NAMA TIDAK ADA'
 break
