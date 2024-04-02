from django.urls import path
from .views import PostListView, PostDetailView, PostFromCategory, PostCreateView, PostUpdateView, CommentCreateView, \
    PostByTagListView, RatingCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment_create_view'),
    path('post/tags/<str:tag>/', PostByTagListView.as_view(), name='post_by_tags'),
    path('category/<str:slug>/', PostFromCategory.as_view(), name="post_by_category"),
    path('rating/', RatingCreateView.as_view(), name='rating'),
]
