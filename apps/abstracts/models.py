from django.db import models

class AbstractDateTime(models.Model):

    datetime_created = models.DateTimeField(
        verbose_name='Время создания',
        auto_now=True
    )

    datetime_deleted = models.DateTimeField(
        verbose_name='Время удаления',
        null=True,
        blank=True,
        auto_now=True
    )

    datetime_live = models.DateTimeField(
        verbose_name='Время обноаления',
        null=True,
        blank=True,
        auto_now=True
    )

    class Meta:
        abstract=True
