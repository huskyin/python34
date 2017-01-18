'''
Program managedata.py
Mengolah data yang didapat dari file lain (txt)

dibuat oleh : Rian Irawan Hariadi , www.huskyin.com 
'''

''' Mencari Direktory yg aktif
sumur: http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
'''

import os

dir_path =  os.path.dirname(os.path.realpath(__file__))
print (dir_path)

cwd = os.getcwd()
print(cwd)

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))











