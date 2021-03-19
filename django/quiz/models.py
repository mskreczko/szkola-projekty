from django.db import models


class Question(models.Model):
    question_content = models.TextField()
    answers = []
    correct_answer = models.PositiveIntegerField()
