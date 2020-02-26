from rest_framework import viewsets

from .serializers import Lowerparel, LowerparelSerializer
from .models import Lowerparel


class LowerparelViewSet(viewsets.ModelViewSet):
    queryset = Lowerparel.objects.all().order_by('name')
    serializer_class = LowerparelSerializer




from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset

from .resources import LowerparelResource
from .models import Lowerparel

def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        Lowerparel_resource = LowerparelResource()
        dataset = Lowerparel_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response

    return render(request, 'export.html')


def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        Lowerparel_resource = LowerparelResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
            result = Lowerparel_resource.import_data(dataset, dry_run=True)
        elif file_format == 'JSON':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
            # Testing data import
            result = Lowerparel_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            # Import now
            Lowerparel_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')
