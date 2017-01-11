''' Modul PotonganGaji '''

class Pajak:
	def __init__(self):
		self.PPN = 0.1 
		self.PPH21 = 0.05

	def PotonganPPN(self):
		return self.PPN

	def PotonganPPH21(self):
		return self.PPN
	


class Tunjangan:
	"""docstring for Tunjangan"""
	def __init__(self, arg):
		super(Tunjangan, self).__init__()
		self.arg = arg
		