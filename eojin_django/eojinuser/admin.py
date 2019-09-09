from django.contrib import admin
from .models import Eojinuser

# Register your models here.


class EojinuserAdmin(admin.ModelAdmin):
    list_display = ('email', )


admin.site.register(Eojinuser, EojinuserAdmin)
