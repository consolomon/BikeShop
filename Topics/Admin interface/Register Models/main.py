from django.contrib import admin


class RatingAdmin(admin.ModelAdmin):
    fields = ("film", "user", "value")


admin.site.register(Rating, RatingAdmin)