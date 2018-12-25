from django.shortcuts import render
from testapp.models import Employee
from testapp.models import Manager

# Create your views here.


def employee_info_view(request):
    employees=Employee.objects.all()
    return render(request, 'testapp/results.html', {'employees' : employees})
