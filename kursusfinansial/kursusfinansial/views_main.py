''' views_main.py , file ini adalah View untuk menampilkan template '''

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

def index(request):
	isi = {'title' : 'Kursus Finansial Indonesia - Rian Irawan Hariadi'  }
	return render(request,'index.html',isi,content_type = 'text/html')