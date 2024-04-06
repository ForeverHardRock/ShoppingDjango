from django.core.exceptions import ValidationError
from django.db import models


class FAQ(models.Model):
    q_a_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def clean(self):
        if FAQ.objects.filter(question=self.question).exists() and self.q_a_id is None:
            raise ValidationError("Такой вопрос уже существует")