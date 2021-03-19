from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_quiz, name='render_quiz')
]