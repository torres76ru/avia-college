from django.contrib import admin
from pages.models import HomePage, News, PriemComission, Pravilapriema, Infooprieme, Reitingoviespiske, Prikazeozachislenie, S1, S2, S3, S4, S5, S6, S7, Instrtaction, Instrtaction2, Instrtaction3
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class HomePageAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = HomePage
		fields = '__all__'

class PagesAdmin(admin.ModelAdmin):
	form =  HomePageAdminForm
	class Meta:
		verbose_name = "Страницы"
		verbose_name_plural =  "Страница"

class SpecAdmin(admin.ModelAdmin):
	class Meta:
		verbose_name = "Специальности"
		verbose_name_plural =  "Специльности"
# Главная
admin.site.register(HomePage, PagesAdmin)
# Новости
admin.site.register(News, PagesAdmin)
#Абитуриенту
admin.site.register(PriemComission, PagesAdmin)
admin.site.register(Pravilapriema, PagesAdmin)
admin.site.register(Infooprieme, PagesAdmin)
admin.site.register(Reitingoviespiske, PagesAdmin)
admin.site.register(Prikazeozachislenie, PagesAdmin)
# admin.site.register(Pages, PagesAdmin)
# admin.site.register(Profession, PagesAdmin)

# Специальности
admin.site.register(S1, SpecAdmin)
admin.site.register(S2, SpecAdmin)
admin.site.register(S3, SpecAdmin)
admin.site.register(S4, SpecAdmin)
admin.site.register(S5, SpecAdmin)
admin.site.register(S6, SpecAdmin)
admin.site.register(S7, SpecAdmin)

# Подать документы
admin.site.register(Instrtaction, SpecAdmin)
admin.site.register(Instrtaction2, SpecAdmin)
admin.site.register(Instrtaction3, SpecAdmin)

