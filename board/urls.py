from django.urls import path
from . import views

# 네임스페이스
# 사용할때는 board:question_detail 와 같이 사용
app_name = 'board'  # board 앱의 URL 네임스페이스 설정

urlpatterns = [
    path('', views.index, name='question_list'),  # board 앱의 index 뷰를 기본 URL로 설정
    path('<int:question_id>/', views.detail, name='question_detail'),  # 질문 상세 페이지 URL
    path('ask/create/<int:question_id>/',
         views.create_answer, name='create_answer'),  # 답변 생성 URL
    
    path('question/create/', views.create_question, name='create_question')
]