from django.urls import path , re_path

from . import views





urlpatterns = [
    path('upload/', views.base_upload, name='base_upload'),
    path('show_bases/', views.show_bases, name='show_bases')
]


