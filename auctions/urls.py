from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("bid", views.bid, name="bid"),
    path("watch_list", views.watch_list, name="watch_list"),
    path("remove_from_watch_list", views.remove_from_watch_list, name='remove_from_watch_list'),
    path("end_auction", views.end_auction, name="end_auction"),
    path("closed_listings", views.closed_listings, name="closed_listings"),
    path("comment", views.comment, name="comment"),
    path("Categories", views.Categories, name="Categories"),
    path("closed/<int:id>", views.closed, name="closed"),
    path("listing/<int:id>", views.listing, name="listing")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
