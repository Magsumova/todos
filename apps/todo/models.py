from django.db import models

from abstracts.models import AbstractDateTime

class Task(AbstractDateTime):

    title = models.CharField(
        verbose_name='Тема',
        max_length=20,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание задания',
        null=False,
        blank=False
    )
    todo = models.CharField(
        verbose_name='Задание',
        max_length=20,
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активность',
        null=False
    )
    
    def __str__(self) -> str:
        return f'Задание {self.id}: {self.todo}'

    class Meta:
        ordering = (
            'id',
        )
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'