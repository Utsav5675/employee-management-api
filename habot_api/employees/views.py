from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import Employee
from .serializers import EmployeeSerializer


# Pagination: 10 employees per page
class EmployeePagination(PageNumberPagination):
    page_size = 10


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    # Filtering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'role']

    # Pagination
    pagination_class = EmployeePagination
