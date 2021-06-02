from django.contrib import admin

from .models import Ages, Brands, Types, Prices, Cosmetics, Preferences

admin.site.register(Ages)
admin.site.register(Brands)
admin.site.register(Types)
admin.site.register(Prices)
admin.site.register(Cosmetics)
admin.site.register(Preferences)
