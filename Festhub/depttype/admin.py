from django.contrib import admin
from .models import Depttype


class DepttypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Depttype, DepttypeAdmin)
