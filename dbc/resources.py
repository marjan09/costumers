from import_export import resources
from .models import InsertToDb

class PersonResource(resources.ModelResource):
    class Meta:
        model = InsertToDb