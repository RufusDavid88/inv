from import_export import resources
from .models import Lowerparel
from .models import Bhiwandi
from .models import STORE

class LowerparelResource(resources.ModelResource):
    class Meta:
        model = Lowerparel



class BhiwandiResource(resources.ModelResource):
    class Meta:
        model = Bhiwandi



class STOREResource(resources.ModelResource):
    class Meta:
        model = STORE
