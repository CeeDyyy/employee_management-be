from django.contrib import admin

from web.models import *

class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('setting','value')
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(SystemSetting,SystemSettingAdmin)

class NativeLanguageAdmin(admin.ModelAdmin):
    list_display = ('short_lang','lang')
admin.site.register(NativeLanguage,NativeLanguageAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user','employee_id')
    search_fields = ('user__username','employee',)
admin.site.register(Employee,EmployeeAdmin)


#ตัวอย่างการเอาข้อมูลไปแสดงหน้า localhost:8004/admin ที่จะสามารถแก้อะไรตรงนั้นได้เลย
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Users._meta.get_fields()]    # ข้อมูลที่ต้องการโชว์ ตามที่เขียนคือมาหมด แต่ถ้าอยากได้แค่บางอันก็เขียนแบบอันบน ๆ
    search_fields = ('user_id',)            # สามารถ search ด้วยอะไรได้
admin.site.register(Users,UserAdmin)      # Model,ชื่อ class อันนี้