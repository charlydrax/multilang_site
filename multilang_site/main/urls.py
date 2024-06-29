from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
#on donne une vue à l'url de base (vide) et chaque fois que l'on cliquera sur un article, son slug sera mis dans l'url
urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:Slug>/', views.DetailView.as_view(), name="post_detail"),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_root)