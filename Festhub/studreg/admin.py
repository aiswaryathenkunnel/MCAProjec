from django.contrib import admin
from . models import Studreg


class StudregAdmin(admin.ModelAdmin):
    list_display = ["stud_name", "stud_place", "stud_email", "stud_contactno", "stud_age", "clg_id", "dept_id", "stud_admno", "stud_course", "stud_batch", "stud_username", "stud_password", "stud_status"]


admin.site.register(Studreg, StudregAdmin)