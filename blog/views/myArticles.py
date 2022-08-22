from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def myArticles(request):
    articles = request.user.articles.order_by("-id")
    page = request.GET.get('page')
    paginator = Paginator(articles, 10)

    return render(request, "pages/my-articles.html", context={
        "articles": paginator.get_page(page),
    })
