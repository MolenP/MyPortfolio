from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@require_POST  # Запрещает доступ через GET-запросы
def logout_view(request):
    logout(request)
    return redirect('home')


def article_list(request):
    user_id = None
    user_name = None
    if request.user.is_authenticated:
        user_id = request.user.id
        user_name = request.user.username
    
    articles = Article.objects.all().order_by('-date')

    return render(request, 'article_list.html', {'articles': articles, 'user_id': user_id, 'user_name': user_name})

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'article.html', {'article': article})


def create_article(request):
    if not request.user.is_authenticated:
        return

    user = request.user

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = user
            article.save()
    
            return redirect('home')

    else:
        form = ArticleForm()

    return render(request, 'create_article.html', {'form': form})

def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = ArticleForm(instance=article)

    return render(request, 'edit_article.html', {'form': form})

def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user_id = request.user.id

    if article.author.id == user_id:
        article.delete()

    return redirect('home')