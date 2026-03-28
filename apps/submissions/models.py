from django.db import models
from .choices import TaskType, SubmissionStatus


class Submission(models.Model):

    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО студента',
        db_index=True
    )

    group_name = models.CharField(
        max_length=100,
        verbose_name='Название группы',
        db_index=True
    )

    task_type = models.CharField(
        max_length=20,
        choices=TaskType.choices,
        default=TaskType.PYTHON,
        verbose_name='Тип задания',
        db_index=True
    )

    task_description = models.TextField(
        verbose_name='Условие задания'
    )

    student_code = models.TextField(
        verbose_name='Код или текст ответа студента'
    )

    score = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Оценка (0–100)'
    )

    ai_feedback = models.TextField(
        null=True,
        blank=True,
        verbose_name='Полный комментарий ИИ'
    )

    short_comment = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Краткое резюме'
    )

    is_ai_generated = models.BooleanField(
        default=False,
        verbose_name='Сгенерировано ИИ?'
    )

    status = models.CharField(
        max_length=20,
        choices=SubmissionStatus.choices,
        default=SubmissionStatus.CHECKING,
        verbose_name='Статус проверки',
        db_index=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время сдачи',
        db_index=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Сдача задания'
        verbose_name_plural = 'Сдачи заданий'

    def __str__(self):
        return f'{self.full_name} – {self.get_task_type_display()}'

    def save(self, *args, **kwargs):

        if self.score is not None and self.score > 100:
            self.score = 100
        super().save(*args, **kwargs)
