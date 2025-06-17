from django.contrib import admin

# Register your models here.
from .models import Question, Answer

# Question 모델을 관리자 사이트에 등록
# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # list_display = ('subject', 'created_at', 'updated_at')  # 관리자 페이지에서 보여줄 필드 설정
    search_fields = ['subject']  # 검색 기능을 위한 필드 설정

admin.site.register(Question, QuestionAdmin)  # Question 모델과 QuestionAdmin을 연결
