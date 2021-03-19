from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_quiz, name='render_quiz'),
    path('evaluate/', views.render_score, name='render_score')
]