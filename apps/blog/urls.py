from django.urls import path
from .views import PostListView, PostDetailView, PostFromCategory, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<str:slug>/', PostFromCategory.as_view(), name="post_by_category"),

]