from django.contrib import admin
from training.models import Training


class UserAdmin(admin.ModelAdmin):
    list_display = ('date',)


admin.site.register(Training, UserAdmin)
