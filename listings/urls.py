from django.urls.conf import path
from .views import ListingsAll, ListingCreate, ListingDelete

urlpatterns = [
    path('', ListingsAll.as_view(), name="listings_all"),
    path('create', ListingCreate.as_view(), name="listing_create"),
    path('delete/<pk>', ListingDelete.as_view(), name="listings_delete"),
]