# // Program python 34, jawaban pertanyaan Muhammad AR
'''
[ask]
pola: 
input 9 hasilkan [1,2,3,4,5,6,7,8,9] terlebih dahulu

input 2, karena ada list array dari input pertama maka:
[1,2,3,4,5,6,7,8,9]
[1,2]
------------------------- +
[2,4,3,4,5,6,7,8,9] <- ini yg dicetak & di simpan di list array hasil

input 3 maka:
[2,4,3,4,5,6,7,8,9]
[1,2,3]
------------------------- +
[3,6,6,4,5,6,7,8.9] <- inilah hasil input 3


'''



def MasukkanList1():
	theList1 = []
	total = int()
	total = int(input('Masukkan jumlah list ke-1: ')) + 1
	i = int()
	i = 1
	for i in range (i,total):
		theList1.append(i)

	# print (theList1)
	return theList1


def MasukkanList2():
	theList2 = []
	total = int()
	total = int(input('Masukkan jumlah list ke-2: ')) + 1
	i = int()
	i = 1
	for i in range (i,total):
		theList2.append(i)

	# print (theList2)
	return theList2


theList1 =  MasukkanList1()
theList2 =  MasukkanList2()
print(theList1)
print(theList2)


from itertools import zip_longest
z = [ x+y for x,y in zip_longest(theList1, theList2, fillvalue=0 )][::1] 
print('Jumlah kedua list: ', z)


'''
Reference:
- How to add list with different length:
sumur: http://stackoverflow.com/questions/17521145/add-two-lists-of-different-lengths-in-python-start-from-the-right

'''




