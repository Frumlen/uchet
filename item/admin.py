from django.contrib import admin
from item.models import Region, Category, Item, ItemImage
import re


from django.contrib import admin


class ImageInline(admin.TabularInline):
    model = ItemImage
    fields = ('image', )
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'comment', 'count')
        }),
        ('Дополнительно', {
            'classes': ('collapse',),
            'fields': ('region', 'price_buy', 'price_sell', 'description', 'material', )
        }),
    )
    inlines = [
        ImageInline,
    ]

    list_display = [
        'articul',
        'name',
        'comment',
        'description',
        'material',
        'region',
        'price_buy',
        'price_sell',
        'count',
        'created'
    ]
    search_fields = ['id', 'name', 'description', ]

admin.site.register(Item, ItemAdmin)
