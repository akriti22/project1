from django.contrib import admin
from testapp.models import Employee
from testapp.models import Manager


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'e_name', 'e_no', 'e_sal', 'e_addr']


class ManagerAdmin(admin.ModelAdmin):
    list_display = ['m_no', 'm_name', 'm_sal']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Manager, ManagerAdmin)
#admin.site.register(EmployeeAdmin)
#admin.site.register(ManagerAdmin)
