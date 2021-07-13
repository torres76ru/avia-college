import datetime
from django.db import models

from django.utils import timezone

class EmailSend(models.Model):
	# name = models.CharField('Имя', max_length=20)
	# surname = models.CharField('Фамилия',max_length=30)
	email = models.EmailField('E-mail', unique=True)
	date = models.DateTimeField('Дата', unique=True)
	key  = models.CharField('Ключ', max_length = 20)

	def __str__(self):
		return self.email


	class Meta:
		verbose_name='Встали в электронную очередь'
		verbose_name_plural ='Встали в электронную очередь'

class Confirmation(models.Model):
	email = models.EmailField('E-mail', unique=True)
	date = models.DateTimeField('Дата', unique=True)
	sent_date = models.DateTimeField('Дата регистрации')
	key  = models.CharField('Ключ', max_length = 20)
	confirm = models.BooleanField('Подтверждение', default=False)
	
	def __str__(self):
		return self.email

	def confirm(self, k):
		pass

	class Meta:
		verbose_name='Подтвержден?'
		verbose_name_plural ='Подтвержден?'