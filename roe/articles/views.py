from django.shortcuts import render

from django.http import HttpResponse
from newsapi import NewsApiClient
#k = open('.k','r')
#k = k.readline().split('\n')[0]
api = NewsApiClient(api_key='81a9b72f08c345d6b54b226c6e5f6efe')

def home(request):
	data = api.get_top_headlines()
	head = 'Top Headlines'
	articles = data['articles']
	return render(request,'articles/home.html',{'articles':articles,'head':head})

def about(request):
	return HttpResponse('About Page.')

def business(request):
	ar = api.get_everything(q='business',language='en',sort_by='relevancy')
	ar = ar['articles']
	return render(request,'articles/home.html',{'articles':ar})

def entertainment(request):
	ar = api.get_everything(q='entertainment',language='en',sort_by='relevancy')
	ar = ar['articles']
	return render(request,'articles/home.html',{'articles':ar})

def general(request):
	ar = api.get_everything(q='general',language='en',sort_by='relevancy')
	ar = ar['articles']
	return render(request,'articles/home.html',{'articles':ar})

def health(request):
	ar = api.get_everything(q='health',language='en',sort_by='relevancy')
	ar = ar['articles']
	return render(request,'articles/home.html',{'articles':ar})

def science(request):
	ar = api.get_everything(q='science',language='en',sort_by='relevancy')
	ar = ar['articles']
	return render(request,'articles/home.html',{'articles':ar})

def sports(request):
	ar = api.get_everything(q='sports',language='en',sort_by='relevancy')
	ar = ar['articles']
	return render(request,'articles/home.html',{'articles':ar})

def technology(request):
	ar = api.get_everything(q='technology',language='en',sort_by='relevancy')
	ar = ar['articles']
	return render(request,'articles/home.html',{'articles':ar})

def search(request):
	q = (request.GET['query'])
	ar = api.get_everything(q=q,language='en',sort_by='relevancy')
	ar = ar['articles']
	return render(request,'articles/home.html',{'articles':ar})

error404 = lambda request,exception: HttpResponse('<h1>Page Not Found.<h1>')