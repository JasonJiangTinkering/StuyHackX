from django.contrib import admin
from school.models import School
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','email_extension', 'get_school_score')
    readonly_fields = ('get_school_score',)

    def get_school_score(self, obj):
        return obj.school_score
        
admin.site.register(School, SchoolAdmin)
