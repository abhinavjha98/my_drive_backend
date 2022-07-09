from django.contrib import admin
from .models import CustomUser, Profession, ReferalCode, ReferalUser
# Register your models here.
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "User details",{
                'fields':(
                    'dob',
                    'profession',
                    'user_id',
                    'profile_photo',
                    'finger_print',
                    'pass_code',
                    'user_face',
                    'user_storage',
                    'dark_mode',
                    'notification',
                    'referal_code',
                    'referal_count',
        )
            }
        )
    )

class ProfessionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('name','slug',)
    search_fields = ('name','slug',)
    list_filter = ('name','slug',)

class ReferalUserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('refer_by','refer_to','refer_code',)
    search_fields = ('refer_to','refer_by','refer_code',)
    list_filter = ('refer_to','refer_by','refer_code',)

class ReferalCodeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('refer_code',)
    search_fields = ('refer_code',)
    list_filter = ('refer_code',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profession,ProfessionAdmin)
admin.site.register(ReferalUser,ReferalUserAdmin)
admin.site.register(ReferalCode,ReferalCodeAdmin)