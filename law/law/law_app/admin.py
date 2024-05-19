from django.contrib import admin
from law_app.models import Judge, Assistant, Case, QueryType

# Register your models here.
admin.site.register(Judge)
admin.site.register(Assistant)
admin.site.register(Case)
admin.site.register(QueryType)