from django.urls import path
from .views import ProfileView

urlpatterns = [
    # path('create', UserCreate.as_view(), name="create_user"),
    # path('delete/:<pk>', UserDelete.as_view(), name="delete_user"),
    path('view/:<pk>', ProfileView.as_view(), name="view_user"),
]