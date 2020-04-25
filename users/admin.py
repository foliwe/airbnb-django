from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)  # with decorator. This works because it is on top
class CustomUserAdmin(UserAdmin):

    # admin.site.register(models.User, CustomUserAdmin) will still work instead of @admin.register(models.User)
    """ Custom User Admin """

    # list_display = ("username", "email", "gender", "language", "currency", "superhost")

    # list_filter = ("superhost", "language")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Fields",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "date_of_birth",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
