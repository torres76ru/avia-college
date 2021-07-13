from django import forms
from .models import EmailSend

class EmailSendForm(forms.Form):
	# name = forms.CharField(label='Ваше имя:', max_length=20)
	# surname = forms.CharField(label='Ваша фамилия:', max_length=30)
	to = forms.EmailField(label='Ваш e-mail:', required=True)
	date = forms.DateTimeField(label='дата и время:', required=True)

	def save(self):
		new_send = EmailSend.objects.create(
			email=self.cleaned_data['to'],
			date=self.cleaned_data['date'],
			#key = ""
			
		)
		return new_send
	def save_key(self,k):
		e = EmailSend.objects.get(email = self.cleaned_data['to'])
		e.key = k
		e.save()

class DeleteQueueForm(forms.Form):
	key = forms.CharField(max_length=20, required=True)

	def delete_queue(self):
		try:
			EmailSend.objects.filter(key = self.cleaned_data['key']).delete()
		except:
			return