from django.contrib import admin
from .models import Category, Movie, MoviShots, RatingStar, Rating, Reviews, Cinema, News


class CinemaAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'description', 'address', 'contact_phone']


admin.site.register(News)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(MoviShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
