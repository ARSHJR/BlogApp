from django.urls import path, include
from blog import views
from .views import Index, DetailedArticleView, LikeArticle, Featured

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>/', DetailedArticleView.as_view(), name='detail_article'), #primary key
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('featured', Featured.as_view(), name='featured'),
]