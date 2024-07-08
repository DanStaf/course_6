from django.urls import path
from blog.apps import BlogConfig
from django.views.decorators.cache import never_cache
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog'),
    path('<int:pk>', ArticleDetailView.as_view(), name='view_article'),
    path('create', ArticleCreateView.as_view(), name='create_article'), # never_cache
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update_article'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete_article'),
]
