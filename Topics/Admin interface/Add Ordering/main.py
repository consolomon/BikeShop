from django.contrib import admin


class FilmAdmin(admin.ModelAdmin):
    list_display = ("writer", "director", "box_office")
    ordering = ("box_office",)