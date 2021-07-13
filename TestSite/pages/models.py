from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



# Страницы

# Главная
class HomePage(models.Model):
	name = models.CharField(max_length = 20)
	content = models.TextField(max_length = 99999)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Главная страница"
		verbose_name_plural = "Главная страница"

class News(models.Model):
	title = models.CharField('Заголовок', max_length = 200)
	content = RichTextUploadingField('Контент')
	create_time = models.DateTimeField('Дата')

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-create_time', '-id']
		verbose_name = "Новости"
		verbose_name_plural = verbose_name

# Абитуриаенту

class PriemComission(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Приёмная комиссия"
		verbose_name_plural = "Приемная комиссия"

class Pravilapriema(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Правила приёма"
		verbose_name_plural = "Правила приёма"

class Infooprieme(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Информация о приеме"
		verbose_name_plural = "Информация о приеме"


class Reitingoviespiske(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Рейтинговые списки"
		verbose_name_plural = "Рейтинговые списки"

class Prikazeozachislenie(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Приказы о зачислении"
		verbose_name_plural = "Приказы о зачислении"

# Специальности

class S1(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "СЕТЕВОЕ И СИСТЕМНОЕ АДМИНИСТРИРОВАНИЕ"
		verbose_name_plural = "СЕТЕВОЕ И СИСТЕМНОЕ АДМИНИСТРИРОВАНИЕ"

class S2(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ПРОИЗВОДСТВО АВИАЦИОННЫХ ДВИГАТЕЛЕЙ"
		verbose_name_plural = "ПРОИЗВОДСТВО АВИАЦИОННЫХ ДВИГАТЕЛЕЙ"

class S3(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ТЕХНОЛОГИЯ МАШИНОСТРОЕНИЯ"
		verbose_name_plural = "ТЕХНОЛОГИЯ МАШИНОСТРОЕНИЯ"

class S4(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ"
		verbose_name_plural = "ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ"

class S5(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ПРАВО И ОРГАНИЗАЦИЯ СОЦИАЛЬНОГО ОБЕСПЕЧЕНИЯ"
		verbose_name_plural = "ПРАВО И ОРГАНИЗАЦИЯ СОЦИАЛЬНОГО ОБЕСПЕЧЕНИЯ"

class S6(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ЭЛЕКТРИЧЕСКИЕ СТАНЦИИ, СЕТИ И СИСТЕМЫ"
		verbose_name_plural = "ЭЛЕКТРИЧЕСКИЕ СТАНЦИИ, СЕТИ И СИСТЕМЫ"

class S7(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "ТЕХНОЛОГИЯ МЕТАЛЛООБРАБАТЫВАЮЩЕГО ПРОИЗВОДСТВА"
		verbose_name_plural = "ТЕХНОЛОГИЯ МЕТАЛЛООБРАБАТЫВАЮЩЕГО ПРОИЗВОДСТВА"

# Подать документы
class Instrtaction(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Электронная почта"
		verbose_name_plural = verbose_name

class Instrtaction2(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Электронная запись"
		verbose_name_plural = verbose_name

class Instrtaction3(models.Model):
	name = models.CharField(max_length = 20)
	content = RichTextUploadingField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Почта России"
		verbose_name_plural = verbose_name
# ========================================================
# Другое
class Pages(models.Model):
	name = models.CharField(max_length = 100)
	url = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Страница"
		verbose_name_plural = "Страницы"

class Profession(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Професси"
		verbose_name_plural = "Професии"

#=========================================================