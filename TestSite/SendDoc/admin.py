from django.contrib import admin
from .models import EmailSend

#admin.site.register(EmailSend)

# class QueueAdmin(admin.ModelAdmin):
# 	pass

# admin.site.register(EmailSend)

@admin.register(EmailSend)
class QueueAdmin(admin.ModelAdmin):
	list_display = ('id','date', 'email')
	list_filter = ( 'date', 'email')	
