from django.contrib import admin
from . import models
# Register your models here.

# admin.site.site_url = "/site/"
admin.site.site_title = "Zexa HRM Administration"
class AdminEmployee(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()

    def mark_as_active(self, request, queryset):
        queryset.update(status='active')
    mark_as_active.short_description = "Mark selected employees as Active"

    def mark_as_inactive(self, request, queryset):
        queryset.update(status='inactive')
    mark_as_inactive.short_description = "Mark selected employees as Inactive"

    def mark_as_retired(self, request, queryset):
        queryset.update(status='retired')
    mark_as_retired.short_description = "Mark selected employees as Retired"

    def mark_as_fired(self, request, queryset):
        queryset.update(status='fired')
    mark_as_fired.short_description = "Mark selected employees as Fired"


    actions = [mark_as_active,mark_as_inactive,mark_as_retired,mark_as_fired]
    readonly_fields = ('id',)
    list_display = ['id','name','age','gender','title','salary','department','reports_to','status']
    list_display_links = ['id','name','age','gender','title','salary','department','reports_to','status']
    search_fields = ('id','name','age','salary','department__name')
    list_filter = (('reports_to',admin.RelatedOnlyFieldListFilter),'department' ,'status','title','gender')
    list_per_page = 10

admin.site.register(models.Employee,AdminEmployee)

class AdminPayroll(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.recorded_by = request.user
        obj.save()

    raw_id_fields = ('employee',)
    readonly_fields = ('id',)
    list_display = ['employee','payment_amount','timestamp_of_payment']
    list_display_links = ['employee', 'payment_amount', 'timestamp_of_payment']
    search_fields = ('employee','payment_amount')
    list_filter = ['timestamp_of_payment','recorded_by']

admin.site.register(models.Payroll,AdminPayroll)

class AdminDepartment(admin.ModelAdmin):
    readonly_fields = (id,)
    list_display = ['name','total_employees']
admin.site.register(models.Department,AdminDepartment)

admin.site.register(models.Role)

class AdminDeptManager(admin.ModelAdmin):
    list_display = ['department','manager']

admin.site.register(models.Department_Manager,AdminDeptManager)
