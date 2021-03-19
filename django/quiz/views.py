from django.shortcuts import render

def render_quiz(request):
    return render(request, 'quiz/index.html', {})