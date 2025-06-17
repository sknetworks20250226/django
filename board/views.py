from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer

def index(request):
    questions = Question.objects.order_by('-created_at')  # 질문을 생성 시간 기준으로 내림차순 정렬
    return render(request, 'board/index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)    
    return render(request, 'board/detail.html', {'question': question})