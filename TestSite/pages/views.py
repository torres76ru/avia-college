from django.shortcuts import render
from .models import HomePage, News, PriemComission, Pravilapriema, Infooprieme, Reitingoviespiske, Prikazeozachislenie, S1, S2, S3, S4, S5, S6, S7, Instrtaction, Instrtaction2, Instrtaction3
from .functions import makeHash

def index(request):
	content = HomePage.objects.all()
	return render(
		request,
		'pages/homePage.html',
		{"content": makeHash(content)}
	)

def news(request):
	content = News.objects.all()
	return render(
		request,
		'pages/news.html',
		{"content": content}
	)

# Абитуриенту
def priemcomissia(request):
	content = PriemComission.objects.all()
	return render(
		request,
		'pages/priemcomissia.html',
		{"content": makeHash(content)}
	)

def pravilapriema(request):
	content = Pravilapriema.objects.all()
	return render(
		request,
		'pages/pravilapriema.html',
		{"content": makeHash(content)}
	)

def infooprieme(request):
	content = Infooprieme.objects.all()
	return render(
		request,
		'pages/infooprieme.html',
		{"content": makeHash(content)}
	)

def reitingoviespiske(request):
	content = Reitingoviespiske.objects.all()
	return render(
		request,
		'pages/reitingoviespiske.html',
		{"content": makeHash(content)}
	)

def prikazeozachislenie(request):
	content = Prikazeozachislenie.objects.all()
	return render(
		request,
		'pages/prikazeozachislenie.html',
		{"content": makeHash(content)}
	)

# Специальности
def setevoe_i_sistemnoe_administririvanie(request):
	content = S1.objects.all()
	return render(
		request,
		'pages/setevoe_i_sistemnoe_administririvanie.html',
		{"content": makeHash(content)}
	)

def proizvodstvo_aviocionneh_dvigateley(request):
	content = S2.objects.all()
	return render(
		request,
		'pages/proizvodstvo_aviocionneh_dvigateley.html',
		{"content": makeHash(content)}
	)

def tehnologii_mashinostroenia(request):
	content = S3.objects.all()
	return render(
		request,
		'pages/tehnologii_mashinostroenia.html',
		{"content": makeHash(content)}
	)

def informatsionnie_sisteme_i_programmirovanie(request):
	content = S4.objects.all()
	return render(
		request,
		'pages/informatsionnie_sisteme_i_programmirovanie.html',
		{"content": makeHash(content)}
	)

def pravo_i_organisacia_soc_obespechenia(request):
	content = S5.objects.all()
	return render(
		request,
		'pages/pravo_i_organisacia_soc_obespechenia.html',
		{"content": makeHash(content)}
	)

def electrichestvo(request):
	content = S6.objects.all()
	return render(
		request,
		'pages/electrichestvo.html',
		{"content": makeHash(content)}
	)

def technologia_metaloobrabatevaushego_proizvodstva(request):
	content = S7.objects.all()
	return render(
		request,
		'pages/technologia_metaloobrabatevaushego_proizvodstva.html',
		{"content": makeHash(content)}
	)
def instrtaction(request):
	content = Instrtaction.objects.all()
	return render(
		request,
		'pages/instrtaction.html',
		{"content": makeHash(content)}
	)

def instrtaction3(request):
	content = Instrtaction3.objects.all()
	return render(
		request,
		'pages/instrtaction3.html',
		{"content": makeHash(content)}
	)

def instrtaction2(request):
	content = Instrtaction2.objects.all()
	return render(
		request,
		'pages/instrtaction2.html',
		{"content": makeHash(content)}
	)
