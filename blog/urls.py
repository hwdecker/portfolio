from django.urls import path
from .views import PostListView

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog-home'),
]