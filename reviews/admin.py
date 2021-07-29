from django.contrib import admin
from .models import SeriesReviews
# Register your models here.
class SeriesReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'serie_name', 'serie_genre', 'serie_rating']
    list_display_links = list_display

admin.site.register(SeriesReviews, SeriesReviewsAdmin)