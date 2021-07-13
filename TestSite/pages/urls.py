from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('news/', views.news, name='news'),
	path('priemcomissia/', views.priemcomissia, name='priemcomissia'),
	path('pravilapriema/', views.pravilapriema, name='pravilapriema'),
	path('infooprieme/', views.infooprieme, name='infooprieme'),
	path('reitingoviespiske/', views.reitingoviespiske, name='reitingoviespiske'),
	path('prikazeozachislenie/', views.prikazeozachislenie, name='prikazeozachislenie'),
	path('setevoe_i_sistemnoe_administririvanie/', views.setevoe_i_sistemnoe_administririvanie, name='setevoe_i_sistemnoe_administririvanie'),
	path('proizvodstvo_aviocionneh_dvigateley/', views.proizvodstvo_aviocionneh_dvigateley, name='proizvodstvo_aviocionneh_dvigateley'),
	path('tehnologii_mashinostroenia/', views.tehnologii_mashinostroenia, name='tehnologii_mashinostroenia'),
	path('informatsionnie_sisteme_i_programmirovanie/', views.informatsionnie_sisteme_i_programmirovanie, name='informatsionnie_sisteme_i_programmirovanie'),
	path('pravo_i_organisacia_soc_obespechenia/', views.pravo_i_organisacia_soc_obespechenia, name='pravo_i_organisacia_soc_obespechenia'),
	path('electrichestvo/', views.electrichestvo, name='electrichestvo'),
	path('technologia_metaloobrabatevaushego_proizvodstva/', views.technologia_metaloobrabatevaushego_proizvodstva, name='technologia_metaloobrabatevaushego_proizvodstva'),
	path('instrtaction/', views.instrtaction, name='instrtaction'),
	path('instrtaction2/', views.instrtaction2, name='instrtaction2'),
	path('instrtaction3/', views.instrtaction3, name='instrtaction3')
	
]