from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', 1)  # GET 요청에서 'page' 파라미터를 가져옴, 기본값은 1
    questions = Question.objects.order_by('-created_at')  # 질문을 생성 시간 기준으로 내림차순 정렬
    paginator = Paginator(questions, 10)  # Paginator 객체 생성, 한 페이지에 10개의 질문 표시
    paginated_questions = paginator.get_page(page)  # 현재 페이지에 해당하는 질문 목록 가져오기

    return render(request, 'board/index.html', {'questions': paginated_questions})


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

# 임시로 Question 객체를 100개 생성하는 뷰
def test(request):
    # Question 객체 100개 생성
    for i in range(1, 101):
        Question(
            subject=f'질문 {i}', 
            content=f'질문 내용 {i}').save()
    return HttpResponse('100개의 질문이 생성되었습니다.')