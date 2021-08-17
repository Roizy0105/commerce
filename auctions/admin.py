from django.contrib import admin

from .models import User, Listings, Bids, Watch_list, Closed_listings, Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Bids)
admin.site.register(Watch_list)
admin.site.register(Closed_listings)
admin.site.register(Comments)
