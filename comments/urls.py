from django.urls.conf import path
from .views import CommentLookup, CommentCreate, CommentDelete, CommentUpdate

urlpatterns = [
    path('', CommentLookup.as_view(), name="comment_lookup"),
    path('create', CommentCreate.as_view(), name="comment_create"),
    path('delete/<pk>', CommentDelete.as_view(), name="comment_delete"),
    path('update/<pk>', CommentUpdate.as_view(), name="comment_update"),
]