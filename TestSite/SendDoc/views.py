from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailSendForm, DeleteQueueForm
from .models import EmailSend
from .freetime import FreeTime
import random

def send(request):
	#Помечаем что пока сообщение не отправленно
	sent = False

	#Получаем свободное время
	fT = FreeTime()
	dt_arr = fT.getFreeTime()

	if request.method == 'POST':
		# Form was submitted
		form = EmailSendForm(request.POST)
		if form.is_valid():
			#Сохранение в БД
			form.save();

			#Генерация пароля-ключа
			chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
			length = 15
			password =''
			for i in range(length):
				password += random.choice(chars)

			#Создание сообщения на e-mail
			cd = form.cleaned_data
			months=["","Января","Февраля","Марта","Апреля","Мая","Июня","Июля","Августа","Сентября","Октября","Ноября","Декабря"];
			obj = EmailSend.objects.get(email=cd['to'])
			subject = 'Авиационный колледж'
			password += str(obj.id)
			cancel_link ='https://aviacollege.ru/cancel/?key={}'.format(password)
			message = 'Ваша запись в приемную комиссию авиационного колледжа назначена на {} {} в {}:{}.\n\nВаш регистрационный номер {}\n\nДля отмены регистрации перейдите по ссылке:\n{}.'.format(cd['date'].day, months[cd['date'].month], str(cd['date'].hour).zfill(2), str(cd['date'].minute).zfill(2), obj.id, cancel_link)
			form.save_key(password)
			
			
			send_mail(subject, message, 'priem@aviacollege.ru',[cd['to']])
			sent = True
	else:
		form = EmailSendForm()


	return render(request, 'SendDoc/share.html', {'form': form,
																 'sent': sent,
																 'dt_arr': dt_arr
																 })


def cofirmation(request):
	pass


def cancel(request):
	deleted = False
	if request.method == 'POST':
		form = DeleteQueueForm(request.POST)
		if form.is_valid():
			form.delete_queue()
			deleted = True
	else:
		form = DeleteQueueForm(initial={'key':request.GET.get("key")})

	return render(request, 'SendDoc/cancel.html',{'key': request.GET.get("key"),
																 'form': form,
																 'deleted': deleted})

