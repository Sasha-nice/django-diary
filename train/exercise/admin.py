from django.contrib import admin
from exercise.models import Exercise


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'musc')


admin.site.register(Exercise, UserAdmin)
