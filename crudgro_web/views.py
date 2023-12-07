from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
# Z URLS ODSYLA TUTAJ
def test_response(request):
    return HttpResponse("PRZYKLAD URL")


def all_articles(request):
    title_page = "To jest tytuł strony"
    options = [
        "option 1",
        "option 2",
        "option 3"
    ]

    articles = Article.objects.all()

    return render(
        request,
        'template.html',
        {
            'title': title_page,
            'options': options,
            'articles': articles
        }
    )
def index(response):
    title_article = "artykuly"
    return render(response, "template.html", {"title_article_view": title_article})
