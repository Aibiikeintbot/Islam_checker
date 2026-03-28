from django.db import models

class TaskType(models.TextChoices):
    HTML = 'html', 'HTML/CSS'
    JS = 'js', 'JavaScript'
    PYTHON = 'python', 'Python'
    ENGLISH = 'english', 'English'

class SubmissionStatus(models.TextChoices):
    CHECKING = 'checking', 'В ожидании'
    PROCESSING = 'processing', 'Проверяется'
    DONE = 'done', 'Готово'
    ERROR = 'error', 'Ошибка'