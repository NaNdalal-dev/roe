from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home-articles'),
    path('about', views.about, name='about'),

    path('business',views.business,name='business-articles'),
    path('entertainment',views.entertainment,name='entertainment-articles'),
    path('general2',views.general,name='general-articles2'),
    path('health',views.health,name='health-articles'),
    path('science',views.science,name='science-articles'),
    path('sports',views.sports,name='sports-articles'),
    path('technology',views.technology,name='technology-articles'),
    path('search',views.search,name='search-articles')
]