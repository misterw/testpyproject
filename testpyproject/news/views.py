from django.shortcuts import render


def news_page(request):
    return render(request, "news/index.html")


def simple_news_page(request, news_id):
    return render(request, "news/index.html")
