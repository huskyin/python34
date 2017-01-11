'''
  - Angka UMR ditentukan
1 - Gaji berdasarkan posisi jabatan (OB, staff, supervisor, manager) dan/atau lama pengalaman (experience)
  - Gaji OB HARUS dibawah UMR
2 - Gaji kotor dipotong pajak 10% , untuk gaji di atas UMR
3 - Gaji bersih akan dipotong tunjangan pensiun : 
- jika usia < 30 pemotongan tunjangan 10% gaji
- jika usia 30-40 pemotongan tunjangan 15% gaji
- jika usia di atas 40, pemotongan 20% gaji
4 - Terakhir, jika karyawan Pria, maka dari hasil akhir masih dipotong lagi 5% , untuk tunjangan keluarga
'''




'''
class StandarGaji:
	def __init__(self,rank):
		self.rank = rank
	
		

	def Gaji(self):
		if self.rank == 'Manager':
			self.gaji = 6500000
		elif self.rank == 'Staff':
			self.gaji = 3500000
		elif self.rank == 'OB':
			self.gaji = 2000000
		else:
			self.gaji = 2500000
		return self.gaji
'''

def StandarGaji(rank):
	if rank == 'Manager':
			gaji = 6500000
	elif rank == 'Staff':
			gaji = 3500000
	elif rank == 'OB':
			gaji = 2000000
	else:
			gaji = 2500000
	return gaji



