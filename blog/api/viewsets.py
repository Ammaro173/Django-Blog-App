from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from blog.models import Article

from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly


class ArticleListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)  # always tuple remeber!!
