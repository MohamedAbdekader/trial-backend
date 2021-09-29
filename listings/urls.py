from django.urls.conf import path
from .views import ListingLookup, ListingsAll, ListingCreate, ListingDelete, ListingUpdate

urlpatterns = [
    path('', ListingsAll.as_view(), name="listings_all"),
    path('create', ListingCreate.as_view(), name="listing_create"),
    path('delete/<pk>', ListingDelete.as_view(), name="listings_delete"),
    path('update/<pk>', ListingUpdate.as_view(), name="listings_update"),
    path('<pk>', ListingLookup.as_view(), name="listing_lookup"),
]