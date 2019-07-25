from django.contrib import admin
from .models import Places, Photos, Review
# Register your models here.
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'maps']
    list_display_links = ['id', 'name']
    search_fields = ['name']

class PhotosAdmin(admin.ModelAdmin):
    list_display = ['id', 'place_name', 'pic_url']
    list_display_links = ['id', 'pic_url']
    search_fields = ['place_name']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'place_name', 'review']
    list_display_links = ['id', 'review']
    search_fields = ['place_name']

admin.site.register(Places, PlacesAdmin)
admin.site.register(Photos, PhotosAdmin)
admin.site.register(Review, ReviewAdmin)