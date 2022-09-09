from django.contrib import admin

from . import models


# This is required to view Notes in the admin panel
class NotesAdmin(admin.ModelAdmin):
    # below is for showing the note title at the top view of the table in admin vs the default 'Notes Object 1'
    list_display = ('title',)


admin.site.register(models.Notes, NotesAdmin)
