from django.urls.conf import path
from .views import CommentsAll, CommentCreate

urlpatterns = [
    path('', CommentsAll.as_view(), name="comments_all"),
    path('create', CommentCreate.as_view(), name="comment_create"),
]