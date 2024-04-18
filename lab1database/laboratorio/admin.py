from django.contrib import admin
from .models import Database

class DatabaseAdmin(admin.ModelAdmin):
    readonly_fields = [f.name for f in Database._meta.get_fields()]


admin.site.register(Database, DatabaseAdmin)