from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['department', 'date_joined']
    ordering_fields = ['name', 'date_joined']

def chart_view(request):
    dept_data = Department.objects.annotate(employee_count=Count('employee')).values('name', 'employee_count')
    
    attendance_data = Attendance.objects.filter(date__year=date.today().year).values('status').annotate(count=Count('status'))
    return render(request, 'chart.html', {'dept_data': dept_data, 'attendance_data': attendance_data})