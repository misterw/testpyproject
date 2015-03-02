from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from testpyproject.news.models import News

def news_page(request):
    news_list = News.objects.order_by('datetime').reverse().all()
    paginator = Paginator(news_list, 20)

    page_num = request.GET.get('page')
    try:
        news = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)

    return render(request, "news/index.html", {'news': news})


def simple_news_page(request, news_id):
    return render(request, "news/index.html")
