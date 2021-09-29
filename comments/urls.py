from django.urls.conf import path
from .views import CommentsAll, CommentCreate, CommentDelete, CommentUpdate

urlpatterns = [
    path('', CommentsAll.as_view(), name="comments_all"),
    path('create', CommentCreate.as_view(), name="comment_create"),
    path('delete/<pk>', CommentDelete.as_view(), name="comment_delete"),
    path('update/<pk>', CommentUpdate.as_view(), name="comment_update"),
]