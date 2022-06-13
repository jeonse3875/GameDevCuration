from django.contrib import admin
from .models import *

class IdDisplayAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(Game, IdDisplayAdmin)
admin.site.register(Tag, IdDisplayAdmin)