from django.contrib import admin
from .models import Festadd


class FestaddAdmin(admin.ModelAdmin):
    list_display = ["fest_name", "fest_theme", "dept_id", "fest_date", "fest_type"]


admin.site.register(Festadd, FestaddAdmin)