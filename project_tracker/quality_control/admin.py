from django.contrib import admin
from quality_control.models import BugReport, FeatureRequest

class BugReportInLine(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'project','task' ,'status','priority','created_at','updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True

class FeatureRequestInLine(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'project','task' ,'status','priority','created_at','updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project','task','status','priority','created_at','updated_at')
    list_filter = ('project','task','status','priority')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('created_at',)
    fieldsets = (
        (None, {'fields':('title', 'description')}),
        ('Connected task',{'fields':('project','task')}),
        ('Bug report status',{'fields':('status','priority')}),
        ('Timestamps',{'fields':('created_at','updated_at')}),
    )

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project','task','status','priority','created_at','updated_at')
    list_filter = ('project','task','status','priority')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('created_at',)
    fieldsets = (
        (None, {'fields':('title', 'description')}),
        ('Connected task',{'fields':('project','task')}),
        ('Bug report status',{'fields':('status','priority')}),
        ('Timestamps',{'fields':('created_at','updated_at')}),
    )
