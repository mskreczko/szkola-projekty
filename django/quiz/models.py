from django.db import models


class Question(models.Model):
    question_content = models.TextField(default='some_string')
    answer_a = models.TextField(default='some_string')
    answer_b = models.TextField(default='some_string')
    answer_c = models.TextField(default='some_string')
    answer_d = models.TextField(default='some_string')
    correct_answer = models.TextField(default='some_string')
