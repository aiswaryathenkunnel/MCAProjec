from django.contrib import admin
from .models import Eventadd


class EventaddAdmin(admin.ModelAdmin):
    list_display = ["fest_id", "event_name", "event_desc", "event_fees", "part_type", "max_part", "time_from", "time_to", "venue"]


admin.site.register(Eventadd, EventaddAdmin)