from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),  # board 앱의 index 뷰를 기본 URL로 설정
    path('test/abc/', views.index),  # board 앱의 index 뷰를 기본 URL로 설정
]