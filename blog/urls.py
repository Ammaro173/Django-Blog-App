from django.urls import path, include
from blog.api.viewsets import ArticleListView, ArticleDetailView

urlpatterns = [
    path("articles-list/", ArticleListView.as_view(), name="articles-list"),
    path(
        "articles-detail/<int:pk>", ArticleDetailView.as_view(), name="articles-detail"
    ),
]
