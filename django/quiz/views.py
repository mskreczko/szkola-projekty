from django.shortcuts import render
from .models import Question

def render_quiz(request):
    questions = Question.objects.all()
    return render(request, 'quiz/index.html', {'questions': questions})

def render_score(request):
    result = 0
    correct_answers = dict(request.POST)['quiz_correct_answer']
    for key in request.POST:
       if len(key.split("|")) > 1:
           question_number = int(key.split("|")[1])
           if request.POST[key] == correct_answers[question_number-1].replace(" ", ""):
               result += 1
    return render(request, 'quiz/index.html', {'result': str(result)})