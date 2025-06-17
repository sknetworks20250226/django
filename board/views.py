from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer

def index(request):
    questions = Question.objects.order_by('-created_at')  # 질문을 생성 시간 기준으로 내림차순 정렬
    return render(request, 'board/index.html', {'questions': questions})

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)  # 주어진 ID에 해당하는 질문이 없으면 404 에러 발생
    return render(request, 'board/detail.html', {'question': question})

def create_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)  # 주어진 ID에 해당하는 질문이 없으면 404 에러 발생
    Answer(question=question,
           content =request.POST.get('content')).save()  # POST 요청에서 'content' 필드의 값을 가져와 답변 생성
    return redirect('board:question_detail', question_id=question.id)  # 질문 상세 페이지로 리다이렉트

def create_question(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        Question(subject=subject, content=content).save()        
        return redirect('board:question_list')
    return render(request, 'board/create_question.html')