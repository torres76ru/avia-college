from django.utils import timezone
from .models import EmailSend

class FreeTime(object):
	"""Giving free time for registration"""

	def __init__(self):
		time = timezone.now()
		self.year = time.year
		self.month = time.month
		self.day = time.day

		self.hour = time.hour + 3
		self.minute = time.minute
		if self.month < 7 and self.day < 22:
			self.year = 2021
			self.month = 6
			self.day = 21

			self.hour = 8
			self.minute = 0
		if self.hour > 15 or self.hour < 8:
				self.minute = 0
		if self.hour < 8:
			self.hour = 8
		
	def getCampaignTime(self):
		# Дата
		year = self.year
		month = self.month
		day = self.day

		# Время
		hour = self.hour
		minute = self.minute

		#Список
		cmpgnT = []
		date = "{}-{}-{}".format(year, str(month).zfill(2), str(day).zfill(2))

		#Счетчик
		k = 0

		#Заполнение списка
		while month < 13:
			while day < 32:
				while hour < 16 and hour > 7:
					while minute < 51:
						while minute % 10 != 0:
							minute += 1
						if month > 7 and day > 15:
							break
						if day < 31:
							if timezone.datetime.strptime('{}{}{}'.format(year, str(month).zfill(2), str(day).zfill(2)), '%Y%m%d').isoweekday() > 5:
								break
						date = "{}-{}-{}".format(year, str(month).zfill(2), str(day).zfill(2))
						if date in ['2020-01-24', '2022-07-01']:
							break
						time = "{}:{}:00".format(str(hour).zfill(2), str(minute).zfill(2))
						cmpgnT.append([])
						cmpgnT[k].append(date)
						cmpgnT[k].append(time)
						k += 1
						minute += 10
					if month > 7 and day > 15:
						break
					hour += 1
					minute = 0
				if month > 7 and day > 15:
					break
				hour = 8
				day += 1

			if month > 7 and day > 15:
				break
			month += 1
			day = 1
		#Возвращаем список позиций времени продолжительности кампании
		return cmpgnT

	def getCloseTime(self):
		return [n.date.isoformat().replace('+00:00', '').split('T') for n in EmailSend.objects.all()]
	def getFreeTime(self):
		
		#dbd = [n.date.isoformat().replace('+00:00', '').split('T') for n in EmailSend.objects.all()]

		cmpgnT = self.getCampaignTime()
		closeT = self.getCloseTime()
		freeTime_arr = []
		for i in cmpgnT:
			f = True
			for j in closeT:
				if i == j:
					f = False
					break
			if f:
				freeTime_arr.append(i)

		return freeTime_arr