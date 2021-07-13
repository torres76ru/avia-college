from django import forms

class RegForm(forms.Form):
	REQ = True
	surname = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'placeholder': 'Иванов'}), max_length=50, required=REQ)
	name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'placeholder': 'Иван'}), max_length=50, required=REQ)
	midname = forms.CharField(label="Отчество", widget=forms.TextInput(attrs={'placeholder': 'Иванович'}), max_length=50, required=REQ)
	birthday = forms.CharField(label="Дата рождения", widget=forms.TextInput(attrs={'placeholder': 'ДД/ММ/ГГГГ'}), required=REQ)
	obraz = forms.CharField(label="Образование", widget=forms.TextInput(attrs={'list': 'lst'}), max_length=100, required=REQ)
	CHOICES = [('1', 'Нужно'), ('2', 'Ненужно')]
	hostel = forms.BooleanField(label="Общежитие требуется", required=REQ)

	ps = forms.CharField(label="Серия", widget=forms.TextInput(attrs={'data-mask':"00 00"}), max_length=5, min_length=5, required=REQ)
	pn = forms.CharField(label="Номер", widget=forms.TextInput(attrs={'data-mask':"000000"}), max_length=6, min_length=6, required=REQ)
	pc = forms.CharField(label="Код подразделения", widget=forms.TextInput(attrs={'data-mask':'000-000'}),max_length=7, min_length=7, required=REQ)
	pi = forms.CharField(label="Кем выдан", max_length=150, required=REQ)
	pd = forms.CharField(label="Когда выдан", widget=forms.TextInput(attrs={'placeholder': 'ДД/ММ/ГГГГ'}), required=REQ)
	pg = forms.ImageField(label="Фото главной страницы", required=REQ)
	pp = forms.ImageField(label="Фото страницы с регистрацией", required=REQ)

	an = forms.CharField(label="Номер", required=REQ)
	ad = forms.CharField(label="Когда выдан", widget=forms.TextInput(attrs={'placeholder': 'ДД/ММ/ГГГГ'}), required=REQ)
	ai = forms.CharField(label="Кем выдан", required=REQ)
	ag = forms.ImageField(label="Фото главной страницы аттестата", required=REQ)
	am = forms.ImageField(label="Фото страницы с оценками", required=REQ)

	phone = forms.CharField(label="Телефон для связи", required=REQ)
	# email = forms.EmailField(label="Электронная почта", required=REQ)
	
	
	statement = forms.ImageField(label="Фото заяления", required=REQ)
	agreement = forms.ImageField(label="Фото согласия на обработку данных", required=REQ)

	agree = forms.BooleanField(label="Даю согласие на обработку данных", required=REQ)