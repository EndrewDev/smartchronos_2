from .models import CustomUser
from django.contrib import admin

# Register your models here.
class  CustomUserAdmin(admin.ModelAdmin):
    pass
    
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'registration')
#     list_filter = ('username', 'registration', 'first_name')


admin.site.register(CustomUser, CustomUserAdmin)


# @admin.register(UserGroup)
# class UserGroupAdmin(admin.ModelAdmin):
#     list_display = ('user', 'get_group_display')
#     list_filter = ('option',)
#     search_fields = ('user__username',)

#     def get_group_display(self, obj):
#         return obj.get_option_display()
    
#     get_group_display.short_description = "Group"

# admin.site.register(UserGroup, UserGroupAdmin)
