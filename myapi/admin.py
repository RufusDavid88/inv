from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Lowerparel
from .models import Bhiwandi
from .models import STORE

@admin.register(Lowerparel)
class LowerparelAdmin(ImportExportModelAdmin):
    pass

@admin.register(Bhiwandi)
class BhiwandiAdmin(ImportExportModelAdmin):
    pass

@admin.register(STORE)
class STOREAdmin(ImportExportModelAdmin):
    pass



