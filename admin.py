from django.contrib import admin
from app.models import schedule,apt,mail,blog,contact

# Register your models here.

@admin.register(schedule)
class scheduleAdmin(admin.ModelAdmin):
    list_display=('name','phone','time','date','pic','message',)
    
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','subject','message',)
    
@admin.register(apt)
class aptAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','date','time','subject','message',)
    
@admin.register(mail)
class mailAdmin(admin.ModelAdmin):
    list_display=('email',)
    
@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass