from django.shortcuts import render
from .models import Question

def render_quiz(request):
    questions = Question.objects.all()
    return render(request, 'quiz/index.html', {'questions': questions})