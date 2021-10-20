from django.urls.conf import path
from .views import ListingLikeLookup, ListingLookup, ListingsAll, ListingCreate, ListingDelete, ListingUpdate, ListingLike

urlpatterns = [
    path('', ListingsAll.as_view(), name="listings_all"),
    path('create', ListingCreate.as_view(), name="listing_create"),
    path('delete/<pk>', ListingDelete.as_view(), name="listings_delete"),
    path('update/<pk>', ListingUpdate.as_view(), name="listings_update"),
    path('<pk>/like', ListingLike.as_view(), name="listings_like"),
    path('<pk>', ListingLookup.as_view(), name="listing_lookup"),
    path('<pk>/likeCount', ListingLikeLookup.as_view(), name="listinglike_lookup" )
]