from django.contrib import admin
from accounts.models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'wins')

##this is how you change the column names in the django admin
    def user_info(self, obj):
        return obj.description


admin.site.register(UserProfile, UserProfileAdmin)
