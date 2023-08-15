from django.contrib import admin
from .models import *

from import_export.admin import ExportActionMixin


# Register your models here.
class Valueadmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["name", "reg", "dept", "domain", "email", "phone", "reason"]


admin.site.register(Values, Valueadmin)
# Register your models here.
