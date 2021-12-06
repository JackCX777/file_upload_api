from django.contrib import admin
from .models import UploadedFile


class UploadedFileAdmin(admin.ModelAdmin):
    model = UploadedFile
    list_display = ('id', 'upload_date', 'file', 'status', 'finish_date', 'result', )
    readonly_fields = ('upload_date', )
    fieldsets = (
        (None, {'fields': ('file', 'upload_date', 'status', 'finish_date', 'result', )}),
    )


admin.site.register(UploadedFile, UploadedFileAdmin)
