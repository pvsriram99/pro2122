from django.contrib import admin
from a2zapp.models import empmodel, news, calender

# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display = ['EmpName', 'EmpId', 'Designation', 'Dateofjoin', 'Department', 'Salary', 'Experience']
admin.site.register(empmodel, empadmin)

class newsadmin(admin.ModelAdmin):
    list_display = ['occation']
admin.site.register(news, newsadmin)

class calenderadmin(admin.ModelAdmin):
    list_display = ['Date', 'Occation']
admin.site.register(calender, calenderadmin)