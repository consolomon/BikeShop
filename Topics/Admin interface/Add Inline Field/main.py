from django.contrib import admin

class ActorInLine(admin.TabularInline):
    can_delete = False
    model = Actor



class FilmAdmin(admin.ModelAdmin):
    inlines = (ActorInLine,)