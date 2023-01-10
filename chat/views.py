from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
import random
from chat.models import Article, Comment

# Create your views here.
def index(request):
	if request.method == 'POST':
		article =Article(title=request.POST['title'], body=request.POST['text'])
		article.save()
		return redirect(detail, article.id)
		
	context = {
		"articles" : Article.objects.all()
	}
	return render(request, 'chat/index.html', context)



def hello(request):
	data = {
		'name' : 'Alice',
		'weather' : 'CLOUDY',
		'fortune' : 'Great Fortune!'
	}
    
	return render(request, 'chat/hello.html',data)


def redirect_test(request):
	return redirect(hello)

def detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article dosw not exist")

	if request.method=='POST':
		comment=Comment(article=article, text=request.POST['text'])
		comment.save()

	context = {
		"article": article,
		'comments': article.comments.order_by('-posted_at')
	}
	return render(request, "chat/detail.html", context)

def update(request, article_id):
	context = {
		"article_id" : article_id
	}
	return render(request, "chat/tbd.html", context)

def delete(request, article_id):
 try:
  article = Article.objects.get(pk=article_id)
 except Article.DoesNotExist:
  raise Http404("Article does not exist")
 article.delete()
 return redirect(index)
 