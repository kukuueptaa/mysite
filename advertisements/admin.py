from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html
from django.conf import settings


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'auction', 'price', 'created_date', 'updated_date', 'get_thumbnail']
    list_filter = ['auction', 'created_at']
    search_fields = ['title']
    actions = ['mark_auction_as_true', 'mark_auction_as_false']
    fieldsets = (
        ("Общая информация", {
            'fields': ('title', 'description', 'user', 'image'),
            'classes': ['collapse']
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.display(description='Фото')
    def get_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50">'.format(obj.image.url))
        else:
            default_image = settings.STATIC_URL + 'img/adv.png'
            return format_html('<img src="{}" width="50" height="50">'.format(default_image))


    @admin.action(description='Добавить возможность торга')
    def mark_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='Убрать возможность торга')
    def mark_auction_as_false(self, request, queryset):
        queryset.update(auction=False)


#admin.site.register(Advertisement, AdvertisementAdmin)

