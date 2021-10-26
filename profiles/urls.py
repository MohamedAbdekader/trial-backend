from django.urls import path
from .views import ProfileDelete, ProfileUpdate, ProfileList, ProfileCreate, ProfileView

urlpatterns = [
    path('create', ProfileCreate.as_view(), name="create_user"),
    path('delete/<pk>', ProfileDelete.as_view(), name="delete_user"),
    path('update/<pk>', ProfileUpdate.as_view(), name="update_user"),
    path('view/<pk>', ProfileView.as_view(), name="view_user"),
    path('', ProfileList.as_view(), name='list'),
]