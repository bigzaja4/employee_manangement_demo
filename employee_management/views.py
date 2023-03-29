from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentList(APIView):
    
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
    def get(self, request, department_id):
        try:
            department = Department.objects.get(pk=department_id)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    
    def post(self, request):
        department = DepartmentSerializer(data=request.data)
        if department.is_valid():
            department.save()
            return Response(department.data, status=status.HTTP_201_CREATED)
        else:
            return Response(department.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class EmployeeList(APIView):
    
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    def get(self, request, employee_id):
        try:   
            employee = Employee.objects.get(pk=employee_id)
        except Employee.DoesNotExist:
            return Response(data={'msg': f'Employee id {employee_id} does not exists'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def post(self, request):
        employee = EmployeeSerializer(data=request.data)
        if(employee.is_valid()):
            employee.save()
            return Response(employee.data, status=status.HTTP_201_CREATED)
        else:
            return Response(employee.error_messages, status=status.HTTP_400_BAD_REQUEST)