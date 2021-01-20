from django.contrib import admin

# Register your models here

from .models import Members

class MembersAdmin(admin.ModelAdmin):
    list_display=('username','user_email')
    pass

admin.site.register(Members,MembersAdmin)


