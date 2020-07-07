from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import User


# UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'cuit')
# admin.site.register(User, UserAdmin)


#
# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         # original form fieldsets, expanded
#         # new fieldset added on to the bottom
#         # group heading of your choice; set to None for a blank space instead of a header
#         *UserAdmin.fieldsets,
#         (
#             'Custom Field Heading',
#             {
#                 'fields': (
#                     'cuit',
#                 ),
#             },
#         ),
#     )
#     list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'cuit')
#
# admin.site.register(User, CustomUserAdmin)
