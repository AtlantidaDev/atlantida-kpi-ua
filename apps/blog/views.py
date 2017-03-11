from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def articles(request, article_id):
    return render(request, 'blog/article.html', {
        "article": {
            "id": article_id,
            "title": "Title"
        }
    })
