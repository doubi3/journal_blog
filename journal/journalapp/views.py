from django.shortcuts import render
from .models import Article
from django.views import generic
# Create your views here.


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by('-published_on')
    template_name = 'index.html'


class ModelDetailView(generic.DetailView):
    model = Article
    template_name = "article_detail.html"
