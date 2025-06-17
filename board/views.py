from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer

def index(request):
    questions = Question.objects.order_by('-created_at')  # 질문을 생성 시간 기준으로 내림차순 정렬
    return render(request, 'board/index.html', {'questions': questions})

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)  # 주어진 ID에 해당하는 질문이 없으면 404 에러 발생
    return render(request, 'board/detail.html', {'question': question})