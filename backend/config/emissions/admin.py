from django.contrib import admin
from .models import Organization, DataSource, EmissionRecord

admin.site.register(Organization)
admin.site.register(DataSource)
admin.site.register(EmissionRecord)