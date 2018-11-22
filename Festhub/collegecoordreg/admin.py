from django.contrib import admin
from .models import Collegecoordreg


class CollegecoordregAdmin(admin.ModelAdmin):
    list_display = ["coord_name", "coord_contactno", "coord_email", "clg_name", "clg_website", "clg_contactno", "clg_place", "clg_pincode", "clg_dist", "clg_startdate", "clg_licenceno", "clg_type", "clg_username", "clg_password", "clg_status"]


admin.site.register(Collegecoordreg, CollegecoordregAdmin)
