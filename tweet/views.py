from django.http import HttpResponse
from django.shortcuts import render, redirect
from tweet.models import Article
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    articles = Article.objects.all().order_by('-created_at')
    context={
        'articles':articles
    }
    # for article in articles:
    #     print(article)
    #     print(article.content)
    #     print(article.user) -> 값이 username이 나오는 이유는 대표값이 username이기 때문! __str__로 대표값을 지정해주면 그 값으로 나온다!
    #     print(article.user.last_login)
    # user를 users앱에서 foreign key로 가져왔기 때문에 user값와 user.last_login값 등을 가져올 수 있다.
    return render(request, 'index.html', context)

def create_article(request):
    if request.method == 'GET':
        return render(request, 'create_article.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        Article.objects.create(title=title, content=content, user=user)
        # 26, 27번째줄을 한번에 작성하면 Article.objects.create(title=title, content=content, user=request.user) 이다.
        
        return redirect('tweet:index')
    
def article_detail(request, article_id):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
        context = {
            'article': article
        }
        # html에서 context안에 들어있는 데이터를 이용할 수 있다.
        return render(request, 'article_detail.html', context)

def update_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.user != article.user:
        return HttpResponse("권한이 없습니다.")
    if request.method == 'GET':
        context = {
        'article': article
        }    
        return render(request, 'update_article.html', context)
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article.title = title
        # article.content = content
        # 50, 51번줄과 결과가 같다.
        article.save()
        return redirect('tweet:article_detail', article_id)
        
def delete_article(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(id=article_id)
        if request.user != article.user:
            return HttpResponse("권한이 없습니다.")
        article.delete()
        return redirect('tweet:index')
    
